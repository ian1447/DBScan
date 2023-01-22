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

cursor.execute("SELECT id,name,epoch,room FROM logs")

result = cursor.fetchall()

all_id = []
all_name = []
all_date_int = []
all_time_int = []

for id, name, date_int, time_int in result:
    all_id.append(id)
    all_name.append(name)
    all_date_int.append(date_int)
    all_time_int.append(time_int)

dic = {'datetime': all_date_int, 'room': all_time_int, 'name': all_name}
df = pd.DataFrame(dic)
connection.close()
df.to_csv('exported.csv')
cursor.close()
#end sa pag convert to .csv

df = pd.read_csv('exported.csv')

#print(df.head())

# #SHOW PLOT
# plt.figure(figsize=(8,6))
# sns.scatterplot(x='date', y='time', data=df, hue='name')
# plt.legend(bbox_to_anchor= [1, 0.8])
# plt.show()
# epsilon = 0.26251178 # for not float
def get_infected_names(input_name):
    name_room = df[df['name'] == input_name]['room'].item()
    print(name_room)
    epsilon = 1
    model = DBSCAN(eps=epsilon, min_samples=2, metric='haversine').fit(df[['room', 'datetime']])
    df['cluster'] = model.labels_.tolist()

    input_name_clusters = []
    for i in range(len(df)):
        if df['name'][i] == input_name:
            if df['cluster'][i] in input_name_clusters:
                pass
            else:
                input_name_clusters.append(df['cluster'][i])

    infected_unique_names = []
    for cluster in input_name_clusters:
        if cluster != -1:
            ids_in_cluster = df.loc[df['cluster'] == cluster, 'name']
            for i in range(len(ids_in_cluster)):
                member_id = ids_in_cluster.iloc[i]
                if (member_id not in infected_unique_names) and (member_id != input_name):
                    infected_unique_names.append(member_id)
                else:
                    pass

    final_infected_names=[]
    for i in range(len(infected_unique_names)):
        if df[df['name'] == infected_unique_names[i]]['room'].item() == name_room:
            final_infected_names.append(infected_unique_names[i])

    return infected_unique_names



print('Enter Unique Name:')
name = input()
i_name = get_infected_names(name)
print("People Subject to Contact Tracing are:")
for i in i_name:
    print([i])
