from requests import get
from smtplib import SMTP
from re import fullmatch
from sys import exit
from time import sleep
from bs4 import BeautifulSoup

best_buy = "https://www.bestbuy.ca/en-ca/"
amazon = "https://www.amazon.ca/"
canada_computers = "https://www.canadacomputers.com/product_info.php?cPath="
URL = input('Please enter a Product URL from either Best Buy Canada, Canada Computers or Amazon Canada: ')
user_email = input('Please enter your email that you would like to be contacted at: ')
if not fullmatch('\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?', user_email):
    exit('You have entered an INVALID email!')

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
}

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

if best_buy in URL:
    def bb_check_price():
        page = get(URL, headers=headers)
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
                send_mail(user_email, bb_title, bb_price, URL)
            else:
                print("Thank you for using our service. We'll get back to you shortly!")

        except AttributeError:
            print("Hmmm. Try to re-enter the URL of a product that is not already on sale.")
        except NameError:
            print("Hmmm. Try to re-enter the URL of a product that is not already on sale.")
        

elif amazon in URL:
    def az_check_price():
        page = get(URL, headers=headers)
        page_soup = BeautifulSoup(page.content, "html.parser")
        amazon_title = page_soup.find(id="productTitle").get_text().strip()
        
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
            send_mail(user_email, amazon_title, amazon_price, URL)
        else:
            print("Thank you for using our service. We'll get back to you shortly!")


elif canada_computers in URL:
    def cc_check_price():
        page = get(URL, headers=headers)
        page_soup = BeautifulSoup(page.content, "html.parser")
        cc_title = page_soup.find("meta", attrs={"property": "og:title"})["content"]

        try:
            cc_price = page_soup.find("meta", attrs={"name": "price"})["content"]
            # turns $1,699.00 to 1699.0
            if len(cc_price) == 7:
                cc_price = float(cc_price[1:7])
            elif len(cc_price) == 9:
                cc_price = float(cc_price[1])*1000.0 + float(cc_price[3:9])
            elif len(cc_price) == 6:
                cc_price = float(cc_price[1:6])
            # $9.99
            elif len(cc_price) == 5:
                cc_price = float(cc_price[1:5])
            
            sale_price = cc_price

            if sale_price <= cc_price:
                send_mail(user_email, cc_title, sale_price, URL)
            else:
                print("Thank you for using our service. We'll get back to you shortly!")
        except AttributeError:
            print("Hmmm. Try to re-enter the URL of a product that is not already on sale.")


######################################################################################################
######################################################################################################
######################################################################################################

elif best_buy not in URL or amazon not in URL or canada_computers not in URL:
    print("Something's not working... Try to re-enter a link from either Best Buy Canada,"
          " Amazon Canada or Canada Computers")

if best_buy in URL:
    bb_check_price()
    sleep(86400)
elif amazon in URL:
    az_check_price()
    sleep(86400)
else:
    cc_check_price()
    sleep(86400)

'''this runs the program every day. This means the price is checked every 24-hours 
and a single deal will not be missed'''