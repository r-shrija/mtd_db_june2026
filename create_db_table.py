#import pymysql
import db_connect2 as dbc
def create_db():
    query="create database if not existsshrija_db"
    try:
        connection=dbc.db_connect()
        cursor=connection.cursor()
        result=cursor.execute(query)
        connection.commit()
        cursor.close()
        #connection.close()
        dbc.db_disconnect(connection)
        if(result==1):
            print("Table created successfully")
        else:
            print("Table already exists")
    except Exception as e:
        print("Database creation failed",e)
def create_table():
    #query="create table if not exists employee(id int primary key auto_increment,name varchar(50),age int,department varchar(255),designation varchar(255),salary float,commission float default 0.0,years_of_experience tiny int,phone_number bigint unique)"
    query = 'create table if not exists employees(id int primary key auto_increment, name varchar(255) not null, designation varchar(255), salary float, phone_number bigint unique)'
    try:
        connection = dbc.db_connect()
        cursor = connection.cursor()
        result = cursor.execute(query)
        connection.commit()
        cursor.close()
        # connection.close()
        dbc.db_disconnect(connection)
        if result == 1:
            print('Table created successfully')
        else:
            print('Table already exists')
    except Exception as e:
        print('Error while creating table: e', e)

create_db()
create_table()
    
 