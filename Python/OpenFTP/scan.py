#!/usr/bin/python

import requests, sys, os, json, ftplib, shodan, argparse
from termcolor import colored

def shodan_search():
    # rolled the api key - for anyone scraping this is a false positive key
    API_KEY = 'JgWgPNH5N7E66wZof1KXKy5sZqceOqbW'
    try:
        # Setup the api
        api = shodan.Shodan(API_KEY)

        # Perform the search
        query = ' '.join('port 21')
        result = api.search(query)

        # Loop through the matches and check each one for open directories
        print("total results: %i" % len(result['matches']))
        for service in result['matches']:
            connect_ftp(service['ip_str'])
    except Exception as e:
        print('Error: %s' % e)

def check_ip():
    session = requests.session()
    session.proxies = {}
    r = session.get("http://httpbin.org/ip")
    print(r.text)

def connect_ftp(ip):
    # setup the tor node if proxy is required
    #tor_node = FTP('')
    #tor_node.login('anonymous@'+ip,'@anonymous')
    #tor_node.retrlines('LIST')

    # if the argument is set to use tor send to the localhost:9050 instead of the address
    if args.tor:
        print("Use Tor")

    # try the FTP Login
    try:
        print("trying host: %s" % ip)
        ftp = ftplib.FTP(ip, timeout=2)
    except ftplib.all_errors as e:
        print("Could not connect...skipping this host")
        return 0
    
    # now try to login to the FTP client
    print("trying to login to %s" % ip)
    try:
        ftp.login()
    except ftplib.all_errors as e:
        print("could not login")
        return 0

    print colored('Logged in...dumping directory', 'green')
    try:
        list_contents = ftp.retrlines('LIST')
        f = open('test.txt','a+')
        for line in list_contents:
            f.write(line)
            f.close
    except ftplib.all_errors as e:
        print(e)
        return 0

def masscan_search():
    data = {}
    for file in os.listdir("./"):
        if file.endswith(".json"):
            with open(file) as json_file:
                data = json.load(json_file)
    # should have loaded all the data here.          
    if not data:
        print("No data loaded...try running masscan or using Shodan")
        sys.exit(0)
    for ip in data:
        #print(ip['ip'])
        connect_ftp(ip['ip'])



if __name__ == "__main__":
    print("main")
    #get_ip()
    #read_json()
    parser = argparse.ArgumentParser(prog='scan.py')

    # setup argument flags
    generalGroup = parser.add_argument_group('General Options')
    generalGroup.add_argument('-t', '--tor', help='Pipe data through tor', action='store_true', default=False)
    generalGroup.add_argument('-S', '--Shodan', help='Run the shodan function', action='store_const', dest='shodan_search')
    generalGroup.add_argument('-M', '--Masscan', help='Run the masscan function', action='store_const', dest='masscan_search')

    # parse argument
    args = parser.parse_args()

    # choose between Shodan and masscan here
    read_json()
