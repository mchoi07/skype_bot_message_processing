# skype_bot_message_processing

Abstract: Getting message from Skpye account and process it to S3 and HDFS in realtime, and set the batch job for any query or processing for every 6 hr - data in HDFS to Hive and data in S3 to another S3 or RDS in AWS

Update 3/23

Today the team added:
* The ability to monitor Skype messages using the SkPy module, using a loop which collects all incoming and outgoing messages
* A mechanism to save those messages to a file
* A mechanism to post the contents of that file to Amazon s3, then reset the file's contents

Tomorrow, the agenda is:
* Find a way to post the data from the file to HDFS as well
* explore batch processing options with Hive, s3, and RDS
