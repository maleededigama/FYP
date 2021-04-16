import psycopg2

conn = psycopg2.connect(
   database="fae", user='docker', password='docker', host='172.26.0.2', port= '5432'
)

conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()


#Preparing query to create a database
# sql = '''CREATE DATABASE  fae;''';
#  POSTGRES SQL dosnt have if not extxi command for DB
with open('sql/table_gen.sql' ,'r',encoding='utf-8') as f:
    sqls = f.read().split(';')[:-1]
    for sql in sqls:
        print(sql.strip())
        cursor.execute(sql)

#Closing the connection
conn.close()

