import requests

#we are searching for iphone 6 in jumia in this example

search_item = "iphone 6"

shop = "jumia"

#shop options are jumia , kilimall , amazon , skygarden , avechi , pigiame , olx , alladin 

payload = {'query':search_item}

search_results = requests.get('https://www.pricehub.co.ke/api/search/',params=payload)

search_results = search_results.json()

items = search_results['results'][shop]

print(shop)
print("Result count: ",len(items))

for item in items:
	print(item['name'],item['price'],item['image'],item['link'])
	
	

