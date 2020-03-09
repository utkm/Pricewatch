# PriceChecker
Using Python, I created a script that tracks the prices of a certain product and sends you an email once it drops!

Over the past few months, I've spent HOURS searching for computer parts to build my PC. 
Everytime I find a high-quality product, I find myself spending hours glued to the computer, refreshing the site, waiting for a sale.

So, I created a Python script that scrapes the data off compatible* websites using a Python Module called BeautifulSoup.
I also used the SMTPLIB module to be able to send any valid email a notification that the price of the product has gone down. Email validation is done using a simple RegEx (Regular Expression) and checks whether or not the email is valid.

How it Works:
1. Enter a URL from one of the compatible websites
2. Enter an email that you wish to be contacted at 
3. You will be sent an email when the price of the given product decreases
4. If the price doesn't decrease, not to worry! Using the sleep function from the time module, the code will run every 24 hours.
___

***Next Steps:***
- Amazon has initiated a firewall to protect from bots, so I hope to implement the Amazon API to increase reliability
- This program currently runs on the command line however in the future I'd love to build a front end using Tkinter
- As of now, I've made the script compatible with Best Buy, Canada Computers and Amazon but I hope to make it compatible with Newegg soon!

This project was presented in my International Baccalaureate 'Personal Project'. If you're interested here's the [link](http://bit.ly/Pricewatch) to my presentation

Thanks!
