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

if len(sys.argv)==1:
	print("[*] Please Provide Domain Name:\n Usages: python link_re.py www.examplesite.com\n")
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

# Condition
if html_data:
	pattern = re.compile('(<a .*?>)')			# First, Find all <a > tag
	a_tag_captured = pattern.findall(html_data)	
	for i in a_tag_captured:					# Second, Now Find href tag in all tag
		href=re.search('href=.*', i[1:-1])
		if href: 								# If Tag Found
			print(href.group().split(' ')[0]) 	# Print Tag
