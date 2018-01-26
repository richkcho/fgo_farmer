from bs4 import BeautifulSoup
import urllib.request
import re
import os
from WikiaServantData import WikiaServantData
from Utils import *
from multiprocessing import Pool
import multiprocessing

# create servant_name : (servant_info_url, servant_icon_url) dictionary
def get_servant_dictionary():
	data = get_html("http://fategrandorder.wikia.com/wiki/Servant_List")
	
	soup = BeautifulSoup(data, 'html.parser')
	rows = soup.find_all('span', {'class' : 'advanced-tooltip'})
	
	servant_dict = {}
	for row in rows:
		servant_dict[row.a['title']] = ("http://fategrandorder.wikia.com" + row.a['href'], row.a.img['data-src'])
		
	return servant_dict

def get_data(item):
	name, uris = item
	print("Downloading data for", name)
	mashu = WikiaServantData(name, uris)
	mashu.fill_data()
	mashu.save_data()
	print("Finished getting data for", name)
	
def download_wikia_data():
	servant_dict = get_servant_dictionary()
	
	with Pool(multiprocessing.cpu_count()*2) as pool:
		pool.map(get_data, servant_dict.items())