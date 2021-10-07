from flask import Flask
import mysql
from os import listdir
import os
from os.path import isfile, join
from bs4 import BeautifulSoup
from instabot import Bot
import time
import random
import requests
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





def insert_domain(domain,list):
    if domain in list:
        print('domain in list')
    else:
        with app.app_context():
            cursor=mydb.connection.cursor()
            cursor.execute('INSERT INTO DOMAINS(URL)VALUES(%s)',(domain,))
            mydb.connection.commit()
        list.append(domain)

def remove_config():
    try:
        mypath='config'
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        for files in onlyfiles:
            os.remove(mypath+'/'+files)

        try:
            pycache='__pycache__'
            onlyfiles = [f for f in listdir(pycache) if isfile(join(pycache, f))]
            for file in onlyfiles:
                os.remove(pycache+'/'+file)
        except:
            pass

        logfile='config/log'
        onlyfiles = [f for f in listdir(logfile) if isfile(join(logfile, f))]
        for files in onlyfiles:
            os.remove(logfile+'/'+files)

        os.rmdir('config/log')
        os.rmdir(mypath)
    except:
        print('directories not found')

def post_to_gram(file):
    bot = Bot()
    bot.login(username = "its.galo_2",
          password = "KCD831J")
    bot.upload_photo(file,caption='#kenyantrendingmemes #kenyantrendingimages ')
    remove_config()


def obtain_images(url1):
    with app.app_context():
        cursor=mydb.connection.cursor()
        cursor.execute('SELECT * FROM IMAGES WHERE URL="'+url1+'"')
        fff=cursor.fetchall()
        
        try:
            foru=[]
            for ffx in fff:
                foru.append(ffx)
                
            print(fff)
            if url1 in foru:
                print('the url already exists')
            else:
                url=str(url1)
                r = requests.get(url, allow_redirects=True)
                file=random.randint(1,100000)
                file='images/'+str(file)+'.png'
                open(file, 'wb').write(r.content)
                cursor=mydb.connection.cursor()
                cursor.execute('INSERT INTO IMAGES(URL)VALUES(%s)',(url,))
                mydb.connection.commit()
                print('Successfully uploaded to database')
                
        except:
            
            url1=str(url1)
            
            r = requests.get(url1, allow_redirects=True)
            
            file=random.randint(1,100000)
            
            file='images/'+str(file)+'.png'
            
            open(file, 'wb').write(r.content)
            cursor=mydb.connection.cursor()
            cursor.execute('INSERT INTO IMAGES(URL)VALUES(%s)',(url1,))
            mydb.connection.commit()
            print('Successfully uploaded to database')
            




list_of_domains=[]
def fetch_from_list(list):
    with app.app_context():
        cursor=mydb.connection.cursor()
        cursor.execute('SELECT * FROM DOMAINS')
    domains=cursor.fetchall()
    for dormain in domains:
        for minidomain in dormain:
            if minidomain in list:
                pass
            else:
                list.append(minidomain)

def clear_database():
    with app.app_context():
        cursor=mydb.connection.cursor()
        cursor.execute('DELETE FROM DOMAINS')
        mydb.connection.commit()
        print('database cleared')
        list_of_domains.clear()
    

@app.route('/',methods=['POST','GET'])
def home():
    if request.method =='POST':
        fetch_from_list(list_of_domains)
        url=str(request.form['url'])
        try:
            clear=str(request.form['clear'])
            if clear=='yes':
                print('clear command detected')
                clear_database()
        except:
            pass
        
        try:
            activator=str(request.form['activator'])
            
            if activator=='activator':
                
                for domain in list_of_domains:
                    for number in range(1,20):
                        try:
                            print(domain)
                            url1=domain.format(number)
                            print(url1)
                            obtain_images(url1)
                            print('image',number)
                            print(url1,'xxxl')
                        except:
                            print('plan B')
                            remove_config()
        except:
            print('activator not found')

        if len(url)>5:
            
            insert_domain(url,list_of_domains)
        else:
            print('url shorter than 5 characters')
            pass


        print(list_of_domains)
        return redirect(url_for('home'))
    else:
        fetch_from_list(list_of_domains)
        return render_template('text.html',list_of_dtp=list_of_domains)

if __name__ == '__main__':
    app.run(debug=True)
