import mysql.connector
import sys
import boto3
import os

ENDPOINT="mysqldevdbudemy.cx7buk4u4a3b.us-west-2.rds.amazonaws.com"
PORT="3306"
USR="AdamMySqlDev"
REGION="us-east-1"
DBNAME="MySqlDevDBUdemy"
os.environ['LIBMYSQL_ENABLE_CLEARTEXT_PLUGIN'] = '1'

#gets the credentials from .aws/credentials
session = boto3.Session(profile_name='default')
client = boto3.client('rds')

token = client.generate_db_auth_token(DBHostname=ENDPOINT, Port=PORT, DBUsername=USR, Region=REGION)

try:
    conn =  pymysql.connect(host=ENDPOINT, user=USR, passwd=token, port=PORT, database=DBNAME)
    cur = conn.cursor()
    cur.execute("""SELECT now()""")
    query_results = cur.fetchall()
    print(query_results)
except Exception as e:
    print("Database connection failed due to {}".format(e))   