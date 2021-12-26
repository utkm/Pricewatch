from requests import get
from bs4 import BeautifulSoup
from Mail import SendMail

class CanadaComputers():
    def __init__(self, URL, headers, user_email):
        self.URL = URL
        self.headers = headers
        self.user_email = user_email
           

    def cc_check_price(self, curr_price):
        page = get(self.URL, headers=self.headers)
        page_soup = BeautifulSoup(page.content, "html.parser")
        self.product_title = page_soup.find("meta", attrs={"property": "og:title"})["content"]

        try:
            self.product_price = page_soup.find("meta", attrs={"name": "price"})["content"]
            # turns $1,699.00 to 1699.0
            if len(self.product_price) == 7:
                self.product_price = float(self.product_price[1:7])
            elif len(self.product_price) == 9:
                self.product_price = float(self.product_price[1])*1000.0 + float(self.product_price[3:9])
            elif len(self.product_price) == 6:
                self.product_price = float(self.product_price[1:6])
            # $9.99
            elif len(self.product_price) == 5:
                self.product_price = float(self.product_price[1:5])
            
            mail_to = SendMail(self.user_email, self.product_title, self.product_price, self.URL)
            #mail_to.send_mail()

            if self.product_price < curr_price and curr_price != 99999:
                mail_to.send_mail(self.product_title, self.product_price, self.URL)
            else:
                curr_price = self.product_price
                print("Thank you for using our service. We'll get back to you shortly!")
        except AttributeError:
            print("Hmmm. Try to re-enter the URL of a product that is not already on sale.")
        
        return self.product_price