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


'''from PIL import Image  
def resize(image):
    im = Image.open(image)  
    newsize = (1080, 1080) 
    im1 = im.resize(newsize) 
    im1.save(image)
'''
bot = Bot()
time.sleep(5)
bot.login(username = "jabbling2020",
              password = "galojabbling04")

def post_to_gram(file):
    bot.upload_photo(file,caption='#kenyantrendingmemes #kenyantrendingimages ')




def obtain_images(url):
    with app.app_context():
        cursor=mydb.connection.cursor()
        cursor.execute('SELECT * FROM IMAGES WHERE URL="'+url+'"')
        fff=cursor.fetchall()
        for ffx in fff:
            pass
        print(fff)
        try:
            if url in ffx:
                print('the url already exists')
            else:
                url=str(url)

                r = requests.get(url, allow_redirects=True)
                global file
                file=random.randint(1,100000000000)
                file='images/'+str(file)+'.png'
                open(file, 'wb').write(r.content)
                cursor=mydb.connection.cursor()
                cursor.execute('INSERT INTO IMAGES(URL)VALUES(%s)',(url,))
                mydb.connection.commit()
                print('Successfully uploaded to database')
                post_to_gram(file)
        except:
            try:
                url=str(url)

                print('Successfully uploaded to database')
                r = requests.get(url, allow_redirects=True)
                file=random.randint(1,100000000000)
                file='images/'+str(file)+'.png'
                open(file, 'wb').write(r.content)
                
                cursor=mydb.connection.cursor()
                cursor.execute('INSERT INTO IMAGES(URL)VALUES(%s)',(url,))
                mydb.connection.commit()
                post_to_gram(file)
            except:
                print('unknown error occurred with the bot')
                try:
                    la=random.randint(1,1000000)
                    os.rename('config',la)
                    print('trying again')
                    obtain_images(url)
                except:
                    print('could not find the error')

            
#make the bot post to gram
#make the bot swap through the urls of kenya memes
#make the bot Post regularly

url1='https://nairobiwire.com/wp-content/uploads/2021/09/trend{}-15.jpg'
url2='https://nairobiwire.com/wp-content/uploads/2021/10/p{}.jpg'
url3='https://nairobiwire.com/wp-content/uploads/2021/09/trend{}-13.jpg'
list_of_urls=[url1,url2,url3]
for number in range(1,20):
    urlx=url1.format(number)
    urly=url2.format(number)
    urlz=url3.format(number)
    obtain_images(urlx)
    obtain_images(urly)
    obtain_images(urlz)

print('Done Posting')

#https://nairobiwire.com/humour