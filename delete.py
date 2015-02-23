from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


driver = webdriver.Firefox()
content = driver.get("https://webmail.daiict.ac.in/zimbra/")
usname = driver.find_element_by_id('username')
usname.send_keys('201201111')
password = driver.find_element_by_id('password')
password.send_keys('twinparadox')
password.send_keys(Keys.RETURN)

delay = 3
wait = WebDriverWait(driver, delay)
element = wait.until(EC.element_to_be_clickable((By.ID,'OPCHALL')))

#elements = driver.find_elements_by_xpath('//*[@id]')
checkbox = driver.find_element_by_id('OPCHALL')
checkbox.click()
delete = driver.find_element_by_id('SOPDELETE')
delete.click()
