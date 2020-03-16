from requests import get
from smtplib import SMTP
from re import fullmatch
from sys import exit
from time import sleep
from bs4 import BeautifulSoup

best_buy = "https://www.bestbuy.ca/en-ca/"
amazon = "https://www.amazon.ca/"
canada_computers = "https://www.canadacomputers.com/product_info.php?cPath="

URL = input('Please enter a URL from either Best Buy Canada, Canada Computers or Amazon Canada: ') 
user_email = input('Please enter your email that you would like to be contacted at: ')

headers = {
    'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

if best_buy in URL:
    def bb_check_price():
        page = get(URL, headers=headers)
        page_soup = BeautifulSoup(page.content, "html.parser")

        global bb_title
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
            if sale_price < bb_price:
                send_mail()
            else:
                print("Thank you for using our service. We'll get back to you shortly!")

        except AttributeError:
            print("Hmmm. Try to re-enter the URL of a product that is not already on sale.")
        except NameError:
            print("Hmmm. Try to re-enter the URL of a product that is not already on sale.")
        
    def send_mail():
        server = SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login('pricewatch.pp@gmail.com', '# enter app password')

        subject = "The Moment You've been waiting for: The Price Has Decreased!"
        body = 'Hey!\nThe Price of ' + bb_title + " has finally decreased!\n\nClick the link: "\
               + URL + " to claim your deal now!"

        msg = f"Subject: {subject}\n\n{body}"

        server.sendmail('pricewatch.pp@gmail.com', user_email, msg)
        print("Email has been sent")
        server.quit()

elif amazon in URL:
    def az_check_price():
        page = get(URL, headers=headers)
        page_soup = BeautifulSoup(page.content, "html.parser")
        # print(page_soup)
        global amazon_title
        amazon_title = page_soup.find(id="productTitle").get_text().strip()
        
        price = page_soup.find(id="priceblock_ourprice").get_text().strip()
        if len(price) == 10:
            price = int(price[5:7]) + float(price[7:10])
        elif len(price) == 9:
            price = int(price[5:6]) + float(price[6:9])
        elif len(price) == 13:
            price = price[5] + price[7:10] + price[10:13]
            price = float(price)
        
        sale_price = price
        if sale_price <= price:
            send_mail()
        else:
            print("Thank you for using our service. We'll get back to you shortly!")

    def send_mail():
        server = SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login('pricewatch.pp@gmail.com', '# enter app password')

        subject = "The Moment You've been waiting for: The Price Has Decreased!"
        body = 'Hey!\nThe Price of ' + amazon_title + " has finally decreased!\n\nClick the link: "\
               + URL + " to claim your deal now!"

        msg = f"Subject: {subject}\n\n{body}"

        server.sendmail('pricewatch.pp@gmail.com', user_email, msg)
        print("Email has been sent")
        server.quit()

elif canada_computers in URL:
    def cc_check_price():
        page = get(URL, headers=headers)
        page_soup = BeautifulSoup(page.content, "html.parser")

        global cc_title
        cc_title = page_soup.find("h1", {"class": "h3 product-title mb-2"}).get_text().strip()

        try:
            cc_price = page_soup.find("div", {"class": "col-auto col-md-12 order-2 order-md-1"}).get_text().strip()
            if len(cc_price) == 7:
                cc_price = float(cc_price[1:7])
            # turns $139.99 to 139.99
            elif len(cc_price) == 9:
                cc_price = int(cc_price[1]) + float(cc_price[3:9])
            elif len(cc_price) == 6:
                cc_price = float(cc_price[1:6])
            elif len(cc_price) == 5:
                cc_price = float(cc_price[1:5])
                # $9.99
            sale_price = cc_price
            if sale_price <= cc_price:
                send_mail()
            else:
                print("Thank you for using our service. We'll get back to you shortly!")

        except AttributeError:
            print("Hmmm. Try to re-enter the URL of a product that is not already on sale.")

    def send_mail():
        server = SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        
        server.login('pricewatch.pp@gmail.com', '# enter app password')

        subject = "The Moment You've been waiting for: The Price Has Decreased!"
        body = 'Hey!\nThe Price of ' + cc_title + " has finally decreased!\n\nClick the link: "\
               + URL + " to claim your deal now!"

        msg = f"Subject: {subject}\n\n{body}"

        server.sendmail('pricewatch.pp@gmail.com', user_email, msg)
        print("Email has been sent")
        server.quit()

######################################################################################################
######################################################################################################
######################################################################################################

elif best_buy not in URL or amazon not in URL or canada_computers not in URL:
    print("Something's not working... Try to re-enter a link from either Best Buy Canada,"
          " Amazon Canada or Canada Computers")
    while 1:
        break

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