import os
from flask_mysqldb import MySQL
from flask import Flask

app=Flask(__name__)

mydb=MySQL(app)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='GALGALLO10'
app.config['MYSQL_DB']='MEMES'

list_of_domains=[]
def search_url():
    with app.app_context():
        cursor=mydb.connection.cursor()
        cursor.execute('SELECT * FROM DOMAINS')
    domains=cursor.fetchall()
    for domain in domains:
        for minidomain in domain:
            list_of_domains.append(minidomain)

    print(list_of_domains)

#insert into the Database
domain='https://nairobiwire.com/wp-content/uploads/2021/09/trend{}-15.jpg'
def insert_domain(domain):
    with app.app_context():
        cursor=mydb.connection.cursor()
        cursor.execute('INSERT INTO DOMAINS(URL)VALUES(%s)',(domain,))
        mydb.connection.commit()

insert_domain(domain)
search_url()