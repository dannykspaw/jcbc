from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

DRIVER_PATH = '/Users/danielkearney-spaw/Downloads/chromedriver'

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

driver.get("https://www.hallmarkornaments.com/Hallmark-Ornaments-By-Year_c_200.html")
#x_path_helper = '"top-categories-menu"'
#year_menu = driver.find_element_by_xpath('//*[@id={}]/div/ul/li[1]/a'.format(x_path_helper))
#year_menu.click()

x = 1973
prod_num = 1
limit = 40
y = 1
subcat_block = '"subcategoriesBlock"'
prodcat_block = '"productCategoryBlock"'
price_id = '"price"'
ornament_id = '"product_id"'
name_id = '"add"'
for y in range (y,10):
    try:
        year_link = driver.find_element_by_xpath("//*[@id={}]/div[2]/ul/li[{}]/div/div/a".format(subcat_block, y))
        print(year_link.text)
        year_link.click()
        time.sleep(1)
        x += 1
        while prod_num < limit:
            try:
                print("Scraping products...")
                ornament_link = driver.find_element_by_xpath("//*[@id={}]/div[4]/div/div/div[{}]/div/div[1]/a".format(prodcat_block, prod_num))
                ornament_link.click()
                print(driver.currenturl)
                print("in")
                ornament_name = driver.find_element_by_xpath("//*[@id={}]/div[1]/div[2]/h1".format(name_id))
                ornament_price = driver.find_element_by_xpath("//*[@id={}]".format(price_id))
                ornament_id = driver.find_element_by_xpath("//*[@id={}]".format(ornament_id))
                print(ornament_id.text, ornament_name.text, ornament_price.text)
                print(driver.currenturl)
                driver.navigate().back()
                print("Back at product page")
                time.sleep(1)
                prod_num += 1
            except:
                print("Done scraping ",prod_num-1,"ornaments")
                prod_num = limit
        print("going back to year page", prod_num)
        print("")
        driver.execute_script("window.history.go(-1)")
    except:
        # print("ERRORED OUT", x)
        x += 1
print("Exited page find loop")
driver.quit()
