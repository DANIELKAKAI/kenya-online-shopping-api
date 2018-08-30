import requests


search_item = "samsung"

shop = "jumia"

#shop options are jumia,kilimall,amazon,skygarden,avechi,pigiame,olx

payload = {'query':search_item}

results = requests.get('https://www.pricehub.co.ke/api/search/',params=payload)

results = results.json()


print(shop)

items = results['results'][shop]

print(len(items))

for item in items:
	print(item['name'],item['price'],item['image'],item['link'])
