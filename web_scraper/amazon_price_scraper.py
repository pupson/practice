import requests, os, smtplib, lxml
from bs4 import BeautifulSoup

# WEB SCRAPER
amazon_product_url = PRODUCT_URL
product_name = (amazon_product_url.split("/")[3]).replace('-', ' ')
header = {
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "referer": "https://www.amazon.com/",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language":"en-US,en;q=0.9",
    "Cookie": "PHPSESSID=6e67aae0751794cb32d8a629a3a95756"
}

response = requests.get(amazon_product_url, headers=header)
amazon_text = response.content
soup = BeautifulSoup(amazon_text, "lxml")
#print(soup.prettify())
product_price_code = soup.find(class_="a-offscreen").get_text()
product_price = float(product_price_code.split("$")[1])

# MAIL BLOCK
BUY_PRICE = TARGET_FLOAT_PRICE

if product_price < BUY_PRICE:

    sender_email = SENDER_MAIL
    receiver_email = TO_MAIL
    YOUR_PASSWORD = GMAIL_APP_KEY

    subject = f"AMAZON LOW PRICE FOR: {product_name} $$$$ {product_price}"
    message = f"Subject: {subject}\n\n{product_name} is now {product_price}\n{amazon_product_url}"

    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        result = connection.login(sender_email, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=sender_email,
            to_addrs=receiver_email,
            msg=message
        )