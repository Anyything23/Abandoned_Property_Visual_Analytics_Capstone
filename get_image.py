import sys
import requests

KEY = 'AIzaSyC4LVmVfVO0ijWqkMM6cmmZOsauuNcmD5M'

address = sys.argv[1]
	 
addressURL1 = 'https://maps.googleapis.com/maps/api/streetview?size=640x640&location='
addressURL2 = '&key=' 
url = addressURL1 + address + addressURL2 + KEY

r = requests.get(url, allow_redirects=True)
open('streetview.jpg', 'wb').write(r.content)