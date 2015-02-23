from bs4 import BeautifulSoup as bss
from mechanize import Browser
import requests
import re
import html2text

url = "webmail.daiict.ac.in"
master = 'https://webmail.daiict.ac.in/'
r  = requests.get(master)
br = Browser()
br.set_handle_robots(False)
br.open("https://webmail.daiict.ac.in/zimbra/")
br.select_form(name='loginForm')
br.form['username'] = '201201111'
br.form['password'] = 'twinparadox'
br.submit()

response = br.response().read()
pool = bss(response)
links = []
messages = pool.find_all('tbody', {'id':'mess_list_tbody'})[0]
messages = messages.findAll('a',href=True)
print len(messages)
prev = 'https://webmail.daiict.ac.in/zimbra/h/search?si=1&so=0&sc=4986&st=message&id='
next = '&xim=1&action=paneView'

for message in messages:
        #print message
        something, id_ = re.findall('id=(.*?)&', str(message))  
        opened = br.open(prev+id_+next)
        response = br.response().read()
        response = bss(response)
        """X = re.findall('doc.write(.*?)doc.close', str(response), re.DOTALL)
        if len(X):
                X = X[0]
                #print X
                X = X[1:-5]
                html_ = ('u'+X).decode('utf-8')
                save = html2text.html2text(html_)
                print save
        """
        forward = response.findAll('a', {'id':'OPFORW'})
        if len(forward):
                forward = forward[0]
                link = forward['href']
                #print link
                br.open(link)
                #print br.response().read()
                br.select_form(name='composeForm')
                #print br.form
                br.form['to'] = 'kaushik.varanasi1@gmail.com'
                print br.form 
                br.submit()
                print "done"
