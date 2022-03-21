import pprint
import requests
from bs4 import BeautifulSoup
import smtplib, ssl

#Get headline from CNBC.com
cnbc = 'https://www.cnbc.com/'
response = requests.get(cnbc)
soup = BeautifulSoup(response.text, "html.parser")
print("HTML data is loading...")

h2 = soup.find("h2")
h8 = soup.find_all('td', class_="MarketTop-symbol")

pprint.pprint(h2)
pprint.pprint(h8)

#send email
sender_email = "daltonnisbett@gmail.com"
receiver_email = "nisbetda@miamioh.edu"
password = 'Hercules0810?'

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)