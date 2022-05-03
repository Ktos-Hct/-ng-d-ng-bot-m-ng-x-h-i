import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
from time import sleep
import numpy as np

import random

from tqdm import tqdm


x = input("bạn muốn chạy : ")


options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
options.add_experimental_option("prefs",prefs)
options.add_argument("start-maximized")
browser = webdriver.Chrome(r'D:\test\chromedriver.exe')

def wait():
    return sleep(random.randint(5,8))


browser.get("https://www.facebook.com")
wait()

# login to facebook
id = browser.find_element_by_xpath('//*[@id="email"]')
id.send_keys("0913403384")
pwd = browser.find_element_by_xpath('//*[@id="pass"]')
pwd.send_keys("hackerone1a")
pwd.send_keys(Keys.ENTER)

sleep(3)

#facebook_auto_post_group
def facebook_auto_post_group():
    products_data = pd.read_csv(r'D:\test\Fb\group_links.csv')
    for product in tqdm(products_data['Link'].tolist()):
        browser.get(product)
        wait()

            # lấy dữ liệu từ page source để xử lý
        page_source = browser.page_source
        soup = bs(page_source, 'lxml')

            # tìm vị trí của box post bài
            # tuỳ vào ngôn ngữ mà text có thể khác nhau, việc lấy text phải làm manual
        browser.find_element_by_xpath('/html/body/div/div/div/div/div[3]/div/div/div/div/div[4]/div/div/div/div/div/div/div/div/div/div/div').click()

        sleep(1)

    # browser.find_element_by_xpath('/html/body/div/div/div/div/div[4]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div').click()
        bd = browser.find_element_by_xpath('//*[@aria-label="Tạo bài viết công khai..."]')
        bd.send_keys("Hello, im new here")
        sleep(1)
        bt = browser.find_element_by_xpath('//*[@aria-label="Đăng"]')
        bt.click()
        sleep(10)
    browser.quit()

#facebook_auto_comment
def facebook_auto_comment():
    # Lấy link bài viết từ file csv
    products_data = pd.read_csv(r'D:\test\Fb\post_link.csv')
    for product in tqdm(products_data['Link'].tolist()):
        browser.get(product)
        wait()

        # comment
        browser.find_element_by_xpath('//*[@aria-label="Viết bình luận"]').click()

        sleep(2)
        comment_box = browser.find_element_by_xpath(('//*[@class="hcukyx3x oygrvhab cxmmr5t8 kvgmc6g5"]'))
        comment_box.send_keys("Good job")
        wait()
        comment_box.send_keys(Keys.ENTER)
        wait()

    wait()
    browser.quit()


#facebook_auto_follow
def facebook_auto_follow():
    products_data = pd.read_csv('D:\test\Fb\Page_link.csv')
    for product in tqdm(products_data['Link'].tolist()):
        browser.get(product)
        wait()

        # tìm ô like theo nhãn, tuỳ theo ngôn ngữ mà sẽ khác nhau. Việc tìm nhãn phải làm manual
        browser.find_element_by_xpath('//*[@class="d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j fe6kdd0r mau55g9w c8b282yb keod5gw0 nxhoafnm aigsh9s9 d3f4x2em iv3no6db jq4qci2q a3bd9o3v lrazzd5p a57itxjd"]').click()
        try:
            sleep(2)
            browser.find_element_by_xpath('//*[@src="https://static.xx.fbcdn.net/rsrc.php/v3/y2/r/OFdurNsAc7i.png"]').click()
        except:
            wait()

        #finally:
            #browser.find_element_by_xpath('//*[@aria-label="Gỡ Thích"]').click()
        # wait()
    sleep(1)
    browser.quit()

#facebook_auto_unfollow
def facebook_auto_unfollow():
    products_data = pd.read_csv(r'D:\test\Fb\Page_link.csv')
    for product in tqdm(products_data['Link'].tolist()):
        browser.get(product)
        wait()
        # tìm ô like theo nhãn, tuỳ theo ngôn ngữ mà sẽ khác nhau. Việc tìm nhãn phải làm manual
        browser.find_element_by_xpath('//*[@class="d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j fe6kdd0r mau55g9w c8b282yb keod5gw0 nxhoafnm aigsh9s9 d3f4x2em iv3no6db jq4qci2q a3bd9o3v lrazzd5p a57itxjd"]').click()
        try:
            sleep(2)
            browser.find_element_by_xpath('//*[@src="https://static.xx.fbcdn.net/rsrc.php/v3/yI/r/bnvx9uLOEsq.png"]').click()
        except:
            sleep(1)
    sleep(1)
    browser.quit()

#facebook_auto_like
def facebook_auto_like():
    products_data = pd.read_csv(r'D:\test\Fb\post_link.csv')
    for product in tqdm(products_data['Link'].tolist()):
        browser.get(product)
        wait()

        # tìm ô like theo nhãn, tuỳ theo ngôn ngữ mà sẽ khác nhau. Việc tìm nhãn phải làm manual
        try:
            browser.find_element_by_xpath('//*[@aria-label="Thích"]').click()
        except:
        # browser.find_element_by_xpath('//*[@aria-label="Gỡ Thích"]').click()
            wait()
        #finally:
            #browser.find_element_by_xpath('//*[@aria-label="Gỡ Thích"]').click()
        # wait()
    sleep(1)
    browser.quit()


#facebook_auto_unlike
def facebook_auto_unlike():
    products_data = pd.read_csv(r'D:\test\Fb\post_link.csv')
    for product in tqdm(products_data['Link'].tolist()):
        browser.get(product)
        wait()

        # tìm ô like theo nhãn, tuỳ theo ngôn ngữ mà sẽ khác nhau. Việc tìm nhãn phải làm manual
        try:
            browser.find_element_by_xpath('//*[@aria-label="Gỡ Thích"]').click()
        except:

            wait()

    sleep(1)
    browser.quit()

if x == 'post':
    facebook_auto_post_group()
if x == 'comment':
    facebook_auto_comment()
if x == 'follow':
    facebook_auto_follow()
if x == 'unfollow':
    facebook_auto_unfollow()
if x == 'like':
    facebook_auto_like()
if x == 'unlike':
    facebook_auto_unlike()
