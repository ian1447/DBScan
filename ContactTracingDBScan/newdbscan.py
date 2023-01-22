import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# matplotlib inline
import datetime as dt
from sklearn.cluster import DBSCAN
import mysql.connector
from mysql.connector import Error

#convert sql to .csv
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='contact_tracer',
                                         user='root',
                                         password='password',
                                         port='3307')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
# finally:
#     if connection.is_connected():
#         cursor.close()
#         connection.close()
#         print("MySQL connection is closed")

cursor.execute("SELECT name,epoch,room FROM transactions")

result = cursor.fetchall()

all_name = []
all_date_int = []
all_time_int = []

for name,date_int,time_int in result:
    all_name.append(name)
    all_date_int.append(date_int)
    all_time_int.append(time_int)

dic = {'name' : all_name, 'time' : all_date_int, 'date' : all_time_int}
df = pd.DataFrame(dic)
df_csv = df.to_csv('exported.csv')
cursor.close()
#end sa pag convert to .csv

data = pd.read_csv('exported.csv')
print(data.head())