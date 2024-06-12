import requests
from bs4 import BeautifulSoup
from .models import *
import threading
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def search_flipkart_product(product_name,result_container):
    search_url = f'https://www.flipkart.com/search?q={product_name}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(search_url, headers=headers)
    print(response.status_code)
    soup = BeautifulSoup(response.content, 'html.parser')
    products={'url': None , 'price': None, 'name': None}
    items = soup.find_all('div', {'class': '_75nlfW'})
    print(items)
    for item in items:
        product_name = item.find('div', {'class': 'KzDlHZ'}).text.strip()
        product_price = float(item.find('div', {'class': 'Nx9bqj _4b5DiR'}).text.strip().replace("₹", "").replace(",", ""))
        # url_item=soup.find('div', {'class': 'cPHDOP col-12-12'})
        # print(url_item)
        product_url = 'https://www.flipkart.com' + item.find('a', {'class': 'CGtC98'}).get('href')
        products={'url': product_url, 'price': product_price, 'name': product_name}
        break
    result_container.append({"name":"flipkart","result":products})
    return products

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def scrape_product_info(driver, item,result_container):
    try:
        search_url = f"https://www.google.com/search?q={item}+at+chroma"
        driver.get(search_url)
        time.sleep(5)

        max_retries = 5
        for _ in range(max_retries):
            try:
                link = driver.find_element(By.CSS_SELECTOR, "div.g a")
                link.click()
                break
            except Exception as e:
                print("Error finding search result link:", e)
                driver.back()
                driver.refresh()
                time.sleep(5)
                driver.refresh()
        else:
            raise Exception("Failed to find search result link after multiple attempts")

        time.sleep(5)

        try:
            product_name_element = driver.find_element(By.XPATH, '//h1[contains(@class, "pd-title")]')
            product_link = driver.current_url
            if product_name_element:
                pass
            else :
                product_name_element = driver.find_element(By.XPATH, "//h3/a")
                product_link = product_name_element.get_attribute("href")
        except Exception as e:
            print("Error finding product name element:", e)
            try:
                product_name_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.g a")) )
                if  product_name_element is None:
                    product_name_element = driver.find_element(By.XPATH, "//h3")
                    product_link = product_name_element.get_attribute("href")
            except Exception as e:
                print("Error finding product name element:", e)
                product_name_element=driver.find_element(By.CLASS_NAME,'product-title')
                product_link = driver.current_url
               

        product_name = product_name_element.text.strip()

        try:
            product_price_element = driver.find_element(By.CLASS_NAME, "plp-srp-new-amount")
        except Exception as e:
            print("Error finding product price element:", e)
            try:
                product_price_element = driver.find_element(By.XPATH, '//*[@id="pdp-product-price"]')
            except Exception as e:
                print("Error finding product price element:", e)
                product_price_element = driver.find_element(By.CLASS_NAME, "amount")

        product_price_text = product_price_element.text.strip().replace("₹", "").replace(",", "")
        product_price = float(product_price_text)
        driver.quit()
        products =  {'name':product_name, 'price':product_price,'url': product_link}
        result_container.append({"name":"croma","result":products})
        return products

    except Exception as e:
        print(driver.page_source)
        print("Error:", e)
        
        products = {'name':None, 'price':None,'url': None}
        result_container.append({"name":"croma","result":products})
        return products 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def search_amazon_product(product_name,driver,result_container):
    
    try:
        for i in range (0,6):
            try :
                driver.get("https://www.amazon.in")
                time.sleep(2) 
        
                search_box = driver.find_element(By.ID, "twotabsearchtextbox")
                break
            except Exception as e:
                print("Error finding search result link:", e)
                driver.back()
                driver.refresh()
                time.sleep(5)

        search_box.send_keys(product_name)
        search_box.send_keys(Keys.RETURN)
        time.sleep(5)
        first_result = driver.find_element(By.XPATH, "//div[@data-component-type='s-search-result']")
        product_name = first_result.find_element(By.XPATH, ".//span[@class='a-size-medium a-color-base a-text-normal']").text.strip()
        product_price = first_result.find_element(By.XPATH, ".//span[@class='a-price-whole']").text.strip()
        product_price = float(product_price.replace(",", ""))
        first_result.click()
        product_url=driver.current_url
        driver.quit()
        products= {'url':product_url, 'price':product_price, 'name':product_name}
        result_container.append({"name":"amazon","result":products})
        return products
        
        
    except Exception as e:
        print("Error:", e)
        products = {'name':None, 'price':None,'url': None}
        result_container.append({"name":"amazon","result":products})
        return products
    


def prices(productname):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36")
    chrome_driver_path = "C:/Users/yaswa/Downloads/FlipKart_Selenium-main/chromedriver.exe"
    a_driver = webdriver.Chrome(executable_path=chrome_driver_path,options=chrome_options)
    c_driver = webdriver.Chrome(executable_path=chrome_driver_path,options=chrome_options)
    # amazon,driver=search_amazon_product(productname,driver)
    # driver.refresh()
    # driver.get('https://www.google.com/')
    # croma,driver=scrape_product_info(driver,productname)
    # driver.quit()
    # flipkart=search_flipkart_product(productname)
    # print(amazon,croma,flipkart)
    list=[]
    result_container = []
    amazon_thread = threading.Thread(target=search_amazon_product,args=(productname,a_driver,result_container))
    croma_thread = threading.Thread(target=scrape_product_info,args=(c_driver,productname,result_container))
    flipkart_thread = threading.Thread(target=search_flipkart_product,args=(productname,result_container))


    amazon_thread.start()
    croma_thread.start()
    flipkart_thread.start()

    amazon_thread.join()
    croma_thread.join()
    flipkart_thread.join()
    for result in result_container:
        if result['name']=='amazon':
            amazon=result['result']
        elif result['name']=='croma':
            croma=result['result']
        else :
            flipkart=result['result']
    if amazon["price"] is None:
        pass
    else:
        min_set=flipkart
        list.append(amazon)
    if croma["price"] is None:
        pass
    else:
        min_set=flipkart
        list.append(croma)
    if  flipkart["price"] is None:
        pass
    else:
        min_set=flipkart
        list.append(flipkart)
    print(list)
    for item_set in list:
        if item_set["price"]<min_set["price"]:
            min_set=item_set
    if min_set:
        print("Product with minimum price:")
        print(min_set)
    else:
        print("No products found for:", productname)
    return  min_set
    



if __name__== "__main__":
    productname=input("enter product name :")
    yoo=prices(productname)
    print(yoo)


def price_comparator(product,user_id):
    least=prices(product)
    pricecomparator.objects.create(
        user_id=user_id,
        productname=least['name'],
        price=float(least['price']),
        productlink=least['url']
    )
    return least