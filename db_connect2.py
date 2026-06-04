import pymysql
def db_connect():
    connection=None
    try:
        connection=pymysql.connect(user='root',password='root',host='localhost',database='shrija',charset='utf8')
        print("Database Connected")
        #connection.close()
    except Exception as e:
        print("Db connection failed")
    return connection

def db_disconnect(connection):
    try:
        connection.close()
        print("Database disconnected")
    except:
        print("db disconnection failed") 

connection=db_connect()
db_disconnect(connection)
    
