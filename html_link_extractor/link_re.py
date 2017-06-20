#!/usr/bin/python
# ---------------- READ ME ---------------------------------------------
# This Script is Created Only For Practise And Educational Purpose Only
# This Script Is Created For https://bitforestinfo.blogspot.in
# This Script is Written By
#
#
##################################################
######## Please Don't Remove Author Name #########
############### Thanks ###########################
##################################################
#
#
__author__='''

######################################################
                By S.S.B Group                          
######################################################

    Suraj Singh
    Admin
    S.S.B Group
    surajsinghbisht054@gmail.com
    https://bitforestinfo.blogspot.in/

    Note: We Feel Proud To Be Indian
######################################################
'''
# Import Module
import urllib2
import sys
import re

if len(sys.argv)==1:
	print "[*] Please Provide Domain Name:\n Usages: python link_re.py www.examplesite.com\n"
	sys.exit(0)

# Retrieve Html Data From Url
def get_html(url):
	try:
 		page = urllib2.urlopen(url).read()
	except Exception as e:
		print "[Error Found] ",e
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
			print href.group().split(' ')[0] 	# Print Tag
