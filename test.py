
from instabot import Bot

bot=Bot()
bot.login(username='',password='')

followers=bot.get_user_followers('nairobi_gosip_club')
for follower in followers:
    print(bot.get_user_info(follower))


