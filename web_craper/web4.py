from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup as BSP

try:
    html = urlopen('http://pythonscraping.com/pages/page1.html')
except HTTPError as e:
    print(e)
    # return null, break or other
except URLError as e:
    print('The server not found')
else:
    print('It workd!')

bsObj = BSP(html, 'lxml')
print(bsObj)
