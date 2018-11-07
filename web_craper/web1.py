#!/home/asy/.virtualenvs/py3env1/bin/python3

from bs4 import BeautifulSoup as BTSP
import urllib.request

url = 'https://www.amazon.de/s/ref=lp_427957031_nr_p_n_feature_four_bro_1?bbn=427957031&fst=as%3Aoff&ie=UTF8&language=en_GB&qid=1541506893&rh=n%3A340843031%2Cn%3A%21340844031%2Cn%3A427957031%2Cp_n_feature_four_browse-bin%3A7472569031&rnid=7472568031'
souce = urllib.request.urlopen(url).read()
soup = BTSP(souce,'lxml')

#print (soup.title.string)
#print(soup.find_all('p'))

#for paragraph in soup.find_all('p'):
#	print(paragraph.text)
#	print('*******************************************************************')

for url in soup.find_all('a'):
	print(url.get('href'))
	print('*******************************************************************')

