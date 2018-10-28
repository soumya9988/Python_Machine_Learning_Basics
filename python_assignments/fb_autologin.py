from selenium import webdriver
from selenium.webdriver.remote.command import Command
from time import sleep
usr_name = input('Enter your facebook username: ')
password = input('Enter you password: ')

driver = webdriver.Safari()
try:
    # makes the browser wait if it can't find an element
    driver.implicitly_wait(5)
    driver.get("http://www.facebook.org")
    sleep(1)
    username_box = driver.find_element_by_id('email')
    username_box.send_keys(usr_name)
    sleep(1)

    password_box = driver.find_element_by_id('pass')
    password_box.send_keys(password)

    login_box = driver.find_element_by_id('loginbutton')
    login_box.click()

    input('You have successfully logged on to facebook. Press any key, to close the session')
finally:
    driver.quit()
    print("Completing facebook login session!!")
