import requests

res = requests.get('https://ipinfo.io/')
data = res.json()


city= data['city']

location = data['loc'].split(',')
latitude = location[0]

longitude = location[1]

region=data['region']

org=data['org']



print("Latitud : ", str(latitude))
print("Longitud : ", str(longitude))
print("Region :", str(region))
print("Proveedor :", str(org))

