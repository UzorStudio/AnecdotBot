import anecdorrider
import telebot
from time import sleep

bot = telebot.TeleBot('1945439245:AAG7UfIqmfdZDQALLtiyf9fntaFaL6lD1oo')

def SendVideo():
    anekdot = anecdorrider.getAnekdot()

    text = f"\n{anekdot['anekdot']}"
    #bot.send_media_group(-1001650547543,[InputMediaVideo(f,caption="https://t.me/ToKTokVideos")])
    bot.send_message(-1001248431165,text)


while True:
    SendVideo()
    sleep(9000)
    #sleep(10)
