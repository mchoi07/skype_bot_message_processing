from skpy import Skype, SkypeEventLoop, SkypeNewMessageEvent
import boto3
import credentials
import random

sk = Skype(credentials.username, credentials.password)
s3_client = boto3.client('s3')

class SkypePing(SkypeEventLoop):
    def __init__(self):
        super(SkypePing, self).__init__(credentials.username, credentials.password)
    def onEvent(self, event):
        if isinstance(event, SkypeNewMessageEvent):# \
          s3 = boto3.client('s3')
          f1 = open('s3.txt', 'a')
          f2 = open('s3.txt', 'r')
          print(event.msg.content)
          f1.write(str(event.msg.content) + "\n")
          f2.seek(0)
          if (len(f2.readlines())) > 5:
              s3_client.upload_file("s3.txt", "skype-bucket-01", "dump/file {}".format(random.randint(0,1000)))
              open("s3.txt", "w") # erases the contents of the file
              print('writing to s3')



lp = SkypePing()
lp.loop()
