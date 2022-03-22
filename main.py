from bs4 import BeautifulSoup
import requests
import lxml
import urllib.request

#WE are tracking the price of a Hair Steampod
URL = "https://www.amazon.co.uk/LOr%C3%A9al-Professionnel-Steampod-Straightener-Styling/dp/B09KSCBK2J/ref=sr_1_7?crid=ZXHX1V3ZGT6N&keywords=loreal+steampod+3.0+steam+straightener&qid=1637483452&qsid=259-2565520-8994044&s=beauty&sprefix=loreal+stea%2Cbeauty%2C236&sr=1-7&sres=B081B3ZKJR%2CB09GYN63J2%2CB09KSCBK2J%2CB08KG83JY7%2CB09CHR663L%2CB01D8MV0CS%2CB07G3RMWD9%2CB07DT9TTL2%2CB000CSLJDW%2CB078S4B4V2%2CB081H4YPQ8%2CB075N8ZYWZ%2CB087MWCNHQ%2CB008BDSZFK%2CB07YBG8X5P%2CB084MKMXYF%2CB08D9HLNQ4%2CB0896L5C42%2CB08NJ4YG4C%2CB0842R4373&srpt=HAIR_IRON"

BUY_PRICE = 190
MY_EMAIL = ""
MY_PASS = ""

webURL = urllib.request.urlopen(URL)
webURL_read = webURL.read()
data = BeautifulSoup(webURL_read, "html.parser")

product_price = data.find(name="span", class_="a-size-medium a-color-price")
product_price = float(product_price.getText().strip("\n").strip("£"))
print(product_price)
product = data.find(name="span", id="productTitle").getText().strip("\n")
print(product)

if product_price < BUY_PRICE:
     with smtplib.SMTP("smtp.gmail.com") as connection:
         connection.starttls()
         connection.login(user=MY_EMAIL, passwd= MY_PASS)
         connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Amazon Price ALert\n\n THe price of {product} dropped to £{product_price}"
         )
