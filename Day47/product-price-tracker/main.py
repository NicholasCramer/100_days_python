from bs4 import BeautifulSoup
import requests
import smtplib
from credentials import USERNAME, APP_PASSWORD

PRODUCT_URL = "https://www.amazon.com/Instant-Pot-Plus-Programmable-Sterilizer/dp/B075CYMYK6"
header = {
    "accept-language":
        "en-US,en;q=0.9",
    "accept-encoding":
        "gzip, deflate, br",
    "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "accept":
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
        "application/signed-exchange;v=b3;q=0.7",
}

response = requests.get(url=PRODUCT_URL, headers=header).text

soup = BeautifulSoup(response, "lxml")
# print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)

# Send email when price is below configured threshold
title = soup.find(id="productTitle").get_text().strip()

BUY_PRICE = 100

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("outlook.office365.com") as connection:
        connection.starttls()
        connection.login(user=USERNAME, password=APP_PASSWORD)
        connection.sendmail(
            from_addr=USERNAME,
            to_addrs="nick_cramer@outlook.com",
            msg=f"Subject: Amazon Price Alert!\n\n{message}\n{PRODUCT_URL}".encode("utf-8")
        )

    print("Email sent.")
else:
    print(f"Product is not below desired buy price. Current product price: {price}")
