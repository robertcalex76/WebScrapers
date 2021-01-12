from bs4 import BeautifulSoup
import requests
import time
import os

def get_page_html(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
    page = requests.get(url, headers=headers)
    print(page.status_code)
    return page.content


def check_item_in_stock(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    out_of_stock_divs = soup.find("div", {"class": "product-inventory"})
    print(out_of_stock_divs.text)
    return out_of_stock_divs.text.find("OUT OF STOCK.")

def check_inventory():
    url = "https://www.newegg.com/amd-ryzen-9-5900x/p/N82E16819113664"
    page_html = get_page_html(url)
    if check_item_in_stock(page_html) == -1:
        print("In stock")
        os.system('spd-say "Stock Found newegg Stock Found newegg"');
    else:
        print("Out of stock")

while True:
    check_inventory()
    time.sleep(10)
