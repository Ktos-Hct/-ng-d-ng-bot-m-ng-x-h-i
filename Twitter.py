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

x = input("bạn muốn chạy : ")

options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
options.add_experimental_option("prefs",prefs)
options.add_argument("start-maximized")
browser = webdriver.Chrome(r'D:\test\chromedriver.exe', options=options)

def wait():
    return sleep(random.randint(4,6))
def login():
    browser.get("https://twitter.com/i/flow/login?input_flow_data=%7B%22requested_variant%22%3A%22eyJsYW5nIjoidmkifQ%3D%3D%22%7D")
    wait()
    wait()
    id = browser.find_element_by_xpath('//*[@autocomplete="username"]')
    id.send_keys("phcuoc_19pm@student.agu.edu.vn")
    sleep(2)
    browser.find_element_by_xpath('//*[@style="color: rgb(255, 255, 255);"]').click()
    sleep(2)
    try:
        pwd = browser.find_element_by_xpath('//*[@name="text"]')
        pwd.send_keys("@PhanCuoc")
        sleep(1)
    except:
        pass
    browser.find_element_by_xpath('//*[@style="color: rgb(255, 255, 255);"]').click()
    sleep(2)
    pwd = browser.find_element_by_xpath('//*[@name="password"]')
    pwd.send_keys("jack2806")
    browser.find_element_by_xpath('//*[@data-testid="LoginForm_Login_Button"]').click()
    sleep(3)
def twitter_auto_post():
    browser.find_element_by_xpath('//*[@data-testid="tweetTextarea_0"]').click()
    try:
        sleep(1)
        comment_box = browser.find_element_by_xpath('//*[@data-testid="tweetTextarea_0"]')
        sleep(2)
        comment_box.send_keys("I'm Here")
        wait()
        browser.find_element_by_xpath('//*[@data-testid="tweetButtonInline"]').click()
        wait()
    except:
        wait()
    sleep(1)
    browser.quit()

def twitter_auto_comment():
    products_data = pd.read_csv(r'D:\test\TW\Link_post.csv')
    for product in tqdm(products_data['Link'].tolist()):
        browser.get(product)
        sleep(3)
        browser.find_element_by_xpath('//*[@aria-label="Reply"]').click()
        try:
            sleep(1)
            comment_box = browser.find_element_by_xpath('//*[@aria-label="Tweet text"]')
            sleep(2)
            comment_box.send_keys("Good")
            wait()
            browser.find_element_by_xpath('//*[@data-testid="tweetButton"]').click()
            wait()
        except:
            wait()
    sleep(1)
    browser.quit()


def twitter_auto_follow():
    products_data = pd.read_csv(r'D:\test\TW\Link_page.csv')
    for product in tqdm(products_data['Link'].tolist()):
        browser.get(product)
        sleep(3)
        browser.find_element_by_xpath('//*[@style="background-color: rgb(15, 20, 25);"]').click()
        sleep(3)
    sleep(1)
    browser.quit()


def twitter_auto_unfollow():
    products_data = pd.read_csv(r'D:\test\TW\Link_page.csv')
    for product in tqdm(products_data['Link'].tolist()):
        browser.get(product)
        sleep(3)
        browser.find_element_by_xpath('//*[@data-testid="placementTracking"]').click()
        sleep(1)
        browser.find_element_by_xpath('//*[@data-testid="confirmationSheetConfirm"]').click()
    sleep(2)
    browser.quit()

def twitter_auto_like():
    products_data = pd.read_csv(r'D:\test\TW\Link_post.csv')
    for product in tqdm(products_data['Link'].tolist()):
        browser.get(product)
        try:
            sleep(3)
            browser.find_element_by_xpath('//*[@data-testid="like"]').click()
        except:
            wait()
    sleep(1)
    browser.quit()


def twitter_auto_unlike():
    products_data = pd.read_csv(r'C:\Users\Window 10\Desktop\Source\Source\Twitter_scrapy\Twitter_scrapy\Link_post.csv')
    for product in tqdm(products_data['Link'].tolist()):
        browser.get(product)
        try:
            sleep(3)
            browser.find_element_by_xpath('//*[@data-testid="like"]').click()
        except:
            wait()
    sleep(1)
    browser.quit()

def twitter_auto_hashtag():
    products_data = pd.read_csv(r'D:\test\TW\Link_hashtag.csv')
    for product in tqdm(products_data['Link'].tolist()):
        browser.get(product)
        try:
            sleep(3)
            browser.find_element_by_xpath('//*[@data-testid="like"]').click()
        except:
            wait()
    sleep(1)
    browser.quit()
try:
    login()
except:
    login()
if x == 'post':
    twitter_auto_post()
if x == 'comment':
    twitter_auto_comment()
if x == 'follow':
    twitter_auto_follow()
if x == 'unfollow':
    twitter_auto_unfollow()
if x == 'like':
    twitter_auto_like()
if x == 'unlike':
    twitter_auto_unlike()
if x == 'hashtag':
    twitter_auto_hashtag()
