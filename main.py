from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("https://meet.google.com/")

time.sleep(10)
driver.close()
