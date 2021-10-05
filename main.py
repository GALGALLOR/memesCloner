from flask import Flask
from flask import redirect,render_template,request,url_for
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


bot = Bot()
bot.login(username = "jabbling2020",
              password = "galojabbling04")
def post_to_gram(file,url):
    bot.upload_photo(file,caption='#kenyantrendingmemes #kenyantrendingimages '+url)







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

                post_to_gram(file,url)
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

                post_to_gram(file,url)
            except:
                print('unknown error occurred with the bot')
                try:
                    la=random.randint(1,1000000)
                    os.rename('config',la)
                    print('trying again')
                    obtain_images(url)
                except:
                    print('could not find the error')

list_of_dtp=[]

@app.route('/',methods=['POST','GET'])
def home():
    if request.method =='POST':
        url=str(request.form['url'])
        try:
            clear=str(request.form['clear'])
            if clear=='yes':
                print('clear command detected')
                list_of_dtp.clear()
        except:
            print('clear command undetected')
        if len(url)>5:
            list_of_dtp.append(url)
        else:
            print('url shorter than 5 characters')
            pass


        print(list_of_dtp)
        return redirect(url_for('home'))
    else:
        return render_template('text.html',list_of_dtp=list_of_dtp)

if __name__ == '__main__':
    app.run()
