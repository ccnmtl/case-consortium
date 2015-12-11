
from bs4 import BeautifulSoup
from subprocess import call
import urllib
import os
import sys
import fileinput
import re


htmlfile = "case_id_110_id_760.html"
flvname = "Flashback2.flv"
flvname2 = "AfghanSoldier.flv"
htmldoc = open(htmlfile, 'rw')
soup = BeautifulSoup(htmldoc, 'html.parser')
find_href = soup.find_all(href=re.compile(flvname))
video_ids = open('video_ids.txt', 'r')
video_table = {}

for l in video_ids:
    l = l.split('\t\t\t\t')
    id_title = l[1].strip('\n')
    video_table[id_title] = l[0]

video_ids.close()

flvid = video_table[flvname]

def make_replacement_tag(flvid):
    replacement_one = ("""<iframe width="420" height="286" """
                       """src="https://www.youtube.com/embed/""")
    replacement_two = ("""" frameborder="0" allowfullscreen></iframe>""")
    replacement_string = replacement_one + flvid + replacement_two
    return replacement_string


replacement_tag = make_replacement_tag(flvid)
replacement_tag = BeautifulSoup(replacement_tag)
find_href[0].replace_with(replacement_tag)

newdoc = soup.prettify(soup.original_encoding)


htmldoc.close()


with open(htmlfile,"wb") as file:
    file.write(newdoc) # should I close?


'''Convert video name to url encoding...'''
# urllib.urlencode()
