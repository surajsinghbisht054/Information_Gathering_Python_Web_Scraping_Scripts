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
from HTMLParser import HTMLParser


# For More Info https://docs.python.org/2/library/htmlparser.html
class link_extractor(HTMLParser):
    def handle_starttag(self,tag, attrs):
        for attr in attrs:
            if 'href' in attr[0]:
                print attr[1]



if len(sys.argv)==1:
	print "[*] Please Provide Domain Name:\n Usages: python link_hp.py www.examplesite.com\n"
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

parser=link_extractor() # Creating Handler
parser.feed(html_data)	# Feeding Data