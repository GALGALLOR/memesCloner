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




def post_to_gram(names,passy):
    PATH ="C:/Users/LENOVO/Downloads/chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get('https://www.instagram.com/accounts/login/')
    time.sleep(5)
    username=driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
    username.send_keys(names)
    password=driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
    password.send_keys(passy)
    time.sleep(2)
    password.send_keys(Keys.ENTER)
    time.sleep(10)
    not_now=driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
    not_now.send_keys(Keys.ENTER)
    print('Im in!')
    time.sleep(5)
    post=driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/div/button')
    post.send_keys(Keys.ENTER)
    print("success")


def obtain_images():
    url='https://www.goal.com/en?ICID=HP'
    HEADERS = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
    response = requests.get(url)
    soup=BeautifulSoup(response.text,'html.parser')
    global h3
    h3 = soup.find_all('h3')
    global images
    images=soup.find_all('img')
    global list_of_captions
    list_of_captions=[]
    global list_of_images
    list_of_images=[]
    global words
    for words in h3:
        words=words['title']
        list_of_captions.append(words)
    global image
    for image in images:
        image=image['src']
        list_of_images.append(image)
    global captions
    for captions in list_of_captions:
        pass
        global dps
    for dps in list_of_images:
        pass

obtain_images()
@app.route('/')
def home():
    return render_template('text.html',images=list_of_images,captions=list_of_captions)


if __name__=='__main__':
    app.debug=True
    app.run()