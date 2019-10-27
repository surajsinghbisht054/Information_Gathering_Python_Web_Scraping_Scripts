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
# Import Module
import re

# Function For Extracting Html Link
def main(html_data):
    # Filtering Url links
    print("[*] Extracting Html Links ...")
    pattern = re.compile('(<a .*?>)')
    a_tag_captured = pattern.findall(html_data)
    for i in a_tag_captured:
        href_raw=i[str(i).find('href'):]
        href=href_raw[:href_raw.find(' ')]
        yield href[6:-1]
    print(" Done")
    return

# Function For Extracting Sitemap
def main_sitemap(urls):
    print("[*] Extracting Sitemap ....", end=' ')
    pattern = re.compile('<loc>(.*?)</loc>')
    data=pattern.findall(urls)
    print("Done!")
    return data

# Function For Extracting Image Link
def main_img(html_data):
    print("[*] Extracting Image Links ....", end=' ')
    link=[]
    pattern = re.compile('<img .*?>')
    for i in pattern.findall(html_data):
        i=i[i.find('src'):-2]
        img=i.split(' ')[0]
        if 'http' in img[4:10]:
            link.append(img[5:-1])
    print(' Done')
    return link
    