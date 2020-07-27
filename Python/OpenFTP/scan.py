#!/usr/bin/python3
import requests, sys, os, json, ftplib,argparse, requests
from termcolor import colored, cprint
from shodan import Shodan

scanned = []

def read_in_scanned():
    # should use a hardcoded filename - for ease of use. 
    with open('./scanned.txt') as f:
        lines = f.read().splitlines()

    for line in lines: 
        scanned.append(line)
    cprint ("We read in %i line(s)" % len(lines), 'green')

def write_out_scanned(ip):
    try:
        f = open("./scanned.txt", "a")
        f.write(ip + "\n")
        f.close()
    except Exception as e:
        print ("Error %s" % e)


def shodan_search():
    page = 0
    API_KEY = '<insert API Key here>'
    cprint ("Grabbing the first page", 'red')

    while True:
        try:
            # Setup the api
            api = Shodan(API_KEY)
            page += 1
             # Perform the search
            query = ' '.join('port 21')
            result = api.search(query, page)

             # Loop through the matches and check each one for open directories
            print("total results on page %i: %i" % (len(result['matches']), page))

            for service in result['matches']:
                ip = service['ip_str']
                # try the FTP login
                if ip not in scanned:
                    connect_ftp(ip)

            # get the next page
            cprint ("Grabbing the next page", 'red')

        except Exception as e:
            # need to figure out how to differinate between timeout and no more page errors
            if e == "The search request timed out.":
                cprint("Error: %s" % e)
            else:
                cprint("Error: %s" % e)
                cprint("Exiting", 'red')
                #sys.exit() 


def check_ip():
    session = requests.session()
    session.proxies = {}
    r = session.get("http://httpbin.org/ip")
    print(r.text)


def connect_ftp(ip):
    # show the list of already scanned items for debugging
    if len(scanned) % 10 == 0:
        print ("Already tested %i hosts" % len(scanned), 'yellow')

    # if new IP test it 
    try:
        print("Trying host: %s" % ip)
        ftp = ftplib.FTP(ip, timeout=2)
        # add scanned IP to list for quick checking, and to scanned.txt for on disk checking
        write_out_scanned(ip)
        scanned.append(ip)
    except ftplib.all_errors as e:
        #print ("Couldn't not connect...skipping host")
        write_out_scanned(ip)
        scanned.append(ip)
        return 0

    print("Connected... attempting to login to %s " % ip)
    try:
        ftp.login()
    except ftplib.all_errors as e:
        print("could not login")
        return 0

    cprint ('Logged in...dumping directory', 'green')
    try:
        list_contents = ftp.retrlines('LIST')
        f = open('test.txt','a+')
        f.write("Found dir on %s \n" % ip)
        for line in list_contents:
            f.write(line)
            f.close
    except ftplib.all_errors as e:
        print(e)
        return 0

if __name__ == "__main__":
    read_in_scanned()
    shodan_search()
