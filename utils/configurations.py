import configparser
import mysql.connector
from mysql.connector import Error


def getConfig():
    config = configparser.ConfigParser()
    config.read('D:\\QA COURSE\\API_Testing_Python\\BackEndAutomation\\utils\\properties.ini')
    return config


config_connection = {
    'host': getConfig()['SQL']['host'],
    'database': getConfig()['SQL']['database'],
    'user': getConfig()['SQL']['user'],
    'password': getConfig()['SQL']['password']
}


def getPassword():
    return 'GitHub2022@@##'


def getToken():
    return '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'


def getURL():
    return getConfig()['API']['endpoint']


def getPetURL():
    return getConfig()['API']['petStore_EP']


def establish_DB_Connection():
    try:
        conn = mysql.connector.connect(**config_connection)
        if conn.is_connected():
            print("Connection Successful!")
            return conn
    except Error as e:
        print(e)


def getQuery(query):
    connection = establish_DB_Connection()
    cursor = connection.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    print(row)
    connection.close()
    return row


def updateQuery(query):
    connection = establish_DB_Connection()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()

