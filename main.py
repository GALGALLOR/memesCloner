from instabot import Bot
import time

file='85154871870.png'
bot = Bot()
time.sleep(5)
bot.login(username = "jabbling2020",
          password = "galojabbling04")
time.sleep(5)
bot.upload_photo(file,caption='#kenyanmemes')
time.sleep(5)