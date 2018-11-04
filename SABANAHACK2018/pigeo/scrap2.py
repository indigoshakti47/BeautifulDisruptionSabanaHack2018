

import requests

res = requests.get('https://whatismyipaddress.com/ip-lookup')
data = res.json()

print(data.text)