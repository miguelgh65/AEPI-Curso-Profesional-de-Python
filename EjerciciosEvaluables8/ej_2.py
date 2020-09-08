
from urllib import request
from urllib.error import URLError
url="https://www.gutenberg.org/files/1484/1484-0.txt"
file=request.urlopen(url)

content = file.read()
tamano=len(content.split())

print(tamano)
