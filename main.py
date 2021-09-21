import requests
from bs4 import BeautifulSoup
import json
from instabot import Bot
from flask import Flask,request,render_template,redirect
import time
import re
import random
import pyautogui
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #for pressing keys on the keyboard in chrome
names='its.galo_2'
passy='KCD831J'

app=Flask(__name__)
PATH ="C:/Users/LENOVO/Downloads/chromedriver.exe"
driver = webdriver.Chrome(PATH)



def post_to_gram(names,passy):

    driver.get('https://www.instagram.com/accounts/login/')
    time.sleep(5)
    username=driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
    username.send_keys(names)
    password=driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
    password.send_keys(passy)
    time.sleep(2)
    password.send_keys(Keys.ENTER)
    time.sleep(10)
    not_now=driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
    not_now.send_keys(Keys.ENTER)
    print('Im in!')
    time.sleep(10)
    try:
        time.sleep(5)
        not_now2=driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
        print('found the Not now button')
        not_now2.send_keys(Keys.ENTER)
        time.sleep(5)
    except:
        print('couldnt find the not now 2 button')
    try:
        post=driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/div/button')
        post.send_keys(Keys.ENTER)
        print("found the Post Button")
    except:
        print('Could not find the post button')
    
    select_from_computer=driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div[2]/div[2]/div[2]/div/button')
    print('found the Choose an image button')
    select_from_computer.send_keys(Keys.ENTER)
    print('Choose an image')


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

def download_image(image):
    fifi='//*[@id="app"]/div/div[1]/div[2]/input'
    url='https://imgdownloader.com/'
    driver.get(url)
    time.sleep(10)
    input=driver.find_element_by_xpath(fifi)
    input.send_keys(image)
    search=driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div/button')
    search.send_keys(Keys.ENTER)
    time.sleep(60)
    print('downloading image')
    download=driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div/div/button')
    download.send_keys(Keys.ENTER)
    time.sleep(60)
    print('download complete')



def execute_download_image():
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
            elif 'facebook' in image:
                print('cannot download logos... passing')
            else:
                print('Proper image found')
                download_image2(image)
                print('successfully downloaded')
                time.sleep(5)
                post_to_gram_2(file)
                
            
        except:
            print('testing the alternative')
            pass


def scan_area():
    for n in range(1,1000):
        time.sleep(1)
        print(pyautogui.position())
def post_to_gram_2(file):
    print('posting to gram')
    post_to_gram(names,passy)

    #maximize=(982,24)
    #pyautogui.click(maximize)


 
 
bot = Bot()
 
bot.login(username = "user_name",
          password = "user_password")
 
# Recommended to put the photo
# you want to upload in the same
# directory where this Python code
# is located else you will have
# to provide full path for the photo
bot.upload_photo("",
                 caption ="Techn"


#post_to_gram_2()


#obtain_images()
#execute_download_image()

#post_to_gram(names,passy)
#@app.route('/')
#def home():
#    return render_template('text.html',images=list_of_images,captions=list_of_captions)


#if __name__=='__main__':
#    app.debug=True
#    app.run()