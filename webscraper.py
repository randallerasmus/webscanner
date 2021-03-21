import requests
from bs4 import BeautifulSoup
import smtplib
import time

# https://www.youtube.com/watch?v=Bg9r_yLk7VY&ab_channel=DevEd
# Video explaining the steps in the tutorial

URL = 'https://www.sharedata.co.za/v2/Scripts/Summary.aspx?c=SOL'

headers = {"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}

def check_sasol_stock():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    sasolPrice = soup.find(id="LatestMarketData_LblPrevClose").get_text()
    converted_price = float(sasolPrice[0:7])

    if(converted_price < 200):
        send_mail()

    print(converted_price)
    print(sasolPrice.strip())

    if(converted_price < 200):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    # this encrypts our password
    server.starttls()
    server.ehlo()

    server.login('randallerasmus1@gmail.com', 'udvqvefcmkhiyxdd')

    subject = 'Your Sasol Stock fell down'
    body = 'Check your Sasol Share price link https://www.moneyweb.co.za/tools-and-data/click-a-company/SOL/'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'randallerasmus1@gmail.com',
        'randallerasmus1@gmail.com',
        msg
    )
    print('HEY EMAIL HAS BEEN SENT')

    server.quit()

while(True):
    check_sasol_stock()
    time.sleep(3600*23)
