from bs4 import BeautifulSoup
import requests
import time

def get_page_html(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
    page = requests.get(url, headers=headers)
    print(page.status_code)
    return page.content


def check_item_in_stock(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    out_of_stock_divs = soup.find("div", {"class": "product-inventory"})
    print(out_of_stock_divs)
    return out_of_stock_divs.text.find == "OUT OF STOCK."

def check_inventory():
    #return 1 if data has changed, 0 if no change
    url = "https://www.newegg.com/hp-prodesk-400-g5-nettop-computer/p/N82E16883997492?Item=9SIA7ABC996974"
    page_html = get_page_html(url)
    if check_item_in_stock(page_html) == -1:
        print("In stock")
    else:
        print("Out of stock")

#main
#get item name, web url, and maybe html data item from file, place them into struct 
#print if read in successfuly 
int found = 0;
while True:
    #iterate throught list of urls or html data
        found = check_inventory(url and or html data)
        if found == 1:
            #output which website had stock
            #maybe beep loudly
            #loop indefinitly, require restart

    time.sleep(2)
