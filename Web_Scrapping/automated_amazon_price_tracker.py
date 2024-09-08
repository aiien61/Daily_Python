import os
import requests
import smtplib
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# in .env file
SMTP_ADDRESS: str = "smtp.gmail.com"
EMAIL_ADDRESS: str = "your_email@email.com"
EMAIL_PASSWORD: str = "your app password"

load_dotenv()

URL: str = "https://appbrewery.github.io/instant_pot/"

# Full headers
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
}

# A minimal header
# header = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
#     "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
# }

response = requests.get(URL, headers=header)
soup = BeautifulSoup(response.content, 'html.parser')
# print(soup.prettify())

price: str = soup.find(class_='a-offscreen').getText()

# remove currency sign
price_without_currency: str = price.split('$')[1]

# convert to floating number
price_as_float: float = float(price_without_currency)
print(price_as_float)

# ====================== Send an Email ===========================

# Get the product title
title: str = ''.join([s.strip() for s in soup.find(id="title").getText().split('\r\n')])
print(title)

buy_price: int = 100

if price_as_float < buy_price:
    message = f"{title} is on sale for {price}!"
    # ====================== Use environment variables ===========================
    with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
        connection.starttls()
        result = connection.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSWORD"])
        connection.sendmail(
            from_addr=os.environ["EMAIL_ADDRESS"],
            to_addrs=os.environ["EMAIL_ADDRESS"],
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )
