#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#
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
import urllib.request, urllib.error, urllib.parse
import os

# Function For Downloading Html
def main(url):
    try:
        print("[*] Downloading Html Codes ... ", end=' ')
        page = urllib.request.urlopen(url).read()
        print(" Done!")
    except Exception as e:
        print("[Error Found] ",e)
        page=None
    return page

# Function For Downloading Image
def image_download(link):
    #print link
    Saved_in = "WebsitePicturesDownloaded"
    if not os.path.isdir(Saved_in):
        print("[+] Creating Directory... ",Saved_in, end=' ')
        os.mkdir(Saved_in)
        print(" Done")
    img=open(os.path.join(Saved_in, os.path.basename(link)),'wb')
    data=urllib.request.urlopen(link)
    print("[+] Picture Saved As ",os.path.join(Saved_in, os.path.basename(link)))
    img.write(data.read())
    img.close()
    return
