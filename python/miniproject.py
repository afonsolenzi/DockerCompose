import mysql.connector
import pymysql
import datetime as dt
import pandas as pd
from sqlalchemy import create_engine
from faker import Faker

fake = Faker(locale='pt_BR')
volume = []

for _ in range(10):
    
      volume.append ({
          'prefix': fake.prefix_nonbinary(),
          'name': fake.name_nonbinary(),
          'suffix': fake.suffix_nonbinary(),
          'phone': fake.phone_number(),
          'email': fake.ascii_free_email(),
          'address': fake.address()
      })
    
df = pd.DataFrame(volume)

df

########################################### CONNECT MYSQL ############################

from sqlalchemy import create_engine

## Parameter
engine      = 'mysql'
conect      = 'pymysql'
user        = 'root'
password    = 'root'
host        = 'mysql'
port        = "3306"
database    = 'db'
table       = 'tab_clientes'


engine  = create_engine(f"{engine}+{conect}://{user}:{password}@{host}:{port}/{database}")
conn    = engine.connect()

connection = mysql.connector.connect(user=user,password=password,host=host,port=port,database=database)

print("Connection ok!")

########################################### INSERT DATA INTO MYSQL ############################
records = df.values.tolist()

mySql_insert_query = f"""INSERT INTO {table} (prefix, name, suffix, phone,email,address)
                           VALUES (%s, %s, %s, %s, %s, %s) """


cursor = connection.cursor()
cursor.executemany(mySql_insert_query, records) #execute rows ingestion
connection.commit()

print(cursor.rowcount, f"Record inserted successfully into {table} table")