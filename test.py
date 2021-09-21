import requests
from bs4 import BeautifulSoup
import json
from instabot import Bot
from flask import Flask,request,render_template,redirect
import time
import os
import re
import random
import pyautogui
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #for pressing keys on the keyboard in chrome




bot = Bot()
 
bot.login(username = "jabbling2020",
          password = "galojabbling04")


def obtain_images():
    url='https://www.football365.com/'
    url2='https://www.dailymail.co.uk/sport/football/index.html'
    HEADERS = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
    response = requests.get(url2)
    soup=BeautifulSoup(response.text,'html.parser')
    global h3
    h3 = soup.find_all('p')
    global images
    images=soup.find_all('img')
    global list_of_captions
    list_of_captions=[]
    global list_of_images
    list_of_images=[]
    
    global words
    global captions
    for captions in list_of_captions:
        pass
    for words in h3:
        words=str(words)
        words=words.replace('<p>','')
        words=words.replace('</p>','')
        print(words)
        #words=words['title']
        list_of_captions.append(words)
    global image
    for image in images:
        image=image['src']
        list_of_images.append(image)
    

    global dps
    for dps in list_of_images:
        pass


def download_image2(images):
    url =images
    url=str(url)
    r = requests.get(url, allow_redirects=True)
    global file
    file=random.randint(1,100000000000)
    file=str(file)+'.png'
    open(file, 'wb').write(r.content)





def execute_download_image():
    ldnf=0
    xlf=0
    for image in list_of_images:
        try:
           ldnf=ldnf+1
           
           print('image ',ldnf)
           print(image)
           if 'gif' in image:
               print('cannot work on a gif image')
           elif 'us' in image:
               print('error found...passing')
           elif 'i.dailymail.co.uk/i/pix' in image:
               print('Possible logo found')
           elif 'facebook' in image:
               print('cannot download logos... passing')
           else:
               print('Proper image found')
               download_image2(image)
               print('successfully downloaded')
               time.sleep(5)
               try:
                   bot.upload_photo(file,caption =list_of_captions[xlf])
                  
                   print('caption number:',xlf)
                   xlf=xlf+1
                   print('successfully posted')
                   time.sleep(10)
                   os.remove(file)
                   print(file)
               except:
                   xlf=xlf+1
                   print(file)
                   os.remove(file)
                   print('Could not post the image')
                   time.sleep(2)
                   
                   print('deleteing the Image')
        except:
            print('testing the alternative')
            pass





obtain_images()
execute_download_image()
