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
          f1.write(
            str(event.msg.id) + "\t" +
            str(event.msg.type) + "\t" +
            str(event.msg.time) + "\t" +
            str(event.msg.clientId) + "\t" +
            str(event.msg.userId) + "\t" +
            str(event.msg.chatId) + "\t" +
            content_payload + "\t" +
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
