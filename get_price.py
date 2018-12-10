import time
import sys
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from geopy.geocoders import Nominatim
from selenium.webdriver.chrome.options import Options  

w = open("price_page_source.txt", "w")
y = open("price.txt", "w")
z = open("price_zip.txt", "w")

#Creating url from address
FullAddress = sys.argv[1]
#FullAddress = '225 N 6TH ST Newark NJ'
FullAddress = FullAddress.replace("+", " ")
geolocator = Nominatim()
location = geolocator.geocode(FullAddress, addressdetails = True)
zip = location.raw['address']['postcode']
url = 'https://www.realtor.com/local/' + zip + '/housing-market'
webpage = r"https://www.realtor.com/"

#Setting up Chrome driver
chrome_options = Options()  
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(chrome_options=chrome_options) 
#browser = webdriver.Chrome("./chromedriver")

#Get results from url
browser.set_page_load_timeout(60)
browser.get(webpage)
try:
    timeout = time.time() + 60 
    while True:
        try:
            if time.time() > timeout:
                break
            sbox = browser.find_element_by_id("rdc-main-search-nav-hero-input") 
            sbox.send_keys(FullAddress)
            sbox.submit()
        except:
            if time.time() > timeout:
                break 
            try:
                sbox = browser.find_element_by_id("searchBox")
                sbox.send_keys(FullAddress)
                browser.find_element_by_xpath("//div[@class='home-search-wrapper']/div[2]/span/button[2]").click()				
            except:
                continue
            else:
                break            
            continue
        else:
            break
    timeout = time.time() + 60
    while True:
        try:
            if time.time() > timeout:
                break
            href = browser.find_element_by_xpath("//a[contains(text(),'Track Your Home')]").get_attribute("href")
        except:
            if time.time() > timeout:
                break
            continue
        else:
            break
    href=href[:-5]
    href = href + 'selling-tools'
    browser.get(href)
    text = browser.page_source
    browser.get(url)
    timeout = time.time() + 60
    while True:    
        try:
            if time.time() > timeout:
                break
            p = browser.find_element_by_xpath("//section/p").text
        except:
            if time.time() > timeout:
                break
            continue
        else:
            break
except:
    browser.quit()
else:
    browser.quit()

#Save results to file

w.write(text)
x = open("price_page_source.txt").read().replace('\n','')
start = '"historical":'
end = ']]'
price = ((x.split(start))[1].split(end)[0])
price = price.replace('[[','').replace('],[','\n').replace(',','\n')
price = price + '\n'

y.write(price)

pz = []
m = re.search('[0-9]*\.*[0-9]*%',p)
m = m.group(0)
m = m[:-1]
pz.append(m)
n = re.search('up|down',p)
n = n.group(0)
pz.append(n)
o = re.search('\$[0-9*].*[0-9]*[KM]',p)
o = o.group(0)
o = o[1:-1]
pz.append(o)

for x in pz:
    z.write(x + '\n')