#!/usr/bin/python
# -*- coding: utf-8 -*-
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
import urllib
import sys
import os

# Check Provided Arguments
if len(sys.argv)==1:
	print "\n[*] Please Provide File Url Address:\n Usages: python {} www.examplesite.com\\path\\to\\file.zip\n".format(sys.argv[0])
	sys.exit(0)

# Progress Reporter
def progress(blocks, block_size, total_block_size):
	current_received_blocks = blocks * block_size # Calculate Total Block Received

	percent = (100 * current_received_blocks/total_block_size) # Change in percentage
	
	sys.stdout.write('\rPercent : {}%  [{}]'.format(str(percent),str('#'*(percent/10)).ljust(10))) # Print Percentage with prograss bar
	return

# File Name Creator
def filename(url):
	# Return Url Address Base Name
	url_base = os.path.basename(url)

	if '.' in url_base: # If file extension available 
		base = url_base
		print "[+] File Saved As : ",base
	else:
		base = raw_input("[*] File Saved As : ")
	return base

# Download Function
def download(url, file_name):
	print "\n"
	urllib.urlretrieve(url, file_name, progress) # Downloading File
	print "\n\n"
	return

# Main Function For File Name Management
def main(url, fname=None):
	if fname:
		base = fname
	else:
		base = filename(url)

	if base:
		download(url, base)
	return

if __name__ == '__main__':
	main(sys.argv[1])