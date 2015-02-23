GMAIL_ID = 'kaushik.varanasi1@gmail.com'
WEBMAIL_ID = '201201111'
WEBMAIL_PASS = 'twinparadox'


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


driver = webdriver.Firefox()
content = driver.get("https://webmail.daiict.ac.in/zimbra/")
usname = driver.find_element_by_id('username')
usname.send_keys(WEBMAIL_ID)
password = driver.find_element_by_id('password')
password.send_keys(WEBMAIL_PASS)
password.send_keys(Keys.RETURN)


from bs4 import BeautifulSoup as bss
from mechanize import Browser
import requests
import re

url = "webmail.daiict.ac.in"
master = 'https://webmail.daiict.ac.in/'
r  = requests.get(master)
br = Browser()
br.set_handle_robots(False)
br.open("https://webmail.daiict.ac.in/zimbra/")
br.select_form(name='loginForm')
br.form['username'] = WEBMAIL_ID
br.form['password'] = WEBMAIL_PASS
br.submit()

response = br.response().read()
pool = bss(response)
messages = pool.find_all('tbody', {'id':'mess_list_tbody'})[0]
messages = messages.findAll('a',href=True)
queue = []

for message in messages:
        ID = message['id']
        queue.append(ID)



delay = 3
wait = WebDriverWait(driver, delay)

for each in queue:
        message = wait.until(EC.element_to_be_clickable((By.ID, each)))
        message.click()
        forward = wait.until(EC.element_to_be_clickable((By.ID,'OPFORW')))
        forward.click()
        toaddr = wait.until(EC.element_to_be_clickable((By.ID,'toField')))
        toaddr.send_keys(GMAIL_ID)
        sendbutton = wait.until(EC.element_to_be_clickable((By.ID,'SOPSEND')))
        sendbutton.click()
        mailbutton = wait.until(EC.element_to_be_clickable((By.ID,'TAB_MAIL')))
        mailbutton.click()
