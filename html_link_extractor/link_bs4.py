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
# Imprt Module
import bs4
import urllib2, sys

if len(sys.argv)==1:
    print "[*] Please Provide Domain Name:\n Usages: python link_bs4.py www.examplesite.com\n"
    sys.exit(0)

def parse_url(url):
    try:
    	html=urllib2.urlopen(url).read() # Reading Html Codes
    except Exception as e:
    	print "[Error] ",e
    	sys.exit(0)
    parse=bs4.BeautifulSoup(html)   	# Feed Data To bs4
    for i in parse.findAll('a'):		# Searching For link Tag
        if 'href' in i.attrs.keys():	# Searching For Href key
            link=i.attrs['href']
            print link
    return 

parse_url(sys.argv[1])