import requests
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
from configparser import ConfigParser
from .get_cookies import get_session_cookies


def fetch(urls):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.45',
                   'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}

        cookie_dict = get_session_cookies()

        session = requests.session()

        for cookie in cookie_dict:
            if cookie == 'bm_sv':
                session.cookies.set(cookie, cookie_dict[cookie])
        try:
            with open('response_data.json', 'w') as f:
                f.write('{')

            for url in urls:
                res = session.get(url, headers=headers, timeout=20).json()
                with open('response_data.json', 'a') as f:
                    f.write('"' + url.split('=')[1] + '":')
                    f.write(json.dumps(res))
                    if(url != urls[-1]):
                        f.write(',')

            with open('response_data.json', 'a') as f:
                f.write('}')
            print('Data Fetched')

        except Exception as e:
            print('fetch Failed {}'.format(e))
    except Exception as e:
        print('fetcher Error {}'.format(e))
