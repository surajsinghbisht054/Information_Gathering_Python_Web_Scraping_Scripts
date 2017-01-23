#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Written By:
#       S.S.B
#       surajsinghbisht054@gmail.com
#       bitforestinfo.blogspot.com
#  
# Import Module 
import sys
import Gethtml
import Getlink

links=[]
if len(sys.argv)==2:
    print "\n[*] Usages : python {} http://www.examplesite.com  option_number\n".format(sys.argv[0])
    print "\t[-] Option [-]\n\n1. Current Page Links and Images \n2. Current Page Links \n3. Current Page Image \n4. Website Images \n5. Website Links"
    sys.exit(0)
    pass

# Option Argument
option=int(sys.argv[2])
url=sys.argv[1]

# Current Page Links and Images
if option==1:
    print "[*] Step (1/2)"
    html=Gethtml.main(url)
    for i in Getlink.main_img(html):
        Gethtml.image_download(i)
    print "[*] Step (2/2)"
    save_in='links.txt'
    html=Gethtml.main(url)
    data=Getlink.main(html)
    fileobj=open(save_in,'w')
    fileobj.write(''.join(i+'\n' for i in data))
    fileobj.close()
    print "[*] Url Saved In : ",save_in
    print "[*] Done!"

# For Current Page All Links
elif option==2:
    save_in='links.txt'
    html=Gethtml.main(url)
    data=Getlink.main(html)
    fileobj=open(save_in,'w')
    fileobj.write(''.join(i+'\n' for i in data))
    fileobj.close()
    print "[*] Url Saved In : ",save_in
    print "[*] Done!"
    
# For Current Page All Images
elif option==3:
    html=Gethtml.main(url)
    for i in Getlink.main_img(html):
        Gethtml.image_download(i)
    
# For All Website Image
elif option==4:
    print "[+] Enter Sitemap Url : www.examplesite.com/sitemap?page=1"
    sitemap =  raw_input("[+] Enter Sitemap Url : ")
    html=Gethtml.main(sitemap)
    for i in Getlink.main_sitemap(html):
        Gethtml.image_download(i)
    
# For All Links For Website
elif option==5:
    save_in='links.txt'
    print "[+] Enter Sitemap Url : www.examplesite.com/sitemap?page=1"
    sitemap =  raw_input("[+] Enter Sitemap Url : ")
    html=Gethtml.main(sitemap)
    data=Getlink.main_sitemap(html)
    fileobj=open(save_in,'w')
    fileobj.write(''.join(i+'\n' for i in data))
    fileobj.close()
    
else:
    print " [*] Unknown Option : {}".format(str(option))