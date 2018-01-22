from bs4 import BeautifulSoup
import urllib.request
import re
import os
import errno

# create servant_name : servant_info_url dictionary
def get_servant_dictionary():
	data = get_html("http://fategrandorder.wikia.com/wiki/Servant_List")
	
	soup = BeautifulSoup(data, 'html.parser')
	rows = soup.find_all('span', {'class' : 'advanced-tooltip'})
	
	servant_dict = {}
	for row in rows:
		servant_dict[row.a['title']] = "http://fategrandorder.wikia.com" + row.a['href']
		
	return servant_dict

def get_html(url):
	return urllib.request.urlopen(url).read().decode("utf8")

def create_dir(directory):
	try:
		os.makedirs(directory)
	except OSError as e:
		if e.errno != errno.EEXIST:
			raise