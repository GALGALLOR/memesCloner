import requests
from bs4 import BeautifulSoup
import json
from flask import Flask,request,render_template,redirect
import time
import re
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #for pressing keys on the keyboard in chrome


'''url='https://www.goal.com/en?ICID=HP'
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
    pass'''

url1='https://www.football365.com/'
url2='https://www.dailymail.co.uk/sport/football/index.html'
response=requests.get(url1)
soup=BeautifulSoup(response.text,'html.parser')
h3=soup.find_all('h3')
print(h3)