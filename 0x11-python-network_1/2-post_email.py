#!/usr/bin/python3
# Script that sends a POST request to a given URL with a given email.
import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare 
    data = urllib.parse.urlencode({"email": email}).encode("utf-8")
    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode("utf-8"))
