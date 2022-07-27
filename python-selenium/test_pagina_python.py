from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from utils import *


driver = webdriver.Chrome()
driver.get('https://www.python.org')
assert "Python" in driver.title
elemento = driver.find_element(by=By.NAME, value='q')
elemento.clear()
elemento.send_keys("pycon")
elemento.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
