import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
from time import sleep
import numpy as np
import random

from tqdm import tqdm

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

# constants
from selenium.webdriver.common import action_chains
import random

x = input("Chon che do")

options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
options.add_experimental_option("prefs",prefs)
options.add_argument("start-maximized")
browser = webdriver.Chrome(r'D:\test\chromedriver.exe', options=options)

def wait():
    return sleep(random.randint(4,6))


browser.get("https://www.instagram.com/accounts/login/")
wait()

# login to facebook
id = browser.find_element_by_xpath('//*[@aria-label="Phone number, username, or email"]')
id.send_keys("BotITG12345")
pwd = browser.find_element_by_xpath('//*[@aria-label="Password"]')
pwd.send_keys("Bot123456")
pwd.send_keys(Keys.ENTER)

sleep(3)

        # to clean popups after login
def instagram_auto_comment():
    try:
        browser.find_element_by_xpath("//button[contains(text(),'Save Info')]").click()
    except NoSuchElementException:
        print("no save Info")
    try:
        browser.find_element_by_xpath("//*[contains(@class, 'aOOlW   HoLwm ')]").click()
    except NoSuchElementException:
        print("no notification box")

            # Lấy link bài viết từ file csv
    products_data = pd.read_csv(r'D:\test\In\Link_Post_Instagram.csv')
    for product in tqdm(products_data['Link'].tolist()):
        browser.get(product)
        wait()

        # comment
        browser.find_element_by_xpath('//*[@aria-label="Add a comment…"]').click()
        sleep(1)
        comment_box = browser.find_element_by_xpath('//*[@aria-label="Add a comment…"]')
        sleep(2)
        comment_box.send_keys("Good")
        wait()
        browser.find_element_by_xpath('//*[@data-testid="post-comment-input-button"]').click()
        wait()

                # finally:
                # browser.find_element_by_xpath('//*[@aria-label="Gỡ Thích"]').click()
                # wait()
    browser.quit()

def instagram_auto_follow():
    try:
        browser.find_element_by_xpath("//button[contains(text(),'Save Info')]").click()
    except NoSuchElementException:
        print("no save Info")
    try:
        browser.find_element_by_xpath("//*[contains(@class, 'aOOlW   HoLwm ')]").click()
    except NoSuchElementException:
        print("no notification box")

            # Lấy link bài viết từ file csv
    products_data = pd.read_csv(r'D:\test\In\Link_page_Instagram.csv')
    for product in tqdm(products_data['Link'].tolist()):
        browser.get(product)
                # tìm ô like theo nhãn, tuỳ theo ngôn ngữ mà sẽ khác nhau. Việc tìm nhãn phải làm manual
        try:
            sleep(3)
            browser.find_element_by_xpath('//*[@class="vBF20 _1OSdk"]').click()
        except:
            wait()

                # finally:
                # browser.find_element_by_xpath('//*[@aria-label="Gỡ Thích"]').click()
                # wait()
    sleep(1)
    browser.quit()   

def instagram_auto_unfollow():
    try:
        browser.find_element_by_xpath("//button[contains(text(),'Save Info')]").click()
    except NoSuchElementException:
        print("no save Info")
    try:
        browser.find_element_by_xpath("//*[contains(@class, 'aOOlW   HoLwm ')]").click()
    except NoSuchElementException:
        print("no notification box")

            # Lấy link bài viết từ file csv
    products_data = pd.read_csv(r'D:\test\In\Link_page_Instagram.csv')
    for product in tqdm(products_data['Link'].tolist()):
        browser.get(product)
                # tìm ô like theo nhãn, tuỳ theo ngôn ngữ mà sẽ khác nhau. Việc tìm nhãn phải làm manual

        sleep(3)
        browser.find_element_by_xpath('//*[@class="vBF20 _1OSdk"]').click()
        try:
            sleep(2)
            browser.find_element_by_xpath('//*[@class="aOOlW -Cab_   "]').click()
        except:
            wait()

                # finally:
                # browser.find_element_by_xpath('//*[@aria-label="Gỡ Thích"]').click()
                # wait()
    sleep(1)
    browser.quit()   

def instagram_auto_like():
    try:
        browser.find_element_by_xpath("//button[contains(text(),'Save Info')]").click()
    except NoSuchElementException:
        print("no save Info")
    try:
        browser.find_element_by_xpath("//*[contains(@class, 'aOOlW   HoLwm ')]").click()
    except NoSuchElementException:
        print("no notification box")

            # Lấy link bài viết từ file csv
    products_data = pd.read_csv(r'D:\test\In\Link_Post_Instagram.csv')
    for product in tqdm(products_data['Link'].tolist()):
        browser.get(product)
                # tìm ô like theo nhãn, tuỳ theo ngôn ngữ mà sẽ khác nhau. Việc tìm nhãn phải làm manual
        try:
            sleep(3)
            browser.find_element_by_xpath('//*[@class="fr66n"]').click()
        except:
            wait()

                # finally:
                # browser.find_element_by_xpath('//*[@aria-label="Gỡ Thích"]').click()
                # wait()
    sleep(1)
    browser.quit()

def instagram_auto_unlike():
    try:
        browser.find_element_by_xpath("//button[contains(text(),'Save Info')]").click()
    except NoSuchElementException:
        print("no save Info")
    try:
        browser.find_element_by_xpath("//*[contains(@class, 'aOOlW   HoLwm ')]").click()
    except NoSuchElementException:
        print("no notification box")

            # Lấy link bài viết từ file csv
    products_data = pd.read_csv(r'D:\test\In\Link_Post_Instagram.csv')
    for product in tqdm(products_data['Link'].tolist()):
        browser.get(product)
                # tìm ô like theo nhãn, tuỳ theo ngôn ngữ mà sẽ khác nhau. Việc tìm nhãn phải làm manual
        try:
            sleep(3)
            browser.find_element_by_xpath('//*[@class="fr66n"]').click()
        except:
            wait()

                # finally:
                # browser.find_element_by_xpath('//*[@aria-label="Gỡ Thích"]').click()
                # wait()
    sleep(1)
    browser.quit()
def instagram_auto_post_group():
    try:
        browser.find_element_by_xpath("//button[contains(text(),'Save Info')]").click()
    except NoSuchElementException:
        print("no save Info")
    try:
        browser.find_element_by_xpath("//*[contains(@class, 'aOOlW   HoLwm ')]").click()
    except NoSuchElementException:
        print("no notification box")
    products_data = pd.read_csv(r'D:\test\In\Link_page_Instagram.csv')
    for product in tqdm(products_data['Link'].tolist()):
        browser.get(product)
        wait()

        # comment
        try:
            sleep(1)
            browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[2]/a[1]/span/span').click()
            sleep(1)
            browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div/div[2]').click()
            sleep(1)
            browser.find_element_by_xpath('//*[@aria-label="Add a comment…"]').click()
            sleep(1)
            comment_box = browser.find_element_by_xpath('//*[@aria-label="Add a comment…"]')
            sleep(2)
            #comment_box = browser.find_element_by_xpath('/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea')
            comment_box.send_keys("Good")
            wait()
            browser.find_element_by_xpath('/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/button"]').click()
        except:
            wait()
    wait()
    browser.quit()

if x == 'post':
     instagram_auto_post_group()
if x == 'comment':
    instagram_auto_comment()
if x == 'follow':
    instagram_auto_follow()
if x == 'unfollow':
    instagram_auto_unfollow()
if x == 'like':
    instagram_auto_like()
if x == 'unlike':
    instagram_auto_unlike()