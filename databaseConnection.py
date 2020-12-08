import mysql.connector
from mysql.connector import errorcode

config={
        'user':'******',
        'password':'********',
        'host':'127.0.0.1', 
        'database':'TaxiBookingSystem',
        'raise_on_warnings':True
        }
try:
    con=mysql.connector.connect(**config)

except mysql.connector.Error as err:
    if err.errno--errorcode.ER_ACCES_DENIED_ERROR:
        print("Something is wrong with your username or password")
    elif err.erno==errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
     con.close()


