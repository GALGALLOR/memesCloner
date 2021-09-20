import requests
from bs4 import BeautifulSoup
import json
from flask import Flask,request,render_template,redirect
import time
import re
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #for pressing keys on the keyboard in chrome
names='jabbling2020'
passy='galojabbling04'

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
        post=driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/div/button')
        post.send_keys(Keys.ENTER)
        print("success")
    except:
        print('Could not find the post button')


def obtain_images():
    url='https://www.football365.com/'
    url2='https://www.dailymail.co.uk/sport/football/index.html'
    HEADERS = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
    response = requests.get(url2)
    soup=BeautifulSoup(response.text,'html.parser')
    global h3
    h3 = soup.find_all('h3')
    global images
    images=soup.find_all('img')
    """global list_of_captions
    list_of_captions=[]"""
    global list_of_images
    list_of_images=[]
    """
    global words
    global captions
    for captions in list_of_captions:
    pass
    for words in h3:
        words=words['title']
        list_of_captions.append(words)"""
    global image
    for image in images:
        image=image['src']
        list_of_images.append(image)
    

    global dps
    for dps in list_of_images:
        pass

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

obtain_images()
ldnf=0
for image in list_of_images:
    try:
        ldnf=ldnf+1
        print('image ',ldnf)
        print(image)
        download_image(image)
        
    except:
        print('testing the alternative')
        pass
#post_to_gram(names,passy)
#@app.route('/')
#def home():
#    return render_template('text.html',images=list_of_images,captions=list_of_captions)


if __name__=='__main__':
    app.debug=True
    app.run()