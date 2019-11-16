import time
from datetime import datetime as dt

hosts_temp = '/etc/hosts'
hosts_path = '/etc/hosts'
redirect = '127.0.0.1'
website_list = ['https://mobile.twitter.com', 'https://www.facebook.com']

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print('Working hours!!!!')
    else:
        print('Fun time')
