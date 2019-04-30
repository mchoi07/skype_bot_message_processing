from skpy import Skype, SkypeEventLoop, SkypeNewMessageEvent
import boto3
import credentials
import random
import subprocess
import time
import re

sk = Skype(credentials.username, credentials.password)
s3_client = boto3.client('s3')

class SkypePing(SkypeEventLoop):
    def __init__(self):
        super(SkypePing, self).__init__(credentials.username, credentials.password)
    def onEvent(self, event):
        if isinstance(event, SkypeNewMessageEvent):
          print(event.msg)

          f1 = open('data.tsv', 'a')
          content_payload = re.sub('\s+', " ", str(event.msg.content))

          chat_name_array = str(event.msg.chatId).split(":")
          if chat_name_array[0] == '19':
              chat_name = str(sk.chats[str(event.msg.chatId)].topic)
          else:
              # chat_name = str(sk.chats[str(event.msg.chatId)].userId) # based on the user id
              chat_name = str(sk.chats[str(event.msg.chatId)].user.name) # need to format the username in case of unusual characters

          f1.write(
            str(event.msg.id) + "\t" +
            str(event.msg.type) + "\t" +
            str(event.msg.time) + "\t" +
            str(event.msg.clientId) + "\t" +
            str(event.msg.userId) + "\t" +
            str(event.msg.chatId) + "\t" +
            chat_name + "\t" +
            content_payload +
            "\n"
            )

          f2 = open('data.tsv', 'r')
          f2.seek(0)

          if (len(f2.readlines())) > 1:
              production_file_name = "file{}".format(format(time.time())) + ".tsv"
              s3_client.upload_file('data.tsv', "skype-bucket-01", production_file_name)
              subprocess.call(["hdfs", "dfs", "-put", 'data.tsv', 'skype_bot_data/' + production_file_name])
              open("data.tsv", "w") # erases the contents of the file
              print('writing to s3')
              print('writing to hdfs')



lp = SkypePing()
lp.loop()

# Hive create table command:
# create table skype_data (id string, type string, time string, clientId string, userId string, chatId string, chatName string, content string) row format delimited fields terminated by '\t' lines terminated by '\n';
