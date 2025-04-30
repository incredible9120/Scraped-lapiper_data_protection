from selenium import webdriver
from RecaptchaSolver import RecaptchaSolver
import time
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import csv
from requests_html import HTMLSession
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import random
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service as ChromeService
import zipfile
# from webdriver_manager.chrome import ChromeDriverManager

options = Options()

# Proxy details

proxy_host = "res.proxy-seller.com"
proxy_port = "10000"
proxy_user = "5f88d977c59b8866"
proxy_pass = "RNW78Fm5"

# 🔨 Create the extension files
plugin_path = 'proxy_auth_plugin.zip'

manifest_json = """
{
    "version": "1.0.0",
    "manifest_version": 2,
    "name": "Proxy Auth Extension",
    "permissions": [
        "proxy",
        "tabs",
        "unlimitedStorage",
        "storage",
        "<all_urls>",
        "webRequest",
        "webRequestBlocking"
    ],
    "background": {
        "scripts": ["background.js"]
    }
}
"""

background_js = f"""
var config = {{
    mode: "fixed_servers",
    rules: {{
        singleProxy: {{
            scheme: "http",
            host: "{proxy_host}",
            port: parseInt({proxy_port})
        }},
        bypassList: ["localhost"]
    }}
}};

chrome.proxy.settings.set({{value: config, scope: "regular"}}, function() {{}});

chrome.webRequest.onAuthRequired.addListener(
    function(details, callbackFn) {{
        callbackFn({{
            authCredentials: {{
                username: "{proxy_user}",
                password: "{proxy_pass}"
            }}
        }});
    }},
    {{urls: ["<all_urls>"]}},
    ['blocking']
);
"""

with zipfile.ZipFile(plugin_path, 'w') as zp:
    zp.writestr("manifest.json", manifest_json)
    zp.writestr("background.js", background_js)

# 🚀 Launch Chrome with extension
options = Options()
options.add_extension(plugin_path)

# proxy_server_url = "http://5f88d977c59b8866:RNW78Fm5@res.proxy-seller.com:10000"
# print(proxy_server_url)
# options.add_argument('--proxy-server=http://5f88d977c59b8866:RNW78Fm5@res.proxy-seller.com:10000')

# options.add_argument("--no-sandbox")
# options.add_argument("--disable-blink-features=AutomationControlled")
# # Initialize the WebDriver options
# options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--no-sandbox")
# # options.add_argument('--no-proxy-server')
# options.add_argument("--log-level=3")
# options.add_argument("--incognito")

# options.add_argument("--headless")  # Run headlessly if needed
# options.add_argument("--disable-gpu")  # Disable GPU acceleration
# options.add_argument("start-maximized")
# options.add_argument("disable-infobars")
# options.add_argument("--disable-extensions")


# options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
# options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(
    # service=ChromeService(ChromeDriverManager().install()),
    options=options
)
# driver.get("https://ipinfo.io/json")
driver.get("https://www.dlapiperdataprotection.com/?c=AL&c=DZ&c=AO&c=AR&c=AM&c=AW&c=AU&c=AT&c=AZ&c=BS&c=BH&c=BD&c=BB&c=BY&c=BE&c=BJ&c=BM&c=BO&c=BQ&c=BA&c=BW&c=BR&c=VG&c=BN&c=BG&c=BF&c=BI&c=KH&c=CM&c=CA&c=CV&c=KY&c=TD&c=CL&c=CN&c=CO&c=CI&c=CR&c=HR&c=CU&c=CW&c=CY&c=CZ&c=CD&c=DK&c=DO&c=EC&c=EG&c=SV&c=GQ&c=EE&c=ET&c=FM&c=FJ&c=FI&c=FR&c=GA&c=GE&c=DE&c=GH&c=GI&c=GR&c=GT&c=GG&c=GN&c=HT&c=HN&c=HK&c=HU&c=IS&c=IN&c=ID&c=IR&c=IE&c=IL&c=IT&c=JP&c=JE&c=JO&c=KZ&c=KE&c=XK&c=KW&c=KG&c=LA&c=LV&c=LB&c=LS&c=LR&c=LY&c=LT&c=LU&c=MO&c=MG&c=MY&c=MT&c=MU&c=MX&c=MD&c=MC&c=MN&c=ME&c=MA&c=MZ&c=MM&c=NA&c=NP&c=NL&c=NZ&c=NI&c=NE&c=NG&c=MK&c=NO&c=PK&c=PA&c=PY&c=PE&c=PH&c=PL&c=PT&c=QA&c=QA2&c=CG&c=RO&c=RU&c=RW&c=SA&c=SN&c=RS&c=SC&c=SG&c=SX&c=SK&c=SI&c=ZA&c=KR&c=ES&c=LK&c=SE&c=CH&c=TW&c=TJ&c=TZ&c=TH&c=TO&c=TT&c=TN&c=TR&c=TM&c=AE4&c=AE2&c=AE3&c=AE&c=UG&c=UA&c=GB&c=US&c=UY&c=UZ&c=VE&c=VN&c=ZM&c=ZW")
time.sleep(random.uniform(0.5, 1))
# driver.get("https://www.dlapiperdataprotection.com")
# recaptchaSolver = RecaptchaSolver(driver)

try:
    # Perform CAPTCHA solving
    t0 = time.time()
    # driver.find_element(By.ID, "subACK").click()
    # driver.find_element(By.NAME, "submit").click()
    
    # recaptchaSolver.solveCaptcha()
    # time.sleep(random.uniform(100, 100))
    # driver.find_element(By.NAME, "patient-powered-search-input").send_keys('Dentist')
    # driver.find_element(By.NAME, "maxResult").clear()
    # driver.find_element(By.NAME, "maxResult").send_keys('100')
    # driver.find_element(By.CLASS_NAME, "sc-w1fnvw-5 SDjDR").click()
    print(f"Time to solve the captcha: {time.time() - t0:.2f} seconds")
    
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
        btn_txt.replace("Data protection laws in ", "")
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