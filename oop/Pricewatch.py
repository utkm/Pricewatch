from requests import get
from smtplib import SMTP
from re import fullmatch
from sys import exit
from time import sleep
from bs4 import BeautifulSoup
from CanadaComp import CanadaComputers

def send_mail(email_addr, product_title, product_price, product_URL):
    server = SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('m.utkarsh10@gmail.com', 'fiwjlmehyuoobvvc')

    subject = "The Moment You've been waiting for: The Price Has Decreased!"
    body = 'Hey!\nThe Price of ' + product_title + " has finally decreased to $" + str(product_price)+ "!\n\nClick the link: "\
            + product_URL + " to claim your deal now!"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('m.utkarsh10@gmail.com', user_email, msg)
    print("Email has been sent")
    server.quit()
    exit()


if __name__ == "__main__":
    best_buy = "https://www.bestbuy.ca/en-ca/"
    amazon = "https://www.amazon.ca/"
    canada_computers = "https://www.canadacomputers.com/product_info.php?cPath="

    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

    URL = input('Please enter a Product URL from either Best Buy Canada, Canada Computers or Amazon Canada: ')
    user_email = input('Please enter your email that you would like to be contacted at: ')

    if not fullmatch('\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?', user_email):
        exit('You have entered an INVALID email!')

    if best_buy in URL:
        pass
    elif amazon in URL:
        pass
    elif canada_computers in URL:
        cc = CanadaComputers(URL, headers, user_email)
        cc.cc_check_price()
        
    else:
        print("Something's not working... Try to re-enter a link from either Best Buy Canada,"
          " Amazon Canada or Canada Computers")