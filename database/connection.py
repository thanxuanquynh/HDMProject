from database.database import TABLES
from database.env import *
from mysql.connector import errorcode
import mysql.connector as connector
from database.SQLQuerry import *
from datetime import date, datetime, timedelta


cnx = None
cursor = None


def get_database_connection():
    global cnx
    if not cnx:
        cnx = connector.connect(
        host="127.0.0.1",
        port=3306,
        user=USER_NAME,
        password="")
    return cnx


def get_database_cursor():
    global cursor
    if not cursor:
        cursor = get_database_connection().cursor()
    return cursor


def init_database():
    create_database(get_database_cursor())
    create_table(get_database_cursor())


def create_table(cursor):
    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("Creating table {}: ".format(table_name), end='')
            cursor.execute(table_description)
        except connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")



def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DATABASE_NAME))
    except connector.Error as err:
        print("Failed creating database: {}".format(err))
    try:
        cursor.execute("USE {}".format(DATABASE_NAME))
    except connector.Error as err:
        print("Database {} does not exists.".format(DATABASE_NAME))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(cursor)
            print("Database {} created successfully.".format(DATABASE_NAME))
            get_database_connection().database = DATABASE_NAME
        else:
            print(err)


def insert_database(table_type, data):
    if table_type == Enum_Table.user.value:
        try:
            get_database_cursor().execute(add_users, data)
            get_database_connection().commit()
            return True
        except Exception as er:
            print(er)
            return False
