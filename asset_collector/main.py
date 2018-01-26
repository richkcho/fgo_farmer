from bs4 import BeautifulSoup
import urllib.request
import re
import os
import download_wikia_data as wikia

def main():
	wikia.download_wikia_data()
	
	# qwe = next (iter (servant_dict.items()))
	
	# print(qwe)
	
	# mashu = WikiaServantData(qwe[0], qwe[1])
	# mashu.fill_data()
	# mashu.save_data()
	
	# appmedia is unreliable training data probably or something
	# appmedia_base_url = 'https://appmedia.jp/fategrandorder/'
	# appmedia_servant_lists = ['429305', '429052', '100382', '93558', '96261']
	# servant_links = []
	# for page_id in appmedia_servant_lists:
		# soup = get_html_soup(appmedia_base_url + page_id)
		# servant_links += [link['href'] for link in soup.find_all('table', border='1')[1].find_all('a')]

	# print(len(servant_links))

if __name__ == "__main__":
	main()