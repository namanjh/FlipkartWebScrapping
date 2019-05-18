# -*- coding: utf-8 -*-
"""
Created on Sat May 18 19:52:49 2019

@author: naman
"""
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq
import re


#_______________________CSV File Opeartions_________________
filename = "flipkart_data.csv"

fp = open(filename,"w",encoding = 'utf-8')
headers = "Product_ID, Product_Name, Rating, Rated_by, MRP, Discount,Current_Price \n"

fp.write(headers)

#________________________Web Scraping_____________________
myurl = "https://www.flipkart.com/search?q=earphones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

#opening the connection and grabbing the page
client = ureq(myurl)
page = client.read()
client.close()

page_soup = soup(page, "html.parser")

#grabbing for each container containing products
containers = page_soup.findAll("div",{"class":"_3liAhj _1R0K0g"})
product_id = 0
for container in containers:
    
    #assign a product id so that it will be easy to index
    product_id += 1
    
    #to find the name.. inspect the webpage for class names and the html structure
    names = container.findAll("a", {"class":"_2cLu-l"})
    product_name = names[0].text
    
    #rating
    rates = container.findAll("div",{"class": "hGSR34"})
    rate = rates[0].text
    
    #rated by 
    ratings = container.findAll("span",{"class":"_38sUEc"})
    rated_by = ratings[0].text
    rated_by = rated_by.strip('()')
    
    #original price
    original_prices = container.findAll("div",{"class":"_3auQ3N"})
    original_price = original_prices[0].text
    
    #discount rate
    discounts = container.findAll("div",{"class":"VGWI6T"})
    discount = discounts[0].text
    discount_percentage = int(re.search(r'\d+', discount).group())
    discount_percentage
    
    #current_price
    discounted_prices = container.findAll("div",{"class":"_1vC4OE"})
    discounted_price = discounted_prices[0].text
    discounted_price = discounted_price.strip('₹')
    
    #to check if all the variables are in correct format
    '''
    print("product_name: " , product_name)
    print("rate: ",rate)
    print("rated_by: ",rated_by)
    print("original_price: ",original_price)
    print("discount_percentage: ",discount_percentage)
    print("discounted_price: ",discounted_price)
    '''
    #to write all the values into a csv file
    fp.write(str(product_id) + "," + str(product_name) + "," + str(rate) + "," + str(rated_by) + "," + str(original_price) + "," + str(discount_percentage) + "," + str(discounted_price) + "\n")

#Yeah, Just forgot,.. never forget to close the connection
fp.close()


