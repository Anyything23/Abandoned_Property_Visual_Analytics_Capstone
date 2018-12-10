import time
import sys
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from geopy.geocoders import Nominatim
from selenium.webdriver.chrome.options import Options  
x = open("crimes.txt", "w")
#Creating url from address
address = sys.argv[1]
#address = "108 Brookdale Ave Newark NJ"
geolocator = Nominatim()
address = address.replace("+", " ")
location = geolocator.geocode(address, addressdetails = True)
url = 'https://www.crimereports.com/home/#!/dashboard?lat=' + str(location.latitude) + '&lng=' + str(location.longitude) + '&zoom=18&incident_types=Assault%252CAssault%2520with%2520Deadly%2520Weapon%252CBreaking%2520%2526%2520Entering%252CDisorder%252CDrugs%252CHomicide%252CKidnapping%252CLiquor%252COther%2520Sexual%2520Offense%252CProperty%2520Crime%252CProperty%2520Crime%2520Commercial%252CProperty%2520Crime%2520Residential%252CQuality%2520of%2520Life%252CRobbery%252CSexual%2520Assault%252CSexual%2520Offense%252CTheft%252CTheft%2520from%2520Vehicle%252CTheft%2520of%2520Vehicle&start_date=2017-' + datetime.datetime.today().strftime('%m-%d') + '&end_date=' + datetime.datetime.today().strftime('%Y-%m-%d') + '&days=sunday%252Cmonday%252Ctuesday%252Cwednesday%252Cthursday%252Cfriday%252Csaturday&start_time=0&end_time=23&include_sex_offenders=false&current_tab=list&shapeIds=&shape_id=false'

#Setting up Chrome driver
chrome_options = Options()  
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(chrome_options=chrome_options)
#browser = webdriver.Chrome("./chromedriver")

#Get results from url
browser.set_page_load_timeout(60)
browser.get(url)
try:
    timeout = time.time() + 25
    while True:
        try:
            if time.time() > timeout:
                break
            browser.find_element_by_xpath("//span[@ng-click='incidentList.openPrintPage()']").click()
        except:
            if time.time() > timeout:
                break
            continue
        else:
            break
    timeout = time.time() + 25
    while True:
        try:
            if time.time() > timeout:
                break
            table = browser.find_element_by_class_name('table-striped')
        except:
            if time.time() > timeout:
                break
            continue
        else:
            break
    text = []
    for td in table.find_elements_by_tag_name('td'):
        text.append(td.text)
except:
    browser.quit()
else:
    browser.quit()

#Save results to file

for line in text:
    x.write(line + "\n")