#!/usr/bin/python
# ---------------- READ ME ---------------------------------------------
# This Script is Created Only For Practise And Educational Purpose Only
# This Script Is Created For https://bitforestinfo.blogspot.in
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
from bs4 import BeautifulSoup
import urllib2, sys

url="http://who.is/whois/"
website=sys.argv[1]

print "[*] Please Wait.... Connecting To Who.is Server.."
htmldata=urllib2.urlopen(url+website).read()
class_name="rawWhois"  # Class For Extraction

try:
    import lxml
    parse=BeautifulSoup(htmldata,'lxml')
    print "[*] Using lxml Module For Fast Extraction"
except:
    parse=BeautifulSoup(htmldata, "html.parser")
    print "[*] Using built-in Html Parser [Slow Extraction. Please Wait ....]"

try:
    container=parse.findAll("div",{'class':class_name})
    sections=container[1:]
    for section in sections:
        extract=section.findAll('div')
        heading=extract[0].text
        print '\n[ ',heading,' ]'
        for i in extract[1].findAll('div'):
            fortab='\t|'
            for j in i.findAll('div'):
                fortab=fortab+'----'
                line=j.text.replace('\n', ' ')
                print fortab,'>', line
except Exception as e:
    print "[ Error ] ", e
    print "[ Last Update : 1 Jan 2017 ]"
    print "[ Script Is Not Updated ]"
    print "[ Sorry! ]"
     
    
