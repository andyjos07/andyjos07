from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

song = 'dhoni'

driver = webdriver.Chrome ('C:\Program Files\chromedriver_win32\chromedriver.exe')
driver.get ('https://www.youtube.com/')

search_field=driver.find_element_by_name('search_query')
print(search_field.is_displayed())
search_field.send_keys(song)
time.sleep(3)
search_field.send_keys(Keys.ENTER)

time.sleep(5)

vid=driver.find_element_by_xpath('//*[@id="thumbnail"]')
print(vid.is_displayed())







