import pymysql
connection=pymysql.connect(user='root',password='root',host='localhost',database='shrija',charset='utf8')
print("Database Connected")
connection.close()
print("Database disconnected")
