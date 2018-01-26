from bs4 import BeautifulSoup
import urllib.request
import re
import os
import errno

def get_html(url):
	return urllib.request.urlopen(url).read().decode("utf8")

def get_html_soup(url):
	return BeautifulSoup(get_html(url), 'html.parser')
	
def create_dir(directory):
	try:
		os.makedirs(directory)
	except OSError as e:
		if e.errno != errno.EEXIST:
			raise