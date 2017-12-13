import urllib.request
import time

def get_price():
    page = urllib.request.urlopen("http://beans.itcarlow.ie/prices-loyalty.html")
    text = page.read().decode("utf8")
    where = text.find(">$")
    start_of_price = where + 2
    end_of_price = start_of_price + 4
    #price = text[start_of_price:end_of_price]
    #price = float(price)
    #print(price)

    #print(text[start_of_price:end_of_price])
    return float(text[start_of_price:end_of_price])   #返回sting格式

'''
#page = urllib.request.urlopen("http://www.beans-r-us.biz/prices.html")
#page = urllib.request.urlopen("http://beans.itcarlow.ie/prices.html")
page = urllib.request.urlopen("http://beans.itcarlow.ie/prices-loyalty.html")
#page = urllib.request.urlopen("https://api.yeeuu.com/v2/device/00124b000f0855c4/devicestatus?key=superman")
text = page.read().decode("utf8")

#print(text[233:238])

#price = text[233:238]   #$5.70< 233是$    238是<（不包括）
#print(price)

#characterposition = text.find(">$")

#print(text)
#print(text[characterposition+1:characterposition+6])

where = text.find(">$")
start_of_price = where + 2
end_of_price = start_of_price + 4
price = text[start_of_price:end_of_price]


print(price)
'''
'''
price = 99.99
while price > 4.74:
    time.sleep(5)
    page = urllib.request.urlopen("http://beans.itcarlow.ie/prices-loyalty.html")
    text = page.read().decode("utf8")
    where = text.find(">$")
    start_of_price = where + 2
    end_of_price = start_of_price + 4
    price = text[start_of_price:end_of_price]
    price = float(price)
    print(price)
print(price)
print("Buy!")
'''

print("You are welcome, Master！")
order = input("Do you want to see the price of coffee now? (Y/N) ")
if order == 'Y':
    print(get_price())
else:
    price = 99.99
    while price > 4.74:
        time.sleep(5)
        # price
        price = get_price()
        print(price)
    print("Buy!")