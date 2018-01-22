from bs4 import BeautifulSoup
import urllib.request
import re
import os
from ServantData import ServantData
from Utils import *

def main():
	servant_dict = get_servant_dictionary()
	
	# for name, url in servant_dict.items():
		# print(name, url)
	
	qwe = next (iter (servant_dict.items()))
	
	print(qwe)
	
	mashu = ServantData(qwe[0], qwe[1])
	mashu.fill_data()
	mashu.save_data()

if __name__ == "__main__":
	main()