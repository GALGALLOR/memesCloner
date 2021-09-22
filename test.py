import requests
from bs4 import BeautifulSoup
import json
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





#from instabot import Bot
#bot = Bot()
#bot.login(username = "jabbling2020",
#          password = "galojabbling04")


def obtain_images():
    url='https://www.football365.com/'
    url2='https://www.dailymail.co.uk/sport/football/index.html'
    url3='https://sportslens.com/tags/competitions/english-premier-league/'
    url4='https://www.sportsmole.co.uk/'
    url5='http://inbedwithmaradona.com/'
    url6='https://www.diariogol.com/'
    url7='https://www.instagram.com/433'
    HEADERS = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
    response = requests.get(url7)
    soup=BeautifulSoup(response.text,'html.parser')
    
    #h2 = soup.find_all('h2')
    images=soup.find_all('img')
    #global list_of_captions
    #list_of_captions=[]
    global list_of_images
    list_of_images=[]
    

    
    for image in images:
        image=image['src']
        print(image)
        list_of_images.append(image)

    
    

    '''for words in images:
        words=words['alt']
        print(words)
        title=str(words)['title']
        #words=str(words)
        #words=words.split('>')
        #words=words[2]
        #words=str(words)
        #words=words.split('<')
        #words=words[0]
        list_of_captions.append(words)'''
    
    

    


def download_image2(images):
    url =images
    url=str(url)
    r = requests.get(url, allow_redirects=True)
    global file
    file=random.randint(1,100000000000)
    file=str(file)+'.png'
    open(file, 'wb').write(r.content)





def dailymail_download_image(list_of_images,list_of_captions):
    captionx=0
    ldnf=0
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
                   bot.upload_photo(file,caption)
                  
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




def get_instagram_caption(username):
   # Create an instaloader object with parameters
    L = instaloader.Instaloader(download_pictures = False, download_videos = False, download_comments= False, compress_json = False)
   
    # Log in with the instaloader object
    L.login("jabbling2020" , "galojabbling04")
    # Search the instagram profile
    profile = instaloader.Profile.from_username(L.context, username)
    print('success')
    # Scrape the posts
    posts = profile.get_posts()
    duration=0
    for post in posts: 
        duration=duration+1
        L.download_post(post, target = profile.username)
        time=str(post.date)
        time=time.replace(' ','_')
        time=time.replace(':','-')
        time='433/'+time+'_UTC.txt'
        f = open(time, "r",encoding='utf8')
        caption=f.read()
        global list_of_captions
        list_of_captions=[]
        list_of_captions.append(caption)
        
        if duration==5:
            break

def instagram_download_image(list_of_images,list_of_captions):
    captionx=0
    ldnf=0
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
                   bot.upload_photo(file,caption)
                  
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
        
def obtain_images_instagram():
    url='https://knowyourmeme.com/'
    HEADERS = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
    response = requests.get(url)
    soup=BeautifulSoup(response.text,'html.parser')
    images=soup.find_all('img')
    global list_of_images
    list_of_images=[] 

    for image in images:
        image=image['src']
        print(image)
        list_of_images.append(image)
    



obtain_images_instagram()
#print(list_of_images)
#get_instagram_caption('433')
#print(list_of_captions)



