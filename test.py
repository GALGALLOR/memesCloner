import mysql
import requests
from bs4 import BeautifulSoup
from instabot import Bot
import instaloader
from flask import Flask,request,render_template,redirect
import time
import os
import re
import random
import pyautogui
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #for pressing keys on the keyboard in chrome

from flask_mysqldb import MySQL
from flask import  get_flashed_messages, session,Flask,render_template,redirect,request,flash,url_for
app=Flask(__name__)

mydb=MySQL(app)

"""app.config['MYSQL_HOST']='LightAcademy.mysql.pythonanywhere-services.com'
app.config['MYSQL_USER']='LightAcademy'
app.config['MYSQL_PASSWORD']='KCDndogariyetu'
app.config['MYSQL_DB']='LightAcademy$default'"""

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='GALGALLO10'
app.config['MYSQL_DB']='MEMES'


def post_to_gram(file):
    bot = Bot()
    bot.login(username = "jabbling2020",
              password = "galojabbling04")
    bot.upload_photo(file)

def obtain_images():
    for number in range(1,20):
        url1=f'https://nairobiwire.com/wp-content/uploads/2021/09/trend{number}-15.jpg'
        
        with app.app_context():
            cursor=mydb.connection.cursor()
            cursor.execute('SELECT * FROM IMAGES WHERE URL="'+url1+'"')
            fff=cursor.fetchall()
            for ffx in fff:
                pass
            print(fff)
            try:
                if url1 in ffx:
                    print('the url already exists')
                else:
                    url=str(url1)
                    number=str(number)
                    cursor=mydb.connection.cursor()
                    cursor.execute('INSERT INTO IMAGES(URL)VALUES(%s)',(url,))
                    mydb.connection.commit()
                    print('Successfully uploaded to database')
                    r = requests.get(url, allow_redirects=True)
                    global file
                    file=random.randint(1,100000000000)
                    file='images/'+str(file)+'.png'
                    open(file, 'wb').write(r.content)
                    post_to_gram(file)
            except:
                url=str(url1)
                number=str(number)
                cursor=mydb.connection.cursor()
                cursor.execute('INSERT INTO IMAGES(URL)VALUES(%s)',(url,))
                mydb.connection.commit()
                print('Successfully uploaded to database')
                r = requests.get(url, allow_redirects=True)
                file=random.randint(1,100000000000)
                file='images/'+str(file)+'.png'
                open(file, 'wb').write(r.content)
                post_to_gram(file)
            
            
#make the bot post to gram
#make the bot swap through the urls of kenya memes
#make the bot Post regularly

obtain_images()

