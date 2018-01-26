from bs4 import BeautifulSoup
import urllib.request
import os
from Utils import *
import json

class WikiaServantData:
	"""holds data about a servant"""
	
	servant_save_directory = "../servant_assets"
	num_stat_field_names = ['Star Absorption', 'Star Generation', 'NP Charge ATK', 'NP Charge DEF', 'Death Rate']
	
	def __init__(self, name, uris):
		self.info = {}
		self.info['name'] = name
		self.uri = uris[0]
		self.image_urls = {'icon' : uris[1]}
		self.data_directory = None
		create_dir(WikiaServantData.servant_save_directory)

	def fill_data(self):
		soup = BeautifulSoup(get_html(self.uri), 'html.parser')
		servant_info = soup.find('div', {'class' : 'ServantInfoWrapper'})
		self.info['id'] = int(servant_info.find("b", string="ID:").parent.getText()[3:])
		self.data_directory = os.path.join(WikiaServantData.servant_save_directory, str(self.info['id']))
		create_dir(self.data_directory)
		
		# grab images/icons
		servant_image_div = servant_info.find('div', {'class' : 'pi-image-collection'})
		for image in servant_image_div.find_all("a"):
			if image['title'].startswith("Stage") or "Sprite" in image['title']:
				self.image_urls[image['title']] = image["href"]
		
		# grab stats
		self.info['class'] = servant_info.find('p', {'class' : 'ServantInfoClass'}).a['title']
		
		# collect numerical stats
		for field_name in WikiaServantData.num_stat_field_names:
			cleanfield = re.sub(r'\s+|%', '', soup.find('b', string=field_name+":").parent.parent.getText()[len(field_name)+2:])
			
			# round down split fields
			if '/' in cleanfield:
				numfield = min([float(i) for i in cleanfield.split('/')])
			else:
				numfield = float(cleanfield)
			self.info[field_name] = numfield
		
		# retrieve non-numerical stats
		# TODO maybe do these or something
		
		
	def save_data(self):
		# save images to servant_save_directory/id/title.png
		for title, url in self.image_urls.items():
			urllib.request.urlretrieve(url, os.path.join(self.data_directory, title + ".png"))
		
		# save servant information to info.json
		with open(os.path.join(self.data_directory, "info.json"), 'w') as f:
			json.dump(self.info, f)

