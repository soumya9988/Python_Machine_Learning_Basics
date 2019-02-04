from selenium import webdriver
import time

v_email = input('Please enter your facebook username/email...')
v_password = input('Please enter your FB password...')

browser = webdriver.Safari()
browser.get('https://www.facebook.com')

try:

    browser.implicitly_wait(2)
    email_details = browser.find_element_by_name('email')
    print(email_details.tag_name)
    email_details.send_keys(v_email)

    pass_word_det = browser.find_element_by_name('pass')
    pass_word_det.send_keys(v_password)

    log_in_det = browser.find_element_by_id('loginbutton')
    log_in_det.click()
    time.sleep(10)

except Exception as exc:
    print('Error while opening facebook.. %s' % exc)

finally:
    browser.close()