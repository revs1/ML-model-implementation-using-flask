import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'total_rooms':880, 'total_bedrooms':129, 'population':322  })

print(r.json())