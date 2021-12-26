import requests
from Mail import SendMail
from requests_html import HTMLSession

class BestBuy():
    def __init__(self, URL, headers, user_email):
        self.URL = URL
        self.headers = headers
        self.user_email = user_email

    def bb_check_price(self, curr_price):
        try:
            session = HTMLSession()
            response = session.get(self.URL)
            
        except requests.exceptions.RequestException as e:
            print(e)

        self.product_title =  response.html.find('title')
        self.product_title = self.product_title[0].text
        # print(title)
        
        self.product_price = response.html.find(".price_FHDfG")
        self.product_price = self.product_price[0].text
        self.product_price = float(self.product_price[1:-2])*1.0 + float(self.product_price[-2:])*0.01
        # print(product_price)

        mail_to = SendMail(self.user_email, self.product_title, self.product_price, self.URL)
        # mail_to.send_mail()

        if self.product_price < curr_price and curr_price != 99999:
            mail_to.send_mail(self.product_title, self.product_price, self.URL)
        else:
            curr_price = self.product_price
            print("Thank you for using our service. We'll get back to you shortly!")
        
        return self.product_price