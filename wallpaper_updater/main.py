#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Written By:
#		S.S.B
#		surajsinghbisht054@gmail.com
#		bitforestinfo.blogspot.com
#
#	
# Import Module
import re
import urllib2
import os

# Latest Homepage xml Url
xml_url = 'http://www.bing.com/HPImageArchive.aspx?format=xml&idx=0&n=2&mkt=en-us'

# Fucntion For Extracting Image Url and Image Details From xml
def get_image_details(xml):
	# Url and Details Pattern
	image_url_pattern = '<url>(.*?)</url>.+<copyright>(.*?)</copyright>'
	
	# search patterns 
	(img_url, img_detail) = re.search(image_url_pattern, xml).groups(1)

	# Complete Url
	bing = 'http://www.bing.com'+img_url
	return (bing, img_detail)

# Function for Downloading Image
def download_image(url):
	# Choose Image Name
	filename = url.split('/')[-1]
	img_file = open(filename, 'wb')
	# Download Image
	img_file.write(urllib2.urlopen(url).read())
	# Save Image
	img_file.close()

	# return Image Name
	return filename

# Function For Changing Wallpaper Automatically
def change_wallpaper(filename):
	# Get Absolute Path Of Image
	path = os.path.join(os.path.realpath('.'),filename)
	# Command For Changing Wallpaper
	cmd = 'gsettings set org.gnome.desktop.background picture-uri "file:///{}"'.format(path)
	os.system(cmd)
	return
	
# Main Function
def main():
	# Download Xml Data
	raw_xml = urllib2.urlopen(xml_url).read()

	# Extract Image Url From Xml
	(img_url, img_detail) = get_image_details(raw_xml)

	# Download Image
	filename = download_image(img_url)

	# Change Desktop Wallpaper
	change_wallpaper(filename)

	return

# Main Function Trigger
if __name__ == '__main__':
	main()
