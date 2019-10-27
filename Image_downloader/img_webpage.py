#!/usr/bin/python

##################################################
######## Please Don't Remove Author Name #########
############### Thanks ###########################
##################################################
#
#
__author__='''

    Suraj Singh
    surajsinghbisht054@gmail.com
    https://bitforestinfo.blogspot.in/
'''

# Import Module
import urllib.request, urllib.error, urllib.parse
import sys
import re
import os

if len(sys.argv)==1:
	print("[*] Please Provide Domain Name:\n Usages: python img_webpage.py www.examplesite.com\n")
	sys.exit(0)

# Retrieve Html Data From Url
def get_html(url):
	try:
 		page = urllib.request.urlopen(url).read()
	except Exception as e:
		print("[Error Found] ",e)
		page=None
	return page

html_data=get_html(sys.argv[1])

# Verifying Html Data
if not html_data:
	exit(0)

# Regular Expression
pattern = re.compile('<img .*?>')
image_link=[]
for i in pattern.findall(html_data):
    i=i[i.find('src'):-2]
    img=i.split(' ')[0]
    if 'http' in img[4:10]:
        image_link.append(img)
        
# Downloading Image
def image_download(link):
    img=open(os.path.basename(link),'wb')   
    data=urllib.request.urlopen(link)
    img.write(data.read())
    img.close()
    return

for i in image_link:
    print(str(i[4:]))
    image_download(i[5:-1])
