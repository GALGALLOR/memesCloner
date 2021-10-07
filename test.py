
'''from instabot import Bot
import os
from xxxl import remove_config
remove_config()
bot=Bot()
bot.login(username='jabbling2020',password='galojabbling04')
images='images/'
for image in os.listdir(images):
    bot.upload_photo(images+image,caption='testing')

'''
#Startoff next time by deleting the pycache and config files
#resize the images
#the bot still downloads images that are in the database---done



def resize(path):
    from PIL import Image
    image = Image.open(path)
    image = image.resize((1080,1080),Image.ANTIALIAS)
    import os
    os.remove(path)
    image.save(fp=path)

path='images/41671.png'
resize(path)