import boto3
import sys
import json
import pymysql
import logging
import uuid
import csv
import credentials

s3_client = boto3.client('s3')

# RDS settings
rds_host = credentials.host
rds_uname = credentials.username
rds_password = credentials.password
rds_dbname = credentials.db_name

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(rds_host, port=credentials.port, user=rds_uname, passwd=rds_password, db=rds_dbname, connect_timeout=5)
except:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    sys.exit()
    
logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")

def lambda_handler(event, context):
    
    with conn.cursor() as cur:
        cur.execute("CREATE TABLE IF NOT EXISTS skypechats (id varchar(15) NOT NULL, type TEXT, time TEXT, clientId TEXT, userId TEXT, chatId TEXT, chatName TEXT, content TEXT, PRIMARY KEY(id))")
        conn.commit()
    
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        download_path = '/tmp/{}'.format(uuid.uuid4())

        s3_client.download_file(bucket, key, download_path)
        logger.info("downloaded file: " + download_path)
        with open(download_path, 'r') as f:
            reader = csv.reader(f, delimiter='\t')
            with conn.cursor() as cur:
                for row in reader:
                    logger.info(row)
                    try:
                        cur.execute('INSERT INTO skypechats (id, type, time, clientId, userId, chatId, chatName, content) VALUES ("%s","%s","%s","%s","%s","%s","%s","%s")', row)
                    except Exception as e:
                        logger.error(e)
                            # if idx % 100 == 0:
                            #     conn.commit()
            conn.commit()

