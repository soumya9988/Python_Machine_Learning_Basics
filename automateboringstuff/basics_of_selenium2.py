from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

web_driver = webdriver.Safari()
web_driver.get('http://nostarch.com')
try:
    web_driver.implicitly_wait(5)
    html_elem = web_driver.find_element_by_tag_name('html')
    html_elem.send_keys(Keys.END)
    sleep(5)
    html_elem.send_keys(Keys.HOME)
    sleep(5)
    web_driver.refresh()
except:
    print('Error while opening Safari...')
finally:
    web_driver.close()
