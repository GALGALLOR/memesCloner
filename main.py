import requests
from bs4 import BeautifulSoup
import json
import time
import re
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #for pressing keys on the keyboard in chrome
names='jabbling2020'
passy='galojabbling04'

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
post_to_gram(names,passy)

def obtain_images():
    url='https://www.goal.com/en?ICID=HP'
    HEADERS = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
    response = requests.get(url)
    soup=BeautifulSoup(response.text,'html.parser')

    h3 = soup.find_all('h3')
    images=soup.find_all('img')
    list_of_captions=[]
    list_of_images=[]
    for words in h3:
        words=words['title']
        list_of_captions.append(words)

    for image in images:
        image=image['src']
        list_of_images.append(image)

    for captions in list_of_captions:
        print(captions)
    for dps in list_of_images:
        print(dps)


