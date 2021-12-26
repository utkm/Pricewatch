from smtplib import SMTP
from sys import exit

class SendMail():
    def __init__(self, user_email, product_title, product_price, product_URL):
        self.user_email = user_email
        self.product_title = product_title
        self.product_price = product_price
        self.product_URL = product_URL

    def send_mail(self):
        server = SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login('m.utkarsh10@gmail.com', 'fiwjlmehyuoobvvc')

        subject = "The Moment You've Been Waiting For: The Price Has Decreased!"
        body = 'Hey!\nThe Price of ' + self.product_title + " has finally decreased to $" + str(self.product_price)+ "!\n\nClick the link: "\
                + self.product_URL + " to claim your deal now!"

        msg = f"Subject: {subject}\n\n{body}"

        server.sendmail('m.utkarsh10@gmail.com', self.user_email, msg)
        print("Email has been sent")
        server.quit()
        exit()