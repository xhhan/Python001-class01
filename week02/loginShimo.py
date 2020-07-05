#-*-coding:utf-8-*-

import requests
import time
from selenium import webdriver

def login_shimo(username, passwd):
    login_url = 'https://shimo.im/lizard-api/auth/password/login'
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    try:
        browser = webdriver.Chrome()
        # 需要安装chrome driver, 和浏览器版本保持一致
        # http://chromedriver.storage.googleapis.com/index.html

        browser.get('https://shimo.im')
        time.sleep(1)

        btm1 = browser.find_element_by_xpath('//*[@id="homepage-header"]/nav/div[3]/a[2]/button')
        btm1.click()

        browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input').\
            send_keys(username)
        browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input').\
            send_keys(passwd)
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button').click()
        cookies = browser.get_cookies()  # 获取cookies
        print(cookies)

    except Exception as e:
        print(e)
    finally:
        pass
        #browser.close()



if __name__=='__main__':
    username = 'xxx'
    passwd = 'xxx'
    login_shimo(username,passwd)