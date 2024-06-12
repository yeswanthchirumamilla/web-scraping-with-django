
from .models import *
from django.db.models import Max

    
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random


USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
]

def get_weather_info(city,user_name):
    chrome_driver_path = "C:/Users/yaswa/Downloads/FlipKart_Selenium-main/chromedriver.exe"
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument(f"user-agent={random.choice(USER_AGENTS)}")
    driver=webdriver.Chrome(executable_path="C:/Users/yaswa/Downloads/FlipKart_Selenium-main/chromedriver.exe",options=chrome_options)
    WebDriverWait(driver, 10)
    
    for i in range(0,5):
        try :
            search_url = f"https://www.google.com/search?q=wheatherat+{city}+10daysforcastaccweather"
            driver.get(search_url)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.g")))
            search_results = driver.find_elements(By.CSS_SELECTOR, "div.g")
            break
        except Exception as e:
            print(e)
            driver.back()
            driver.refresh()
            time.sleep(5)
            driver.refresh()
    for result in search_results:
        link = result.find_element(By.CSS_SELECTOR, "a")
        if "accuweather.com" in link.get_attribute("href"):
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.g a"))).click()
            break
    WebDriverWait(driver, 10)
    try:
        elements = driver.find_elements(By.CLASS_NAME, "daily-list-body")
        info = "\n".join([element.text for element in elements])
        info.strip()
        if info is None:
            return None
        
        lines = info.split('\n')
        print(lines)
        j=2
        for i in range (3,8):
            if lines[i].strip()[-1:] =="%":
                j=i-3
                break
    except Exception as e:
        print(e)
        elements = driver.find_elements(By.CLASS_NAME, "daily-wrapper")
        info = "\n".join([element.text for element in elements])
        info.strip()
        if info is None:
            return None
        
        lines = info.split('\n')
        print(lines)
        j=2
        for i in range (3,8):
            if lines[i].strip()[-1:] =="%":
                j=i-3
                break

    today_temp = int(lines[j][:-1])
    dates = []
    high_temps = []
    low_temps = []
    weather_info=[]
    try:
        for j in range(0, 9):
            i = 7 * j + 7
            for m in range(0,7):
                print(lines[i].strip()[-1:] )
                if lines[i].strip()[-1:] =="%":
                    break
                else:
                    i-=1
            date = str(lines[i + 2].strip())
            high_temp = int(lines[i + 3][:-1])  
            low_temp = int(lines[i + 4][:-1])   
    
            
            date_obj = datetime.strptime(date, "%m/%d")
            date_obj = date_obj.replace(year=datetime.now().year)
    
            dates.append(date_obj)
            high_temps.append(high_temp)
            low_temps.append(low_temp)
            
            weather_info.append({
                'date': date_obj,
                'hightemperature': high_temp,
                'lowtemperature': low_temp,
    
            })
    except Exception as e:
        for k in range(0, 9):
            i = 7 * k + 6
            for m in range(0,7):
                print(lines[i].strip()[-1:] )
                if lines[i].strip()[-1:] =="%":
                    break
                else:
                    i-=1

            date = str(lines[i + 1].strip())
            high_temp = int(lines[i + 2][:-1])  
            low_temp = int(lines[i + 3][:-1])   
    
            
            date_obj = datetime.strptime(date, "%m/%d")
            date_obj = date_obj.replace(year=datetime.now().year)
    
            dates.append(date_obj)
            high_temps.append(high_temp)
            low_temps.append(low_temp)
            
            weather_info.append({
                'date': date_obj,
                'hightemperature': high_temp,
                'lowtemperature': low_temp,
    
            })

    print(weather_info)
    max_search_id = Weather.objects.aggregate(Max('Weather_search_id'))['Weather_search_id__max']
    new_search_id=max_search_id+1
    driver.quit()
    Weather.objects.create(
        user_id=user_name,
        location=city,
        Weather_search_id=new_search_id,
        date1=datetime.now().date(),
        temp1=today_temp,
        date2=dates[0].date(),
        hightemp2=high_temps[0],
        lowtemp2=low_temps[0],
        date3=dates[1].date(),
        hightemp3=high_temps[1],
        lowtemp3=low_temps[1],
        date4=dates[2].date(),
        hightemp4=high_temps[2],
        lowtemp4=low_temps[2],
        date5=dates[3].date(),
        hightemp5=high_temps[3],
        lowtemp5=low_temps[3],
        date6=dates[4].date(),
        hightemp6=high_temps[4],
        lowtemp6=low_temps[4],
        date7=dates[5].date(),
        hightemp7=high_temps[5],
        lowtemp7=low_temps[5],
        date8=dates[6].date(),
        hightemp8=high_temps[6],
        lowtemp8=low_temps[7],
        date9=dates[7].date(),
        hightemp9=high_temps[7],
        lowtemp9=low_temps[7],
        date10=dates[8].date(),
        hightemp10=high_temps[8],
        lowtemp10=low_temps[8]
    )
    return today_temp, weather_info