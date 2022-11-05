#! /usr/bin/python

import requests
import base64
from bs4 import BeautifulSoup

url = input("Direct URL to image:")
url_bytes = url.encode('ascii')
base64_bytes = base64.b64encode(url_bytes)
base64_url = base64_bytes.decode('ascii')

resp = requests.get(f'https://token.otfbm.io/meta/{base64_url}', timeout=30)
soup = BeautifulSoup(resp.content, 'html.parser')
print(soup.body.string)
