'''		TODO:	In function get char info, add all the information to a nested dictionary
		where the key is character name and value is another nested dictionary in which
		there will be all their information names as key and information as values
		corresponding to those keys.
				
				{char_name: {born : year
							 gender: male
							 species: human
							}
				}
		
		After information is put in to dictionary then put every characters nested
		dictionaries in a list.
'''


# Adde a comment
import urllib.request
from bs4 import BeautifulSoup as soup
import re


char_list_url = 'https://en.wikipedia.org/wiki/List_of_Harry_Potter_cast_members'
char_info_url = 'https://harrypotter.fandom.com/wiki/Travers'

char_names = []


def main():

	get_char_names()
	get_char_info()




















# Requests url and returns a binary type
def url_request(url):
	request = urllib.request.Request(url)
	f = urllib.request.urlopen(request)
	html_unparsed = f.read()
	f.close()

	return html_unparsed

	# Parse the binary into html
def parse(unparsed):
	html_parsed = soup(unparsed, 'lxml')

	return html_parsed

	# Gets character names
def get_char_names():
	html = parse(url_request(char_list_url))
	contents = html.find('table',{'class':'wikitable'})
	names = contents.findAll('th',{'scope':'row'})

	for name in names:
		if '[' in name:
			# Removes square brackets if they are at the end of name(last 3 elements in string)
			name = name[0:-3]
			if name.a:
				char_names.append(name.a.text.strip())
			else:
				char_names.append(name.text.strip())
		if name.a:
			char_names.append(name.a.text.strip())
		else:
			char_names.append(name.text.strip())


def get_char_info():
	
	html = parse(url_request(char_info_url))
	contents = html.find('aside',{'role':'region'})
	infos = contents.findAll('section',{'class':'pi-item pi-group pi-border-color'})[1:]
	
	born         = infos[0].div.div.text
	print(born)
	
	blood_status = infos[0].findAll('div',{'class':'pi-item pi-data pi-item-spacing pi-border-color'})[1:]
	blood_status = blood_status[0].div.text.strip()
	print(blood_status)
	
	nationality  = infos[0].findAll('div',{'class':'pi-item pi-data pi-item-spacing pi-border-color'})[2:]
	nationality  = nationality[0].div.text.strip()
	print(nationality)
	
	species      = infos[1].div.div.text
	print(species)
	
	gender       = infos[1].findAll('div',{'class':'pi-item pi-data pi-item-spacing pi-border-color'})[1:]
	gender       = gender[0].div.text.strip()
	print(gender)	
	
	wand		 = infos[3].div.div.text
	print(wand)






main()
