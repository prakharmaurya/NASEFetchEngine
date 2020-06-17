from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json


def get_session_cookies():
    try:
        cookie_dict = json.loads(open('./cookies.txt').read())
    except Exception as e:
        print('Error in cookie reading')
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_driver_path = "./chromedriver.exe"
        driver = webdriver.Chrome(
            chrome_driver_path, chrome_options=chrome_options)
        driver.get('https://www.nseindia.com/')
        cookies = driver.get_cookies()
        cookie_dict = {}
        with open('./cookies.txt', 'w') as line:
            for cookie in cookies:
                cookie_dict[cookie['name']] = cookie['value']
            line.write(json.dumps(cookie_dict))
        driver.quit()
        print('got cookies')
    return cookie_dict
