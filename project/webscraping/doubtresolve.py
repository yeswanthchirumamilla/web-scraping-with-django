
import os
import threading
from collections import Counter
from requests_html import HTMLSession
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from transformers import BartTokenizer, BartForConditionalGeneration
import torch
from .models import * 



def bart_extractive_summarization(text, max_length=1024, min_length=56, num_beams=4, length_penalty=2.0, early_stopping=True):
    tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
    model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')

    inputs = tokenizer(text, return_tensors='pt', max_length=max_length, truncation=True, padding=True)
    with torch.no_grad():
        outputs = model.generate(input_ids=inputs.input_ids, attention_mask=inputs.attention_mask, max_length=max_length, 
                                 min_length=min_length, num_beams=num_beams, length_penalty=length_penalty, 
                                 early_stopping=early_stopping)

    summary = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return summary

def scrape_wikipedia_info(url, driver, retry_count=5):
    try:
        driver.get(url)
        time.sleep(5)

        elements = driver.find_elements(By.XPATH, "//p")
        info_text = "\n".join([element.text for element in elements])
        info_text = info_text.strip()

        return info_text
    except Exception as e:
        if "captcha" in driver.page_source.lower() and retry_count > 0:
            print("CAPTCHA detected. Retrying...")
            time.sleep(5)
            driver.back()
            driver.refresh()
            return scrape_wikipedia_info(url, driver, retry_count - 1)
        else:
            print(f"Error: {e}")
            return None


def scrape_w3schools_info(url, driver, retry_count=5):
    try:
        driver.get(url)
        time.sleep(5)

        elements = driver.find_elements(By.XPATH, "//p")
        info_text = "\n".join([element.text for element in elements])
        info_text = info_text.strip()

        return info_text
    except Exception as e:
        if "captcha" in driver.page_source.lower() and retry_count > 0:
            print("CAPTCHA detected. Retrying...")
            time.sleep(5)
            driver.back()
            driver.refresh()
            return scrape_w3schools_info(url, driver, retry_count - 1)
        else:
            print(f"Error on W3Schools: {e}")
            return None

def scrape_tutorialspoint_info(url, driver, retry_count=5):
    try:
        driver.get(url)
        time.sleep(5)

        elements = driver.find_elements(By.XPATH, "//p")
        info_text = "\n".join([element.text for element in elements])
        info_text = info_text.strip()

        return info_text
    except Exception as e:
        if "captcha" in driver.page_source.lower() and retry_count > 0:
            print("CAPTCHA detected. Retrying...")
            time.sleep(5)
            driver.back()
            driver.refresh()
            return scrape_tutorialspoint_info(url, driver, retry_count - 1)
        else:
            print(f"Error on Tutorialspoint: {e}")
            return None


def scrape_programiz_info(url, driver, retry_count=5):
    try:
        driver.get(url)
        time.sleep(5)

        elements = driver.find_elements(By.XPATH, "//p")
        info_text = "\n".join([element.text for element in elements])
        info_text = info_text.strip()

        return info_text
    except Exception as e:
        if "captcha" in driver.page_source.lower() and retry_count > 0:
            print("CAPTCHA detected. Retrying...")
            time.sleep(5)
            driver.back()
            driver.refresh()
            return scrape_programiz_info(url, driver, retry_count - 1)
        else:
            print(f"Error on Programiz: {e}")
            return None


def scrape_geeksforgeeks_info(url, driver, retry_count=5):
    try:
        driver.get(url)
        time.sleep(5)

        elements = driver.find_elements(By.XPATH, "//p[not(ancestor::*[contains(@class, 'comment')])]")

        info_text = "\n".join([element.text for element in elements])
        info_text = info_text.strip()

        return info_text
    except Exception as e:
        if "captcha" in driver.page_source.lower() and retry_count > 0:
            print("CAPTCHA detected. Retrying...")
            time.sleep(5)
            driver.back()
            driver.refresh()
            return scrape_geeksforgeeks_info(url, driver, retry_count - 1)
        else:
            print(f"Error on Geeksforgeeks: {e}")
            return None


def scrape_byjus_info(url, driver, retry_count=5):
    try:
        driver.get(url)
        time.sleep(5)

        elements = driver.find_elements(By.XPATH, "//p[not(ancestor::*[contains(@class, 'comment')])]")

        info_text = "\n".join([element.text for element in elements])
        info_text = info_text.strip()

        return info_text
    except Exception as e:
        if "captcha" in driver.page_source.lower() and retry_count > 0:
            print("CAPTCHA detected. Retrying...")
            time.sleep(5)
            driver.back()
            driver.refresh()
            return scrape_byjus_info(url, driver, retry_count - 1)
        else:
            print(f"Error on Byjus: {e}")
            return None

def scrape_javatpoint_info(url, driver, retry_count=5):
    try:
        driver.get(url)
        time.sleep(5)

        elements = driver.find_elements(By.XPATH, "//p ")

        info_text = "\n".join([element.text for element in elements])
        info_text = info_text.strip()

        return info_text
    except Exception as e:
        if "captcha" in driver.page_source.lower() and retry_count > 0:
            print("CAPTCHA detected. Retrying...")
            time.sleep(5)
            driver.back()
            driver.refresh()
            return scrape_javatpoint_info(url, driver, retry_count - 1)
        else:
            print(f"Error on Javatpoint: {e}")
            return None


def scrape_website(url,driver):
    if 'wikipedia.org' in url:
        return scrape_wikipedia_info(url,driver)
    elif 'w3schools.com' in url:
        return scrape_w3schools_info(url,driver)
    elif 'geeksforgeeks.org' in url:
        return scrape_geeksforgeeks_info(url,driver)
    elif 'byjus.com' in url:
        return scrape_byjus_info(url,driver)
    elif 'javatpoint.com' in url:
        return scrape_javatpoint_info(url,driver)
    elif 'tutorialspoint.com' in url:
        return scrape_tutorialspoint_info(url,driver)
    elif 'programiz.com' in url:
        return scrape_programiz_info(url,driver)

def search_and_scrape(search_engine, query, limit, count=0):
    session = HTMLSession()

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }

    params = {'q': query, 'num': limit}
    if search_engine == 'google':
        response = session.get('https://www.google.com/search', params=params, headers=headers)
    elif search_engine == 'duckduckgo':
        response = session.get('https://duckduckgo.com/html/', params={'q': query})
    elif search_engine == 'bing':
        response = session.get('https://www.bing.com/search', params=params, headers=headers)
        
    if 'did not match any documents' in response.text:
        print(f'No Results Found on {search_engine.capitalize()}')
        return []
    elif 'Our systems have detected unusual traffic from your computer' in response.text and count < 5 and search_engine == 'google':
        print(f'Captcha Triggered on {search_engine.capitalize()}!\nUse VPN or Try After Sometime.')
        return search_and_scrape(search_engine, query, limit, count+1)
    elif 'Our systems have detected unusual traffic from your computer' in response.text and count == 5 and search_engine == 'google':
        try:
            chrome_options.add_argument("--headless")
            driver = webdriver.Chrome(options=chrome_options, executable_path="C:/Users/yaswa/Downloads/FlipKart_Selenium-main/chromedriver.exe")
            driver.get("https://www.google.com/search?q={query}")
            results = driver.find_elements(By.CSS_SELECTOR, "div.g")
            return results
        except Exception as e:
            return []
    else:
        chrome_options = Options()
        links = list(set(response.html.absolute_links))
        print(links)
        results = []
        for url in links[:]:
            if any(site in url for site in ['geeksforgeeks.org', 'wikipedia.org', 'byjus.com', 'w3schools.com', 'tutorialspoint.com', 'programiz.com', 'javatpoint.com']):
                results.append(url)
        print(results)
        return results

    session.close()

def scrape_and_summarize(url,  result_container):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options, executable_path="C:/Users/yaswa/Downloads/FlipKart_Selenium-main/chromedriver.exe")
    scraped_text = scrape_website(url, driver)
    if scraped_text:
        summarized_text = bart_extractive_summarization(scraped_text)
        result_container.append((url, summarized_text))

def doubtscrape(query, User_id):
    os.system('cls' if os.name == 'nt' else 'clear')

    limit = 10  

    all_links = []

    for search_engine in ['google', 'duckduckgo', 'bing']:
        links = search_and_scrape(search_engine, query, limit)
        all_links.extend(links)
        
    link_counts = Counter(all_links)
    top_links = link_counts.most_common(3)
    print(top_links)

    top_3_urls = [link for link, _ in top_links]
    
    results = []

    

    threads = []
    result_container = []
    for url in top_3_urls:
        thread = threading.Thread(target=scrape_and_summarize, args=(url, result_container))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    for url, summary in result_container:
        results.append((url, summary))
        print("URL:", url)
        print("Summary:", summary)
        print()

    while len(results) < 3:
        results.append((None, None))

    urls = [url for url, _ in results]
    summaries = [summary for _, summary in results]

    doubtResolve.objects.create(
        doubt=query,
        user_id=User_id,
        url1=urls[0],
        url2=urls[1],
        url3=urls[2],
        answer1=summaries[0],
        answer2=summaries[1],
        answer3=summaries[2]
    )
    return {"urls": urls, "summaries": summaries}