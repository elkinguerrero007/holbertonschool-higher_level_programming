#!/usr/bin/python3
""" takes a URL and  email, sends a POST request to the passed URL with the\
 email as a parameter,displays the body of the response(decoded in utf-8) \
"""
from sys import argv
from urllib import request, parse

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    data = parse.urlencode({'email': email})
    data = data.encode('ascii')
    with request.urlopen(url, data) as f:
        print(f.read().decode('utf-8'))
