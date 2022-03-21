from account import sender_email, password
from bs4 import BeautifulSoup
import pprint
import requests
import smtplib, ssl

#Step 1:
#Get headline from CNBC.com
cnbc = 'https://www.cnbc.com/'
response = requests.get(cnbc)
soup = BeautifulSoup(response.text, "html.parser")

h2 = soup.find("h2")
pprint.pprint(h2)

#Step 2:
#Send email using Simple Mail Transfer Protocol (SMTP)
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
receiver_email = "nisbetda@miamioh.edu"

#The email content
subject = 'CNBC'
body = h2.get_text()
msg = f'Subject: {subject}\n\n{body}'

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg)

#Step 3:
#Automatically send every morning

#Bugs: email wouldn't send because there is a security setting on gmail to allow outside apps to login

#followed a youtube tutorial on web scrapping to get soccer standings
#applied the same techniques to CNBC, something more useful and interesting to myself

#followed a different tutorial on sending emails using smtplib

#/Users/daltonnisbett/Documents/CODE/DSA/newsletter.py