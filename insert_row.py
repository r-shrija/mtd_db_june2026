import pymysql
import db_connect2 as dbc

def insert_row():
    query = """insert into employees(name, designation, salary, phone_number) values('John Doe', 'Software Engineer', 75000.0, 1234567890)"""
    try:
        connection = dbc.db_connect()
        cursor = connection.cursor()
        result = cursor.execute(query)
        connection.commit()
        cursor.close()
        dbc.db_disconnect(connection)
        if result == 1:
            print("Row inserted successfully")
        else:
            print("Failed to insert row")
    except Exception as e:
        print("Error while inserting row: ", e)

insert_row()