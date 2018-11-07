#!/home/asy/.virtualenvs/py3env1/bin/python3

from bs4 import BeautifulSoup as BTSP
import urllib.request

print ('******************************************************************************')
url = 'https://www.amazon.de/s/ref=lp_427957031_nr_p_n_feature_four_bro_1?bbn=427957031&fst=as%3Aoff&ie=UTF8&language=en_GB&qid=1541506893&rh=n%3A340843031%2Cn%3A%21340844031%2Cn%3A427957031%2Cp_n_feature_four_browse-bin%3A7472569031&rnid=7472568031'
souce = urllib.request.urlopen(url).read()
soup = BTSP(souce,'lxml')

#nav = soup.nav
for div in soup.find_all('div', class_='s-item-container'):
	print ('************ New Item ************')
	print (div.text)
	print ('\n')
#	print (div.find('a', class_='a-link-normal s-access-detail-page s-color-twister-title-link a-text-normal').get('href'))
	print (div.find('a', class_='a-link-normal a-text-nomal'))
