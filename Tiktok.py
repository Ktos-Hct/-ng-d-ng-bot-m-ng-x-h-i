import csv
import json
from tqdm import tqdm
import csvfile as csvfile
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
from time import sleep
import pandas as pd
import numpy as np
import random
x=input("Ban muon chay: ")
options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
options.add_experimental_option("prefs",prefs)
options.add_argument("start-maximized")
browser = webdriver.Chrome(r'D:\test\chromedriver.exe', options=options)
def wait():
    return sleep(random.randint(4,6))


browser.get("https://www.tiktok.com/login/")
wait()
browser.find_element_by_xpath('//div[@class="social-container-NE2xk"]/div[3]').click()
# login to facebook
root = browser.window_handles[0]
browser.switch_to.window(browser.window_handles[1])
id = browser.find_element_by_xpath('//*[@id="email"]')
id.send_keys("zetabase3i@gmail.com")
pwd = browser.find_element_by_xpath('//*[@id="pass"]')
pwd.send_keys("Langnghiem@79")
pwd.send_keys(Keys.ENTER)
browser.switch_to.window(root)
wait()
wait()
def tiktok_auto_comment():
    pass
def tiktok_auto_follow():
    products_data = pd.read_csv(r'D:\test\Tik\Page_link.csv')
    for product in tqdm(products_data['Link'].tolist()):
        browser.get(product)
        wait()
        try:
            sleep(2)
            browser.find_element_by_xpath('//*[@data-e2e="follow-buttonn"]').click()
        except:
            wait()


    sleep(1)
    browser.quit()
    pass
def tiktok_auto_like():
    pass
def tiktok_auto_unlike():
    pass
if x == 'comment':
    tiktok_auto_comment()
if x == 'follow':
    tiktok_auto_follow()
if x == 'unfollow':
    tiktok_auto_unfollow()
if x == 'like':
    tiktok_auto_like()
if x == 'unlike':
    tiktok_auto_unlike()
