#!/usr/bin/python3
# requests for...requests
# urllib3 for suppressing warnings
# base64 for checking JWT and SAML responses
# termcolor for my silly print_response function
# bs4 for extracting SAML responses to get action URLs and RelayStates
import requests
import urllib3
import base64
from termcolor import colored
from bs4 import BeautifulSoup


# tired of warnings - suppress insecure TLS warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# setting up global variables for later use
base_url = "https://<base_url>"
auth_url = "https://<sso_url>"


# can change this if you don't want it going through a mitm proxy
proxies = {
  'http': 'http://127.0.0.1:8080',
  'https': 'http://127.0.0.1:8080',
}


# custom headers for better looking requests - don't get caught using Python Request User-Agent
header_payload = {
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Accept-Language':'en-US,en;q=0.5',
	'Accept-Encoding': 'gzip, deflate',
	'Content-Type':'application/x-www-form-urlencoded',
	'Origin':'<origin URL>',
	'Referer': '<referer URL>'
}

# Payload for Auth'ing 
payload = {
	'username':'user@user.user',
	'password':'<enter password here>'
}


# Cookie Jar can be used to store cookies across Sessions
jar = requests.cookies.RequestsCookieJar()


# print_response is silly function I wrote to print out good responses vs bad ones
def print_response(r):
	if r.status_code == 200:
		out = r.url + " - " + str(r.status_code)
		print (colored(out,'green'))
	elif r.status_code == 302:
		out = r.url + " - " + str(r.status_code)
		print (colored(out,'yellow'))
	elif r.status_code >= 400 and r.status_code < 500:
		out = r.url + " - " + str(r.status_code)
		print (colored(out,'red'))
	else:
		print (r.url + " - " + str(r.status_code))

# get_auth_cookies is a function for making a request to the initial base URL that will
# setup cookies for further SAML requests - this will need to modified to fit your web app
def get_auth_cookies(url):
	session = requests.Session()
	session.proxies.update(proxies)
	print ("Getting Initial Cookies")
	r = session.get(base_url, headers=header_payload,cookies=jar,verify=False)

	# need to get the form post URL, SAMLRequest, and the RelayState to send to the SAML endpoint
	soup = BeautifulSoup(r.text, 'html.parser')
	action = soup.find('form').get('action')
	try:
		inputs = soup.find_all('input')
		for item in inputs:
			if item.get('name') == "SAMLRequest":
				samlvalue = item.get('value')
			elif item.get('name') == "RelayState":
				relaystate = item.get('value')
			else:
				print ("Ruh Roh Raggy")
				#quit()
	except:
		print("nah")
		quit()

	print_response(r)
	get_saml_cookies(session,action,samlvalue,relaystate)

def get_saml_cookies(session,action,samlvalue,relaystate):
	print ("Getting the Form URL")
	saml_payload = {
		'SAMLRequest':samlvalue,
		'RelayState':relaystate
	}
	r = session.post(action,headers=header_payload,data=saml_payload,cookies=jar,verify=False)
	print_response(r)

	# need to get the URL from the form to send to the final request
	soup = BeautifulSoup(r.text,'html.parser')
	action = soup.find('form').get('action')

	finally_auth(session,action)

def finally_auth(session,url):
	print ("Authentication Happening")
	r = session.post(url,headers=header_payload,data=payload,cookies=jar,verify=False)
	print_response(r)

	# should be able to redirect to the home page now and collect all them sweet sweet cookies
	soup = BeautifulSoup(r.text,'html.parser')
	action = soup.find('form').get('action')
	try:
		inputs = soup.find_all('input')
		for item in inputs:
			if item.get('name') == "SAMLResponse":
				samlvalue = item.get('value')
			elif item.get('name') == "RelayState":
				relaystate = item.get('value')
			elif item.get('type') == "SUBMIT":
				print ("sure")
			else:
				print ("Ruh Roh Raggy")
				print (item)
				quit()
	except:
		print("nah")
		quit()

	redirect_to_index(session,action,samlvalue,relaystate)

def redirect_to_index(session,url,samlvalue,relaystate):
	print ("Index Loading")
	saml_payload = {
                'SAMLRequest':samlvalue,
                'RelayState':relaystate
        }

	r = session.post(url,headers=header_payload,data=saml_payload,cookies=jar,verify=False)
	print_response(r)

# you should have cookies in the jar now that will allow for further schtuff
# this will need to be custom written
def open_orders(session):
	orders_url = "https://<URL After AUthentication>"
	r = session.post()


# main for funsies and organization
if __name__ == "__main__":
	get_auth_cookies(base_url)

