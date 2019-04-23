import credentials
import boto3
import random
import os
from skpy import SkypeEventLoop, SkypeNewMessageEvent
class SkypePing(SkypeEventLoop):
	def __init__(self):
		super(SkypePing, self).__init__(credentials.username, credentials.password)
	def onEvent(self, event):
		if isinstance(event, SkypeNewMessageEvent):#
 \
			f1 = open("s3.txt","a")
			f2 = open("s3.txt", "r")
			f1.write(str(event.msg.content) + '\n')
			f2.seek(0)
			if(len(f2.readlines()) > 9) :
				s3 = boto3.client('s3')
				bucket_name = 'skypedata'
				s3.upload_file("s3.txt", bucket_name, "dump/file {}".format(random.randint(0,1000)))
				os.remove("s3.txt")
				print("updating s3")
			print(event.msg)


sp = SkypePing()
sp.loop()
