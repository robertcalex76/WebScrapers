from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
import lxml
import urllib.request
#import winsound
import os

def get_page_html(url):
    
    DRIVER_PATH = '/home/robert/Downloads/chromedriver'
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    driver.get(url);
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language' : 'en-US,en;q=0.5',
        'Accept-Encoding' : 'gzip',
        'DNT' : '1', # Do Not track Request Header
        'Connection' : 'close'
    }
    #page = requests.get(url, headers=headers)
    #print(driver.page_source)
    response = driver.page_source
    driver.quit()
    return (response)

def check_item_in_stock(page_html):
    soup = BeautifulSoup(page_html, 'lxml')
    out_of_stock_divs = soup.find("button", {"class": "btn btn-disabled btn-lg btn-block add-to-cart-button"})
    if(out_of_stock_divs == None):
        print("miss")
        return -1
    else:
        print("hit")
        return out_of_stock_divs.text.find("Sold Out")

def check_inventory():
    url = "https://www.bestbuy.com/site/amd-ryzen-9-5900x-4th-gen-12-core-24-threads-unlocked-desktop-processor-without-cooler/6438942.p?skuId=6438942"
    page_html = get_page_html(url)
    if check_item_in_stock(page_html) == -1:
        print("In stock maybe??????????????")
        #winsound.Beep(1000,1000)
        os.system('spd-say "Stock Found Best Buy Stock Found Best Buy"');
    else:
        print("Out of stock")

while True:
    check_inventory()
    time.sleep(10)

