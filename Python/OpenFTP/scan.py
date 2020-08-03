#!/usr/bin/python3
import requests, sys, os, json, ftplib, argparse, requests, time, re
from termcolor import colored, cprint
import shodan

# defaults
scanned = []
scanned_hosts_file = "./data/scanned.txt"
output_file = "./output/output.txt"

def read_in_scanned():
    # should use a hardcoded filename - for ease of use. 
    with open(scanned_hosts_file) as f:
        lines = f.read().splitlines()

    for line in lines: 
        scanned.append(line)
    cprint ("We read in %i line(s)" % len(lines), 'green')

def write_out_scanned(ip):
    try:
        f = open(scanned_hosts_file, "a")
        f.write(ip + "\n")
        f.close()
    except Exception as e:
        print ("Error %s" % e)


def masscan_search():
    read_in_scanned()
    cprint ("running masscan search", "green")
    with open("./mass/ftp.hosts.grep") as f:
        for line in f:
            if "Host:" in line:
                ip = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line.strip()).group()
                connect_ftp(ip)


def shodan_search():
    read_in_scanned()
    page = 0 # can modify this for now - will eventually be included in argparse

    # rolled the api key - for anyone scraping this is a false positive key
    API_KEY = '<enter API here>'
    cprint ("Grabbing page %i" % page, 'red')

    while True:
        try:
            # Setup the api
            api = shodan.Shodan(API_KEY)
            if page <= 20:
                page += 1
            else:
                page = 1
             # Perform the search
             # play nice with the API
            time.sleep(2)
            query = ' '.join('port 21')
            result = api.search(query, page)

             # Loop through the matches and check each one for open directories
            print("total results on page %i: %i" % (page, len(result['matches'])))

            for service in result['matches']:
                ip = service['ip_str']
                # try the FTP login
                if ip not in scanned:
                    connect_ftp(ip)

            # get the next page
            cprint ("Grabbing the next page", 'red')

        except shodan.APIError as e:
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
        cprint ("Already tested %i hosts" % len(scanned), 'yellow')

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
    f = open(output_file,'a+')
    f.write("Logged in anonymously at %s \n" % ip)
    try:
        list_contents = ftp.retrlines('LIST')
        f.write("Found dir on IP: %s \n" % ip)
        for line in list_contents:
            f.write(line)
        f.write("Finished checking: %s \n" % ip)
        f.close
    except ftplib.all_errors as e:
        f.write("Error: %s on IP %s \n" % (e, ip))
        return 0

def menu():
    # parse dem args my boi
    parser = argparse.ArgumentParser(
        description="OpenFTP -- Happy Hunting!"
    )
    parser.add_argument("-v","--version", action='version', version='%(prog)s 0.1')
    
    # setup subparsers for func action
    subparsers = parser.add_subparsers(dest="command")
    
    # check_ip subparser
    check_parser = subparsers.add_parser("check", help="check to see what IP you are originating from")
    check_parser.set_defaults(func=check_ip)

    # masscan subparser
    mass_parser = subparsers.add_parser("masscan", help="perform a scan for IPs using Masscan data.")
    mass_parser.set_defaults(func=masscan_search)

    # # shodan subparser
    shodan_parser = subparsers.add_parser("shodan", help="perform a scan for IPs using Shodan data.")
    shodan_parser.set_defaults(func=shodan_search)

    # finally parse the arg setup for commands I guess?
    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        parser.exit(1)

    # finally parse the functions for argparse
    args.func()

if __name__ == "__main__":
    menu()
