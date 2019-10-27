#!/usr/bin/python

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

# Import Module   
import urllib.request, urllib.error, urllib.parse
import time
import sys


def main(multi_times):
	starting_check_point = time.time()		# Timer Starting Point 
	print("[+] Test Started On : ", time.ctime(starting_check_point))
	download_data = []						# For Collecting Downloaded Data
	for i in range(multi_times):			# Use Any Website Page
			data = urllib.request.urlopen("https://en.wikipedia.org/wiki/Internet").read()
			download_data.append(sys.getsizeof(data))		# Calculating WebPage Size
	ending_check_point = time.time()		# Time Closing Point
	print("[+] Test Closed On : ",time.ctime(ending_check_point))
	total_data_size = sum(download_data)	# Calculating Total Size of Downloaded data
	total_time_used = ending_check_point - starting_check_point	# Calculating Total Time
	one_byte_equal_to = 1024				
	speed = int(total_data_size/total_time_used/one_byte_equal_to)	# Calculating Average Speed
	print("[+] Average InterNet Speed : {} KB".format(speed))

    
if __name__=='__main__':
	main(5)
input('[ Thanks For USing! Have A Nice Day ]')
