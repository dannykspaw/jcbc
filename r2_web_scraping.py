from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import numpy as np
import pandas as pd
import time
from csv import reader
from joblib import Parallel, delayed
import multiprocessing


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
product_availability = []
product_brand = []
product_data_links =[]
#
# for x in range(1973, 2020):
#     driver.get(year_link_list[x])
#     time.sleep(1)
#     try:
#         view_all_link = driver.find_element_by_class_name("category-viewall")
#         view_all_link.click()
#     except:
#         print("No view all")
#
#     try:
#         number_of_products = driver.find_element_by_class_name('product-count')
#         number_of_products = number_of_products.text[26:]
#         #Working on viewing all products here.text
#         print("NUMBER OF PRODUCTS: ", number_of_products)
#         product_name_list = driver.find_elements_by_class_name('name')
#         for x in product_name_list:
#             product_names.append(x.text)
#             product_link_location = driver.find_element_by_partial_link_text(x.text)
#             product_link = product_link_location.get_attribute("href")
#             product_links.append(product_link)
#             # print(x.text, " : ", product_link)
#         print("product links", len(product_links))
#         # iter_products_num = int(number_of_products)
#         # for product in iter_products_num:
#         #     product_name = driver.find_elements_by_class_name("name")
#     except:
#         print("NUMBER OF PRODUCTS: 0")

# product_link_df = pd.DataFrame()
# product_link_df.insert(0,"Links",product_links)
# product_link_df.to_csv(path_or_buf="product_links.csv", index=False)

# open file in read mode
with open('hallmark_ornaments_21.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
    header = next(csv_reader)
    # Check file as empty
    if header != None:
        for row in csv_reader:
            # row variable is a list that represents a row in csv
            print(row)
            product_url = row[0]
            product_data_links.append(product_url)
            driver.get(product_url)
            try:
                price = driver.find_element_by_id("price").text
                product_prices.append(price)
                code = driver.find_element_by_id("product_id").text
                product_codes.append(code)
                # print("Appended code and price for ",x)
                availability_list = driver.find_elements_by_id("availability")
                brand = availability_list[0].text
                product_brand.append(brand)
                availability = availability_list[1].text
                product_availability.append(availability)
                name = driver.find_element_by_class_name("page_headers")
                product_names.append(name.text)
            except:
                price = "price error"
                brand = "brand error"
                code = "code error"
                availability = "availbility error"
                product_prices.append(price)
                product_codes.append(code)
                product_brand.append(brand)
                product_availability.append(availability)

ornament_df = pd.DataFrame()
ornament_df.insert(0,"Product Code",product_codes)
ornament_df.insert(1,"Product Name",product_names)
ornament_df.insert(2,"Product Price",product_prices)
ornament_df.insert(3,"Product Brand", product_brand)
ornament_df.insert(4,"Product Availability", product_availability)
ornament_df.insert(5,"Product Link",product_data_links)
ornament_df.to_csv(path_or_buf="hallmark_ornaments_21_prod_info.csv", index=False)

print("DONE")
driver.quit()
