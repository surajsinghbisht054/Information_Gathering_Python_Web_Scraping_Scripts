#!/usr/bin/python

#
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


# Imprt Module
import bs4
import urllib.request, urllib.error, urllib.parse, sys

if len(sys.argv)==1:
    print("[*] Please Provide Domain Name:\n Usages: python link_bs4.py www.examplesite.com\n")
    sys.exit(0)

def parse_url(url):
    try:
    	html=urllib.request.urlopen(url).read() # Reading Html Codes
    except Exception as e:
    	print("[Error] ",e)
    	sys.exit(0)
    parse=bs4.BeautifulSoup(html)   	# Feed Data To bs4
    for i in parse.findAll('a'):		# Searching For link Tag
        if 'href' in list(i.attrs.keys()):	# Searching For Href key
            link=i.attrs['href']
            print(link)
    return 

parse_url(sys.argv[1])
