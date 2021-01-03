import requests
import argparse
import os
import sys
import time
import random

parser = argparse.ArgumentParser(description="API key finder.")
required = parser.add_argument_group("required arguments")
required.add_argument("-u", metavar="url", type=str, action="store", dest="url", required=True, help="the url to scan")

args = parser.parse_args()

url = args.url

def key_request(url):
    try:
        r = requests.get(url, timeout=1)
        if r.status_code == 200:
            return r.json()
        else:
            return "Error {}".format(r.status_code)
    except:
        return "Connection failed, check the url and try again."
        sys.exit()

print("- Connecting to {}".format(url))
print("- Processing keys for {}".format(url))
api_keys = [*range(1,101)]
for key in api_keys:
    if key % 2 != 0:
        check = url + "/api/" + str(key)
        test_url = key_request(check)
        if "PROTECTION" in test_url['q']:
            print("X SECURITY TRIPPED! EXITING...")
            sys.exit()
        if "Error" not in test_url['q']:
            print("+ FOUND SANTA AT {} using key {}".format(test_url['q'], test_url['item_id']))
            sys.exit()

        ran = random.randrange(1,3)
        ran_sleep = 1 / ran
        time.sleep(ran_sleep)
