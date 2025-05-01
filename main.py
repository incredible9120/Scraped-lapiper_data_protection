from selenium import webdriver
from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from requests_html import HTMLSession
from RecaptchaSolver import RecaptchaSolver
from bs4 import BeautifulSoup

import time
import requests
import csv
import random
import zipfile
import base64
# from webdriver_manager.chrome import ChromeDriverManager

# configure the proxy
proxy_username = "5f88d977c59b8866"
proxy_password = "RNW78Fm5"
proxy_address = "res.proxy-seller.com"
proxy_port = "10000"

# formulate the proxy url with authentication
proxy_url = f"http://{proxy_username}:{proxy_password}@{proxy_address}:{proxy_port}"

# set selenium-wire options to use the proxy
seleniumwire_options = {
    "proxy": {"http": proxy_url, "https": proxy_url},
}

# set Chrome options to run in headless mode
options = Options()
# options.add_argument("--headless=new")

# initialize the Chrome driver with service, selenium-wire options, and chrome options
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    seleniumwire_options=seleniumwire_options,
    options=options,
)

driver.get("https://www.dlapiperdataprotection.com/?c=AL&c=DZ&c=AO&c=AR&c=AM&c=AW&c=AU&c=AT&c=AZ&c=BS&c=BH&c=BD&c=BB&c=BY&c=BE&c=BJ&c=BM&c=BO&c=BQ&c=BA&c=BW&c=BR&c=VG&c=BN&c=BG&c=BF&c=BI&c=KH&c=CM&c=CA&c=CV&c=KY&c=TD&c=CL&c=CN&c=CO&c=CI&c=CR&c=HR&c=CU&c=CW&c=CY&c=CZ&c=CD&c=DK&c=DO&c=EC&c=EG&c=SV&c=GQ&c=EE&c=ET&c=FM&c=FJ&c=FI&c=FR&c=GA&c=GE&c=DE&c=GH&c=GI&c=GR&c=GT&c=GG&c=GN&c=HT&c=HN&c=HK&c=HU&c=IS&c=IN&c=ID&c=IR&c=IE&c=IL&c=IT&c=JP&c=JE&c=JO&c=KZ&c=KE&c=XK&c=KW&c=KG&c=LA&c=LV&c=LB&c=LS&c=LR&c=LY&c=LT&c=LU&c=MO&c=MG&c=MY&c=MT&c=MU&c=MX&c=MD&c=MC&c=MN&c=ME&c=MA&c=MZ&c=MM&c=NA&c=NP&c=NL&c=NZ&c=NI&c=NE&c=NG&c=MK&c=NO&c=PK&c=PA&c=PY&c=PE&c=PH&c=PL&c=PT&c=QA&c=QA2&c=CG&c=RO&c=RU&c=RW&c=SA&c=SN&c=RS&c=SC&c=SG&c=SX&c=SK&c=SI&c=ZA&c=KR&c=ES&c=LK&c=SE&c=CH&c=TW&c=TJ&c=TZ&c=TH&c=TO&c=TT&c=TN&c=TR&c=TM&c=AE4&c=AE2&c=AE3&c=AE&c=UG&c=UA&c=GB&c=US&c=UY&c=UZ&c=VE&c=VN&c=ZM&c=ZW")

try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'single-accordion--desktop'))
    )
    soup = BeautifulSoup(driver.page_source, "html.parser")
    laws = soup.find_all("div", class_= "single-accordion--detailed")
    
    header_text = []
    header_text.append("Country")
    header_text.append("Details")
    
    # init row text array
    row_text_array = []

    # loop through rows and add row text to array
    for row in laws[0:]:
        row_text = []
        
        button = row.find('button')
        btn_txt = button.text
        btn_txt.replace("Data protection laws in", "")
        row_text.append(btn_txt)
        row_text.append(row.get_text())
        
        row_text_array.append(row_text)

    with open("out.csv", "w") as f:
        wr = csv.writer(f)
        wr.writerow(header_text)
        for row_text_single in row_text_array:
            wr.writerow(row_text_single) 
        
except Exception as e:
    print(f"An error occurred: {e}")
    driver.quit()