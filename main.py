import requests
import pandas as pd
from bs4 import BeautifulSoup as soup
import sendgrid
from sendgrid.helpers.mail import *


def createSendStr(name,to_send):
    sendStr = "Hi " + name + ",\n\n Unread notices:\n"
    for i,notice in enumerate(to_send):
        sendStr += str(i+1) + ") "
        sendStr += "\n"+"Heading: "+to_send[i]['heading'] + " \n"

        sendStr += "\n"+"Link: "+to_send[i]['link'] + " \n"

        sendStr += "\n"+"date: " + to_send[i]['date'] + " \n"
        
    return sendStr

def sendEmail(attenders,to_send):
    for i,row in attenders.iterrows():
        sendStr = createSendStr(row['Name'],to_send)
        sg = sendgrid.SendGridAPIClient(apikey=api_key)
        from_email = Email("kritikab2100@gmail.com")
        to_email = Email(row["Email"])
        subject = "NSUT IMS Notice update"
        content = Content("text/plain", sendStr)
        mail = Mail(from_email, subject, to_email, content)
        response = sg.client.mail.send.post(request_body=mail.get())        
        
with open('apikey.txt','r') as f:
    api_key = f.read()

resp =  requests.get(r'https://imsnsit.org/imsnsit/notifications.php')
resp_soup = soup(resp.content,'lxml')


df = pd.DataFrame(columns =["heading","date","link"])
trs = resp_soup.findAll('tr')
l = len(trs)
j=0

for i in range(3,l,2):
    tds = trs[i].findAll('td')
    if not len(tds) == 2:
        continue    
    date=tds[0].text.strip()
    heading = tds[1].text.strip()
    href=tds[1].a['href'].strip()
    df.loc[j]=[heading,date,href]
    j+=1

db = pd.read_csv('database.csv',usecols=['heading','date','link'])
headset = set(db['heading'])

to_send = []
for i,row in df.iterrows():
    
    if not row['heading'] in headset:
        l = len(db)
        db.loc[l] = row
        to_send.append(row)    
    
db.to_csv('database.csv')   
att = pd.read_excel('attenders.xlsx')

if len(to_send) > 0:
    sendEmail(att,to_send)