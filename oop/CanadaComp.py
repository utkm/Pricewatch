from requests import get
from smtplib import SMTP
from bs4 import BeautifulSoup

class CanadaComputers():
    def __init__(self, URL, headers, user_email):
        self.URL = URL
        self.headers = headers
        self.user_email = user_email
    
    def send_mail(self):
        server = SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login('m.utkarsh10@gmail.com', 'fiwjlmehyuoobvvc')

        subject = "The Moment You've been waiting for: The Price Has Decreased!"
        body = 'Hey!\nThe Price of ' + self.product_title + " has finally decreased to $" + str(self.product_price)+ "!\n\nClick the link: "\
                + self.URL + " to claim your deal now!"

        msg = f"Subject: {subject}\n\n{body}"

        server.sendmail('m.utkarsh10@gmail.com', self.user_email, msg)
        print("Email has been sent")
        server.quit()
        exit()
        

    def cc_check_price(self):
        page = get(self.URL, headers=self.headers)
        page_soup = BeautifulSoup(page.content, "html.parser")
        self.product_title = page_soup.find("meta", attrs={"property": "og:title"})["content"]

        try:
            self.product_price = page_soup.find("meta", attrs={"name": "price"})["content"]
            # turns $1,699.00 to 1699.0
            if len(self.product_price) == 7:
                cc_price = float(self.product_price[1:7])
            elif len(self.product_price) == 9:
                cc_price = float(self.product_price[1])*1000.0 + float(self.product_price[3:9])
            elif len(self.product_price) == 6:
                cc_price = float(self.product_price[1:6])
            # $9.99
            elif len(self.product_price) == 5:
                cc_price = float(self.product_price[1:5])
            
            sale_price = self.product_price

            if sale_price <= self.product_price:
                self.send_mail()
            else:
                print("Thank you for using our service. We'll get back to you shortly!")
        except AttributeError:
            print("Hmmm. Try to re-enter the URL of a product that is not already on sale.")