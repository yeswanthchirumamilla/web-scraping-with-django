import time
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from .models import *
import random

user_agent_list = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
]
def get_movie_info(movie_name, User_id):
    chrome_driver_path = "C:/Users/yaswa/Downloads/FlipKart_Selenium-main/chromedriver.exe"
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument(f"user-agent={random.choice(user_agent_list)}")

    # Initialize Chrome driver with the specified path
    driver = webdriver.Chrome(chrome_driver_path, options=chrome_options)
    ans = get_movie_infon(movie_name, driver, User_id)
    driver.quit()  
    return ans

def get_movie_infon(movie_name, driver, User_id):
    try:
        search_url = f"https://www.google.com/search?q={movie_name}+imdb"

        for i in range (0,5):
            try:
                driver.get(search_url)
                time.sleep(5)  
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.g")))
                break

            except Exception as e:
                print(e)

        print(driver.current_url)

        
        first_result_link = driver.find_element(By.CSS_SELECTOR, "div.g a")
        first_result_link.click()
        print("hi")
        print(driver.current_url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "hero__primary-text")))
        html_content = driver.page_source
        
        
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        prettified_html=soup.prettify()
#         file_path = "prettified_yhtml.txt"

# # Open the file in write mode and save the prettified HTML content

#         with open(file_path, "w", encoding="utf-8") as file:
#             file.write(prettified_html)

        # Extract movie name
        # movie_name = soup.find('title').text.strip().split(' - IMDb')[0]
        # print(movie_name)
        # # Extract movie rating
        rating = soup.find('meta', property='og:title')['content'].split(' | ')[0]
        rating = float(rating[-3:])
        # print(rating)
        # print("hi")
        # Extract movie summary
        # summary_span = soup.find('meta', {'name': 'description'})['content']
        # print(summary_span)
        script_tag = soup.find('script', type='application/ld+json')
        json_content = json.loads(script_tag.string)
        movie_name = json_content['name']
        #rating = json_content['review']['reviewRating']['ratingValue']
        movie_description = json_content['description']
        
        summary = movie_description.strip()

        movie.objects.create(
            title=movie_name, 
            rating=rating,
            summary=summary,
            user_id=User_id
        )
        return {"Movie_Name": movie_name, "Rating": rating, "Summary": summary}

    except Exception as e:
        print("Error:", e)
        return {"Error": str(e)}





def get_actor_filmography(actor_name):
    chrome_driver_path = "C:/Users/yaswa/Downloads/FlipKart_Selenium-main/chromedriver.exe"
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

    try:
        search_url = f"https://www.google.com/search?q={actor_name}+filmography+site:wikipedia.org"
        for i in range (0,5):
            try:
                driver.get(search_url)
                time.sleep(5)  
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.g")))
                break
            except Exception as e:

                print(e)
                time.sleep(5)
                driver.back()
                driver.refresh()
        print(driver.current_url)
        

        search_results = driver.find_elements(By.CSS_SELECTOR, "div.g")

        for link in search_results:
            if "recaptcha" in str(link):
                print("CAPTCHA detected. Retrying...")
                return get_actor_filmography(actor_name)

        for result in search_results:
            link = result.find_element(By.CSS_SELECTOR, "a")
            if "wikipedia.org" in link.get_attribute("href"):
                link.click()
                time.sleep(5)
                print("Navigated to Wikipedia page.")
                tables = driver.find_elements(By.XPATH, "//table[contains(@class, 'wikitable ')]")
                movies = []
                for table in tables:
                    rows = table.find_elements(By.TAG_NAME, "tr")
                    for row in rows[1:]:  
                        try:
                            cell = row.find_element(By.TAG_NAME, 'i')
                            movie_title = cell.text
                            movies.append(movie_title)
                        except Exception as e:
                            pass
                return movies


    
    except Exception as e:
        print("Error:", e)

    finally:
        driver.quit()