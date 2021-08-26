import requests
from bs4 import BeautifulSoup
import json
import re
import requests

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


