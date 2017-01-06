#!/usr/bin/python
# ---------------- READ ME ---------------------------------------------
# This Script is Created Only For Practise And Educational Purpose Only
# This Script Is Created For https://hackworldwithssb.blogspot.in
# This Script is Written By
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
# Importing Module
import urllib2, sys
# =============================================
# 		Configurations
#
header = { 'User-agent' : 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1' }
url='http://www.who.is/whois/'
# =============================================
class Browser:
	def __init__(self):
		"Creating Handler For Extracting Who.is site Webpage"
		self.download_webpage()

	def download_webpage(self):
		domain=sys.argv[1]
		request=urllib2.Request(url, headers=header)
		request=urllib2.urlopen(request)
		self.data=request.read()
		return
if __name__ == '__main__':
	Browser()