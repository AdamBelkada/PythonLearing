import pymysql

conn = pymysql.connect(
    host='mysqldevdbudemy.cx7buk4u4a3b.us-west-2.rds.amazonaws.com',
    port=int(3306),
    user="AdamMySqlDev",
    passwd="5Amc2aw09yE0",
    db="mysqldevdbudemy",
    charset='utf8mb4')
 

cur = conn.cursor()
cur.execute("""SELECT now()""")
query_results = cur.fetchall()
print(query_results)
conn.close()