from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

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

# navigate to the target webpage
driver.get("https://httpbin.io/ip")
time.sleep(5)
# print the body content of the target webpage
print(driver.find_element(By.TAG_NAME, "body").text)

# release the resources and close the browser
driver.quit()
