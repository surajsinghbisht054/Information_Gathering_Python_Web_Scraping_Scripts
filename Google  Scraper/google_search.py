#!/usr/bin/python
# -*- coding: utf-8 -*-
##
#
##################################################
######## Please Don't Remove Author Name #########
############### Thanks ###########################
##################################################
#
#
# Written By:
#       S.S.B
#       surajsinghbisht054@gmail.com
#       bitforestinfo.blogspot.com
#   
# Import Modules
import urllib2
import urllib
import cookielib
import re

# Google Url
google ='https://www.google.com/search?{}&start={}'
Page='1'

# Search Query
Query = "BitForestInfo"

# Create Function
def search(Query, google):

	# Set User Agent
	header = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0 Iceweasel/31.8.0')]

	# Create Cookie Handler
	cj = cookielib.CookieJar()

	# Create Url Handler 
	url_opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj),  # Connect Cookie Jar
    	                              urllib2.HTTPRedirectHandler())    # Address Redirect Handling Function

	# Connect Header With Opener
	url_opener.addheaders=header

	# Encode Query With Url 
	query = google.format(urllib.urlencode({'q':Query}),str(Page))

	# Now Open Google Search Page
	html = url_opener.open(query)

	# Collect Html Code
	codes = html.read()

	pattern = re.compile('<h3(.*?)</h3')
	collect_result = []
	for i in pattern.findall(codes):
		try:
			result = re.search('href=.(.*)..(onmousedown).+(>)([^><]+)(<)',i).groups()
			collect_result.append((result[0],result[3]))
		except:
			pass

	return collect_result

if __name__ == '__main__':
	for i in search(Query, google):
		print i