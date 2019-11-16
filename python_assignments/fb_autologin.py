from selenium import webdriver
from time import sleep

usr_name = input('Enter your facebook username: ')
password = input('Enter you password: ')

web_driver = webdriver.Safari()
try:
    # makes the browser wait if it can't find an element
    web_driver.implicitly_wait(5)
    web_driver.get("http://www.facebook.org")
    sleep(1)
    username_col = web_driver.find_element_by_id('email')
    username_col.send_keys(usr_name)
    sleep(1)

    password_col = web_driver.find_element_by_id('pass')
    password_col.send_keys(password)

    login_col = web_driver.find_element_by_id('loginbutton')
    login_col.click()

    input('You have successfully logged on to facebook. Press any key, to close the session')
finally:
    web_driver.quit()
    print("Completing facebook login session!!")
