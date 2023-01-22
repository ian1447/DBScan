import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mysql.connector
from mysql.connector import Error
from sklearn.neighbors import NearestNeighbors # importing the library
from sklearn.cluster import DBSCAN
import seaborn as sns

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

cursor.execute("SELECT name,date_int,time_int FROM users")

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


#start reading csv file
df = pd.read_csv('exported.csv')
epsilon = 100  # a radial distance of 6 feet in kilometers
model = DBSCAN(eps=epsilon, min_samples=9).fit(df[['date', 'time']])
df['cluster'] = model.labels_.tolist()
x = df.loc[:, ['date',
                 'time']].values
input_name = "1"
labels = model.labels_ # getting the labels
plt.scatter(x[:, 0], x[:,1], c = labels, cmap= "plasma") # plotting the clusters
plt.xlabel("Date") # X-axis label
plt.ylabel("Time") # Y-axis label
plt.show() # showin

# x = dataFrame.loc[:, ['date',
#                  'time']].values
# dbscan = DBSCAN(eps = 8, min_samples = 2).fit(x) # fitting the model
input_name_clusters = []
for i in range(len(df)):
    if df['name'][i] == input_name:
        if df['cluster'][i] in input_name_clusters:
            pass
        else:
            input_name_clusters.append(df['cluster'][i])

infected_names = []
for cluster in input_name_clusters:
    if cluster != -1:
        ids_in_cluster = df.loc[df['cluster'] == cluster, 'name']
        for i in range(len(ids_in_cluster)):
            member_id = ids_in_cluster.iloc[i]
            if (member_id not in infected_names) and (member_id != input_name):
                infected_names.append(member_id)
            else:
                pass
print(infected_names)

#print(get_infected_names("SECRET"))
# df = pd.read_csv("exported.csv")
# df.head()
# print(df['name'].unique())
# plt.figure(figsize=(8,6))
# sns.scatterplot(x='date', y='time', data=df, hue='name')
# plt.legend(bbox_to_anchor= [1, 0.8])
# sns.jointplot(x='date', y='time', data=df, color='red', kind='kde')
# plt.tight_layout()
# epsilon = 0.0018288 # a radial distance of 6 feet in kilometers
# model = DBSCAN(eps = epsilon, min_samples = 2, metric = 'haversine').fit(df[['date', 'time']])
# df['cluster'] = model.labels_.tolist()
# labels = model.labels_
# fig = plt.figure(figsize=(12,10))
# sns.scatterplot(df['date'], df['time'], hue = ['cluster-{}'.format(x) for x in labels])
# plt.legend(bbox_to_anchor = [1, 1])


#lahi nga style
# print("Dataset shape:", data.shape)

# x = dataFrame.loc[:, ['date',
#                  'time']].values
# print(x.shape)
#


# neighb = NearestNeighbors(n_neighbors=2) # creating an object of the NearestNeighbors class
# nbrs=neighb.fit(x) # fitting the data to the object
# distances,indices=nbrs.kneighbors(x) # finding the nearest neighbours
#
# distances = np.sort(distances, axis = 0) # sorting the distances
# distances = distances[:, 1] # taking the second column of the sorted distances
# plt.rcParams['figure.figsize'] = (5,3) # setting the figure size
# plt.plot(distances) # plotting the distances
#
# # cluster the data into five clusters
# dbscan = DBSCAN(eps = 8, min_samples = 2).fit(x) # fitting the model
# labels = dbscan.labels_ # getting the labels
# plt.scatter(x[:, 0], x[:,1], c = labels, cmap= "plasma") # plotting the clusters
# plt.xlabel("Date") # X-axis label
# plt.ylabel("Time") # Y-axis label
# plt.show() # showin

