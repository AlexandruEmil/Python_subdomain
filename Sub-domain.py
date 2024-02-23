#USE python3 subdomain.py "path to wordlist" "URL(domain.com/ro..."

import os
import requests
import sys

file = f"{sys.argv[1]}"
path = os.getcwd() + file

sub_list = open(file).read()
subdoms = sub_list.splitlines()

for sub in subdoms:
    sub_domains = f"http://{sub}.{sys.argv[2]}"

    try:
        requests.get(sub_domains)

    except requests.ConnectionError:
        pass

