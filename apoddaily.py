import configparser
import telegram
import getapod
import numpy as np
from apscheduler.schedulers.blocking import BlockingScheduler

config = configparser.ConfigParser()
config.read('config.ini')

bot = telegram.Bot(token=(config['TELEGRAM']['ACCESS_TOKEN']))

url = 'https://apod.nasa.gov/apod/astropix.html'
url_zh = 'http://sprite.phys.ncku.edu.tw/astrolab/mirrors/apod/apod.html'

def job():
    id = np.loadtxt('id.txt')
    id = np.unique(id)
    pic = getapod.get_pic(url)
    exp = getapod.get_exp(url_zh,'zh')
    for w in id:
        bot.send_message(chat_id=w, text = pic)
        bot.send_message(chat_id=w, text= exp , parse_mode='Markdown')
        
    
scheduler = BlockingScheduler()
scheduler.add_job(job,'cron', day_of_week='0-6', hour=9, minute=59)
scheduler.start()
