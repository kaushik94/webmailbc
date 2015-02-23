from bs4 import BeautifulSoup as bss
from mechanize import Browser
import requests
import re

GMAIL_ID = 'gmail id'
WEBMAIL_ID = 'college id'
WEBMAIL_PASS = 'webmail password'

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
links = []
messages = pool.find_all('tbody', {'id':'mess_list_tbody'})[0]
messages = messages.findAll('a',href=True)
prev = 'https://webmail.daiict.ac.in/zimbra/h/search?si=1&so=0&sc=4986&st=message&id='
next = '&xim=1&action=paneView'


for message in messages:
        something, id_ = re.findall('id=(.*?)&', str(message))
        message_link = prev+id_+next  
        opened = br.open(message_link)
        response = br.response().read()
        response = bss(response)
        forward = response.findAll('a', {'id':'OPFORW'})
        if len(forward):
                forward = forward[0]
                link = forward['href']
                br.open(link)
                #print cr.response().read()
                br.select_form(name='composeForm')
                #print cr.form
                br.form['to'] = GMAIL_ID
                #print cr.form 
                br.submit()
                print "done", id_
