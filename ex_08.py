import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1380584.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')
sum = 0
count = 0

for tag in tags:
  count = count + 1
  sum = sum + int(tag.contents[0])

print('Count', count)
print('Sum', sum)
