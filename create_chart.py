import matplotlib.pyplot as plt
import datetime
import numpy as np
import math
import os

zwq = open("price_slopes.txt", "w")
if os.path.exists('chart.png'):
   os.remove('chart.png')
x = open("price.txt").read() 
count = 1
month = []
price = []
num = ''
for line in x:
	if line != '\n':
		num = num + line
	else:
		if count%2 == 1:
			s = int(num) / 1000.0
			m = datetime.datetime.fromtimestamp(s).strftime('%b-%y')
			month.append(m)
		else:
			price.append(int(num)/1000.0)
		num = ''
		count = count + 1
month = month[-13:]	
price = price[-13:]	
	
with open("price_zip.txt") as f:
    price_zip = f.read().splitlines()

m2 = []
m2.append(month[0])
m2.append(month[12])
p2 = []
if price_zip[1] == 'up':
	p2.append(float("{0:0.1f}".format(float(price_zip[2])/(1 + (float(price_zip[0])/100.0)))))
else:
	p2.append(float("{0:0.1f}".format(float(price_zip[2])/(1 - (float(price_zip[0])/100.0)))))
p2.append(float(price_zip[2]))

	
plt.figure(figsize=(9,5))
plt.plot(month, price, color='b', label = "This House", marker='o')
plt.plot(m2, p2, color='orange',linestyle='-', marker='o', label = "City Average")
plt.xlabel('Date')
plt.ylabel('House Price (Thousands $)')
plt.title('House Pricing History')
plt.legend(loc='best')
plt.grid(True, linestyle='-')
bottom, top = plt.ylim()
plt.ylim((bottom*0.85, top*1.15)) 
plt.tight_layout()
x = list(range(0, 13))
g = list(range(2))
ge = [0,12]
z = np.polyfit(x, price, 1)
p = np.poly1d(z)
plt.plot(x,p(x),"b--")
qw = np.polyfit(ge, p2, 1)
for x, y in zip(x,price):
    plt.annotate('%s' % y, xy=(x, y), textcoords='data', horizontalalignment='center', verticalalignment='bottom')
for x, y in zip(ge,p2):
    plt.annotate('%s' % y, xy=(x, y), textcoords='data', horizontalalignment='center', verticalalignment='bottom')
plt.rcParams.update({'font.size': 22})
#plt.show()
plt.savefig('chart.png', bbox_inches='tight')

data = []
data.append('This House Trendline Slope: ' + str("{0:0.1f}".format(z[0])))
data.append('City Average Trendline Slope: ' + str("{0:0.1f}".format(qw[0])))
diff = math.atan(z[0]/10.0) - math.atan(qw[0]/10.0)
di = diff/math.pi*600

if di < 0:
    di = di * (-1)
if di > 99:
    di = 99.0
if qw[0] < z[0]:
    di = 0.0

data.append("{0:0.1f}".format(di) + '%' + ' Chance of Abandonment')


for x in data:
	zwq.write(x + '\n')
