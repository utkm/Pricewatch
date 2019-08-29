# PriceChecker
Using Python, I created a script that tracks the prices of a certain product and sends you an email once it drops!

Over the past few months, I've spent HOURS searching for computer parts to build my PC. 
Everytime I find a high-quality product, I find myself spending hours glued to the computer, refreshing the site, waiting for a sale.

So, I created a Python script that scrapes the data off compatible* websites using a Python Module called BeautifulSoup.
I also used the smtplib module to be able to send any valid email a notification that the price of the product has gone down.

How it Works:
1. Enter a URL from one of the compatible websites
2. Enter an email that you wish to be contacted at 
3. You will be sent an email when the price of the given product decreases
4. If the price doesn't decrease, not to worry! Using the time module, the code will run every 24 hours.

Next Steps: 
As of now, this program runs on the command line however in the future I'd love to utilise a web framework such as Django or Flask to have a functioning UI that users can interact with.

/* as of now, I've made the script compatible with Best Buy, Canada Computers and Amazon but I hope to make it compatible with Newegg soon!
