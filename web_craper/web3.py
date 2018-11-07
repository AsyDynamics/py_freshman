#!/home/asy/.virtualenvs/py3env1/bin/python3

from bs4 import BeautifulSoup as BTSP
import urllib.request
import csv

print ('******************************************************************************')
url = 'http://www.coreyms.com'
souce = urllib.request.urlopen(url).read()
soup = BTSP(souce,'lxml')

csv_file = open('scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_talk'])

for article in soup.find_all('article'):
	print ('********************* New Item **********************')
	headline = article.h2.a.text
	print (headline)
	summary = article.find('div', class_='entry-content').p.text
	print (summary)

	try:
		vid_src = article.find('iframe', class_='youtuebe-player')['src']
#		vid_id = vid.src.split('/')[4]
#		vid_id = vid_id.split('?')[0]
		yt_link = vid_src.text
#		yt_link = 'https://youtube.com/watch?='+ vid_id
	except Exception as e:
		yt_link = None
	print(yt_link)
	print()
	csv_writer.writerow([headline, summary, yt_link])

csv_file.close()
