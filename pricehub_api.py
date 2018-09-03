import requests

#we are searching for iphone 6 in jumia in this example
#shop options are jumia , kilimall , amazon , skygarden , avechi , pigiame , olx , masoko

search_item = "iphone 6"

shop = "jumia" 

payload = {'query':search_item}

search_results = requests.get('https://www.pricehub.co.ke/api/search/',params=payload)

search_results = search_results.json()

#for each request a maximum of 40 items can be fetched, Authentication is required for more

items = search_results['results'][shop]

print(shop)
print("Result count: ",len(items))

for item in items:
	print(item['name'],item['price'],item['image'],item['link'])
	
	

