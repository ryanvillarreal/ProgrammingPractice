#!/usr/bin/python2.7

### Quick script this morning to play around with geolite2.  Using fail2ban to track banned IPs. 

from termcolor import colored
import time
import subprocess
import select
import re

def lookup_info(ip):
	from sys import argv, stderr, exit
	from geoip import geolite2

	IP_PROVIDER = "http://httpbin.org/ip"
	comma_sep = lambda x: ", ".join([str(y) for y in x])

	try:
 		match = geolite2.lookup(ip)
	except ValueError, e:
		print e

	print colored(("IP: %s" % match.ip),'red')
	print colored(("Country : %s" % match.country), 'green')
	print colored(("Continet: %s" % match.continent), 'green')
	print colored(("Subvisions: %s" % comma_sep(match.subdivisions)), 'green')
	print colored(("Timezone: %s" % match.timezone), 'green')
	print colored(("Location: %s" % comma_sep(match.location)), 'green')
	print ("")

def main():
	f = subprocess.Popen(['tail','-F','/var/log/fail2ban.log'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	p = select.poll()
	p.register(f.stdout)

	while True:
    		if p.poll(1):
			currentline = f.stdout.readline().strip()
			if 'NOTICE' in currentline:
                		if 'Ban' in currentline:
					ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', currentline )
					lookup_info(''.join(ip))
		time.sleep(1)

if __name__ == "__main__":
	main()
