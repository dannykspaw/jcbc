from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import numpy as np
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
for x in range(1973,1999):
    driver.get(year_link_list[x])
    time.sleep(1)
    try:
        number_of_products = driver.find_element_by_class_name('product-count')
        number_of_products = number_of_products.text[26:]
        #Working on viewing all products here
        print("NUMBER OF PRODUCTS: ", number_of_products)
        time.sleep(1)
        product_name_list = driver.find_elements_by_class_name('name')
        product_names = []
        for x in product_name_list:
            print(x.text," : ", x.get_attribute("href"))
        # iter_products_num = int(number_of_products)
        # for product in iter_products_num:
        #     product_name = driver.find_elements_by_class_name("name")
    except:
        print("NUMBER OF PRODUCTS: 0")
print("DONE")
driver.quit()
