from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

safari = webdriver.Safari()
safari.get("http://www.python.org")
try:
    safari.implicitly_wait(3)
    # elem = safari.find_element_by_name('q')
    # elem.clear()
    # elem.send_keys('pycon')
    # elem.send_keys(Keys.RETURN)
    # # alert = safari.switch_to.alert
    # sleep(10)
    # safari.back()
    elem = safari.find_element_by_id('about')
    all_elem = elem.find_elements_by_tag_name('li')
    # print(all_elem)
    for option in all_elem:
        print(option.get_attribute('value'))


except Exception as ex:
    print(ex)
finally:
    safari.close()