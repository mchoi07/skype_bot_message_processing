from skpy import Skype, SkypeEventLoop, SkypeNewMessageEvent
import boto3
import credentials
import random

sk = Skype(credentials.username, credentials.password)
s3_client = boto3.client('s3')


# s3 = boto3.resource('s3')
# BUCKET = "test"
#
# s3.Bucket(BUCKET).upload_file("your/local/file", "dump/file")



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










# sk.user # you
# sk.contacts # your contacts
# sk.chats # your conversations
#
#ch = sk.chats.create(["joe.4", "daisy.5"]) # new group conversation
#ch = sk.contacts["joe.4"].chat # 1-to-1 conversation

# ch = sk.contacts["shinray1"].chat
# print(ch)
# ch.sendMsg(content) # plain-text message
# ch.sendFile(open("song.mp3", "rb"), "song.mp3") # file upload
# ch.sendContact(sk.contacts["daisy.5"]) # contact sharing

# msgs = ch.getMsgs() # retrieve recent messages

# print(msgs[1])
          # and not event.msg.userId == self.userId:
          # and "ping" in event.msg.content:
            # print(msgs[0].content)
            # print(msgs[1].content)
          #   event.msg.chat.sendMsg("Pong!")
