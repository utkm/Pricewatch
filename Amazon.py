from requests import get
from smtplib import SMTP
from bs4 import BeautifulSoup
from Pricewatch import send_mail

class Amazon():
    def __init__(self, URL, headers, user_email):
        self.URL = URL
        self.headers = headers

    def amzn_check_price(self):
        page = get(self.URL, headers=self.headers)
        page_soup = BeautifulSoup(page.content, "html.parser")
        amazon_title = page_soup.find(id="productTitle").get_text().strip()
        
        try:
            amazon_price = page_soup.find(id="priceblock_ourprice").get_text().strip()
            if len(amazon_price) == 10:
                amazon_price = int(amazon_price[5:7]) + float(amazon_price[7:10])
            elif len(amazon_price) == 9:
                amazon_price = int(amazon_price[5:6]) + float(amazon_price[6:9])
            elif len(amazon_price) == 13:
                amazon_price = amazon_price[5] + amazon_price[7:10] + amazon_price[10:13]
                amazon_price = float(amazon_price)
            
            sale_price = amazon_price
            if sale_price <= amazon_price:
                send_mail(self.user_email, amazon_title, amazon_price, self.URL)
            else:
                print("Thank you for using our service. We'll get back to you shortly!")
        except AttributeError:
            print("Hmmm. Try to re-enter the URL of a product that is not already on sale.")