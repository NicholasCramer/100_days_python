from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
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

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()

for key, value in header.items():
    chrome_options.add_argument(f"--{key}={value}")

chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(PRODUCT_URL)

# Bypass captcha by selecting try different image link
has_captcha = True

while has_captcha:
    try:
        captcha = driver.find_element(By.LINK_TEXT, "Try different image")
        captcha.click()
    except NoSuchElementException:
        has_captcha = False

price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
print(f"The price is {price_dollar.text}.{price_cents.text}")

title = driver.find_element(By.ID, value="productTitle")
print(f"The product name is {title.text}")

driver.quit()

# Send email when price is below configured threshold
BUY_PRICE = 100

if int(price_dollar.text) < BUY_PRICE:
    message = f"{title} is now ${price_dollar.text}.{price_cents.text}"
    print(message)

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
    print(f"Product is not below desired buy price. Current product price: ${price_dollar.text}.{price_cents.text}")
