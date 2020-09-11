from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import numpy as np
import pandas as pd
import time

# Establish webdriver path
DRIVER_PATH = '/Users/danielkearney-spaw/Downloads/chromedriver'

#Set webdriver options
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

#Go to initial website
driver.get("https://www.hallmarkornaments.com/Hallmark-Ornaments-By-Year_c_200.html")

#Grab years
seventies_year_link = driver.find_elements_by_partial_link_text('197')
eighties_year_link = driver.find_elements_by_partial_link_text('198')
nineties_year_link = driver.find_elements_by_partial_link_text('199')
twothousand_year_link = driver.find_elements_by_partial_link_text('200')
twothousandten_year_link = driver.find_elements_by_partial_link_text('201')
twothousandtwo_year_link = driver.find_elements_by_partial_link_text('202')

#combine years into one list
all_years = seventies_year_link + eighties_year_link + nineties_year_link + twothousand_year_link + twothousandten_year_link + twothousandtwo_year_link
year_link_list = {}

#create year and url dictionary
year = 1973

for x in all_years:
    year_url = x.get_attribute('href')
    year_link_list.update({year : year_url})
    year += 1

# print(year_link_list)

#Find products in each year, this is a simple iteration that pulls the year links and product names

product_names = []
product_links = []
product_prices = []
product_codes = []

for x in range(1973,1978):
    driver.get(year_link_list[x])
    time.sleep(1)
    try:
        number_of_products = driver.find_element_by_class_name('product-count')
        number_of_products = number_of_products.text[26:]
        #Working on viewing all products here.text
        print("NUMBER OF PRODUCTS: ", number_of_products)
        time.sleep(1)
        product_name_list = driver.find_elements_by_class_name('name')
        for x in product_name_list:
            product_names.append(x.text)
            product_link_location = driver.find_element_by_partial_link_text(x.text)
            product_link = product_link_location.get_attribute("href")
            product_links.append(product_link)
            print(x.text, " : ", product_link)
        print(len(product_links))
        for x in product_links:
            driver.get(x)
            price = "price_placeholder"
            price = driver.find_element_by_id("price").text
            product_prices.append(price)
            code = "code_placeholder"
            # code = driver.find_element_by_id("product_id").text
            product_codes.append(code)
        # iter_products_num = int(number_of_products)
        # for product in iter_products_num:
        #     product_name = driver.find_elements_by_class_name("name")
    except:
        print("NUMBER OF PRODUCTS: 0")

print(product_codes)
print(len(product_codes))
print(product_prices)
print(len(product_prices))
print(product_names)
print(len(product_names))
print(product_links)
print(len(product_links))

# ornament_db = pd.DataFrame()
# ornament_db.insert(0,"Product Name",product_names)
# ornament_db.insert(1,"Product Code",product_codes)
# ornament_db.insert(2,"Product Prices",product_prices)
# ornament_db.insert(3,"Product Link",product_links)
# ornament_db.head()

print("DONE")
driver.quit()
