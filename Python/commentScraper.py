import requests,copy
from bs4 import BeautifulSoup
from bs4 import Comment

proxies = {"http": "http://127.0.0.1:8080","https": "https://127.0.0.1:8080"}


def get_comments(URL):
	r = requests.get(URL,proxies=proxies)
	soup = BeautifulSoup(r.text, "lxml")
	comments = soup.find_all(string=lambda text:isinstance(text,Comment))
	for comment in comments:
		print comment

def spider_web(URL,depth):
	# I guess I need to do an inital grab in order to invoke a psuedo do-while loop?
	urls = []
	new_urls = []
	url_log = []
	r = requests.get(URL, proxies=proxies)
	soup = BeautifulSoup(r.text,"lxml")
	for link in soup.find_all('a', href=True):
		if "redirect" in link["href"]:
			continue
		else:
			urls.append(link["href"])
			url_log.append(link["href"])
	print "Length of URLS %i" % len(urls)

	# now start the depth checking?
	for number in range(int(depth)):
		raw_input("Pause...")
		while len(urls) > 0:
			# build URL with new
			print "Sending request to: %s" % URL+ urls[0]
			r = requests.get(URL+urls[0],proxies=proxies)
			soup = BeautifulSoup(r.text, "lxml")
			urls.pop(0)
			# once the request is made you can pop it off the stack
			for link in soup.find_all('a', href=True):
				# check for out of scope - need to find out redirects work IRL
				if "redirect" in link["href"]:
					break
				else:
					if link["href"] not in url_log:
						print link["href"]
						new_urls.append(link["href"])
						url_log.append(link["href"])
					else: break
			print "Length of new_urls %i" % len(new_urls)
		print "========= Depth %i ==========" % number
	print "Total requests made: %i" % len(url_log)

def spider_sitemap(URL,depth):
	print "grab the sitemap and look at pages from there"


if __name__ == "__main__":
	#URL = raw_input("Enter the URL: ")
	#get_comments(URL)
	#depth = raw_input("Max depth: ")
	spider_web("http://juice.local/", 4)
