from fp.fp import FreeProxy

def get_proxy(number=1):

	proxy_list = []

	for i in range(number):
		proxy_list.append(FreeProxy(rand=True).get()[7:])
	
	return proxy_list