import requests

url = f'https://pixabay.com/api/?key=<API_KEY>&q=FC barcelona&image_type=photo&pretty=true'
r = requests.get(url)
print(r)
json_data = r.json()
for image in json_data['hits']:
	print(len(json_data['hits']))
	name = image['id']
	img_url = image['largeImageURL']
	r = requests.get(img_url,stream=True)
	with open("pixabay_images/"+str(name)+".jpg",'wb') as f:
		f.write(r.content)