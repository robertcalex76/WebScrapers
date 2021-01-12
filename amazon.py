from bs4 import BeautifulSoup
import requests
import time
import lxml
from random import randint
import httplib2
import os

def get_page_html(url):

    headers = {
    'authority': 'www.amazon.com',
    'rtt': '50',
    'downlink': '1.75',
    'ect': '4g',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.amazon.com/DANIPEW-Sand-Man-Cotton-Performance-T-Shirt/product-reviews/B08164VTWH?reviewerType=all_reviews',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'i18n-prefs=USD; lc-main=en_US; ubid-main=133-0414423-5604507; session-id=147-3892155-9445258; session-id-apay=147-3892155-9445258; session-id-time=2082787201l; _mkto_trk=id:365-EFI-026&token:_mch-amazon.com-1604946337453-79083; AMCV_4A8581745834114C0A495E2B%40AdobeOrg=-408604571%7CMCIDTS%7C18576%7CMCMID%7C80497564362888985864515092031015692426%7CMCAAMLH-1605551137%7C7%7CMCAAMB-1605551137%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1604953537s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.6.0; mbox=session#72829ee134b743c29bf060ea63c8ff50#1604948198|PC#72829ee134b743c29bf060ea63c8ff50.34_0#1668191138; s_nr=1604946337526-New; s_lv=1604946337528; x-amz-captcha-1=1605825162946543; x-amz-captcha-2=YWuKyudSa2dzFxm565DLvQ==; session-token=pAvLoaY31PFnvLuAaHsAGfNUQvvGwdK5Aqht3fURnPXXabVl4aDZkJhe2nRDbfFLgo5YKOZtLgTcT8agxHUShGW/Pm+/ZNNHpDIgHrvZGoPgtLl9qwhKL3hp49Vafkb9QbVIX3+dwv5JSil/nYacSYs4rDWLBYfI6Dr4wXnl8LhVwjHBQvZKxIsExzcf67e3; skin=noskin; csm-hit=tb:QSVM7DW90M8W8HCKSQ72+s-D1PQ8XY9NEW4YBTFQCB8|1605818090040&t:1605818090040&adb:adblk_no',
}

    page = requests.get(url, headers=headers)
    #print(page.status_code)
    #return page.content
    http=httplib2.Http()
    temp,page=http.request(url, headers=headers)
    return page

def check_item_in_stock(page_html):
    soup = BeautifulSoup(page_html, 'lxml')
    out_of_stock_divs = soup.find("div", {"id": "availability"})
    if(out_of_stock_divs == None):
        print("miss")
        return 0
    else:
        print("hit")
        return out_of_stock_divs.text.find("Currently unavailable.")

def check_inventory():
    url = "https://www.amazon.com/AMD-Ryzen-5900X-24-Thread-Processor/dp/B08164VTWH/ref=cm_cr_arp_d_pb_opt?ie=UTF8"
    page_html = get_page_html(url)
    if check_item_in_stock(page_html) == -1:
        print("5900x In stock!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        os.system('spd-say "5900x Stock Found amazon 5900x Stock Found amazon"');
    else:
        print("5900x Out of stock")
    url = "https://amazon.com/AMD-Ryzen-5950X-32-Thread-Processor/dp/B0815Y8J9N/ref=cm_cr_arp_d_product_top?ie=UTF8"
    page_html = get_page_html(url)
    if check_item_in_stock(page_html) == -1:
        print("5950x In stock!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        os.system('spd-say "5950x Stock Found amazon 5950x Stock Found amazon"');
    else:
        print("5950x Out of stock")


while True:
    check_inventory()
    time.sleep(randint(5,20))

