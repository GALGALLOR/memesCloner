from instabot import Bot
 
 
bot = Bot()
 
bot.login(username = "its.galo_2",
          password = "KCD831J")
 
# Recommended to put the photo
# you want to upload in the same
# directory where this Python code
# is located else you will have
# to provide full path for the photo
bot.upload_photo("74433125934.png",
                 caption ="Technical Scripter Event 2019")