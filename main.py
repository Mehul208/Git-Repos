from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://meet.google.com/")
driver.implicitly_wait(4)
meet_code = "gwh-yaxb-nka"

try:
    meet_code_input = driver.find_elements_by_css_selector('input.glue-caption')[1]
    meet_code_input.send_keys(meet_code)
    button = driver.find_element_by_css_selector('button.join-button')
    button.click()

except NoSuchElementException:
    print("Not Found")

# driver.close()
