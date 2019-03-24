#!/usr/bin/python
import MySQLdb
import database_secrets as secrets


db = MySQLdb.connect(host   = secrets.SQL_HOST,  # your host 
                     user   = secrets.SQL_USER,       # username
                     passwd = secrets.SQL_PASSWORD,     # password
                     db     = secrets.SQL_DB)   # name of the database
 
# Create a Cursor object to execute queries.
cur = db.cursor()
 
# Select data from table using SQL query.
cur.execute("SELECT * FROM examples")
 
# print the first and second columns      
for row in cur.fetchall() :
    print row[0], " ", row[1]
