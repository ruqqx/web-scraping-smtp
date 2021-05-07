from bs4 import BeautifulSoup
import requests
import time
import datetime
import smtplib
import os

url = "https://www.trendyol.com/turbox/atm9917762-i5-650-turbo-3-46ghz-8gb-ram-240gb-ssd-ofis-bilgisayari-p-37357492"
shorturl = "https://bit.ly/3urU4To"

def pricee():
    try:
        html = requests.get(url).content
        soup = BeautifulSoup(html, "html.parser")
        text = soup.find("h1", {"class":"pr-new-br"}).get_text().strip()
        price = soup.find("span", {"class":"prc-slg"}).get_text().replace(".","")

        x = text[0:31]
        y = float(price[0:5])
        s = f"Name: {x}\nPrice: {y}"
        print(s)
        if y < 1639:
            smtp(x,y)
        else:
            print("it has not fallen yet")
    except:
            print("Error")
            exit()
def smtp(x,y):
    try:
        mail = smtplib.SMTP("smtp.gmail.com",587)
        mail.ehlo()
        mail.starttls()
        sender = "loginmail@gmail.com"
        to = "tomail@gmail.com"
        mail.login(sender,"pass?")
        
        subject = x + "" + "The Price You Want Has Been Dropped!"
        body = f"Last Price: {y}, You can check it from this link => " + (shorturl)
        content = f"Subject:{subject}\n\n{body}"
        mail.sendmail(sender,to,content.encode("utf-8"))
        print("Mail sent")

    except smtplib.SMTPException as e:
        print(e)
    finally:
        mail.quit()

while True:
    pricee()
    time.sleep(60*60)
    