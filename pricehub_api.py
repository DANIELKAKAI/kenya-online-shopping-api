import requests

#we are using samsung as an example

search_item = "samsung"

shop = "jumia"

#shop options are jumia,kilimall,amazon,skygarden,avechi,pigiame,olx

payload = {'query':search_item}

search_results = requests.get('https://www.pricehub.co.ke/api/search/',params=payload)

search_results = search_results.json()


print(shop)
print("Result count: ",len(items))

items = search_results['results'][shop]

for item in items:
	print(item['name'],item['price'],item['image'],item['link'])
