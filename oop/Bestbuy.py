from requests import get
from smtplib import SMTP
from bs4 import BeautifulSoup
from Pricewatch import send_mail

class BestBuy():
    def __init__(self, URL, headers, user_email):
        self.URL = URL
        self.headers = headers

    def bb_check_price(self):
        page = get(self.URL, headers=self.headers)
        page_soup = BeautifulSoup(page.content, "html.parser")

        bb_title = page_soup.find("div", {"class": "x-product-detail-page"})
        bb_title = bb_title.h1.text

        try:
            bb_price = page_soup.find("div", {"class": "price_FHDfG large_3aP7Z"}).get_text()
            if len(bb_price) == 6:
                bb_price = float(bb_price[1:4])
            # turns $28999 to 289
            elif len(bb_price) == 8:
                bb_price = int(bb_price[1]) + float(bb_price[3:6])
            elif len(bb_price) == 5:
                bb_price = float(bb_price[1:3])

            sale_price = bb_price
            if sale_price <= bb_price:
                send_mail(self.user_email, bb_title, bb_price, self.URL)
            else:
                print("Thank you for using our service. We'll get back to you shortly!")

        except AttributeError:
            print("Hmmm. Try to re-enter the URL of a product that is not already on sale.")
        except NameError:
            print("Hmmm. Try to re-enter the URL of a product that is not already on sale.")
