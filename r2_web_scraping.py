from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import numpy as np
import time

DRIVER_PATH = '/Users/danielkearney-spaw/Downloads/chromedriver'

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

driver.get("https://www.hallmarkornaments.com/Hallmark-Ornaments-By-Year_c_200.html")

seventies_year_link = driver.find_elements_by_partial_link_text('197')
eighties_year_link = driver.find_elements_by_partial_link_text('198')
nineties_year_link = driver.find_elements_by_partial_link_text('199')
twothousand_year_link = driver.find_elements_by_partial_link_text('200')
twothousandten_year_link = driver.find_elements_by_partial_link_text('201')
twothousandtwo_year_link = driver.find_elements_by_partial_link_text('202')

all_years = seventies_year_link + eighties_year_link + nineties_year_link + twothousand_year_link + twothousandten_year_link + twothousandtwo_year_link

for x in all_years:
    x = x.get_attribute('href')
    print(x)
