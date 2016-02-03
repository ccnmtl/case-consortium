'''
  Find home page duplicates and delete them, then update links to the duplicate
'''
import fileinput
import os
import re
import sys
import urllib
from bs4 import BeautifulSoup
from subprocess import call


list_of_mp3s = 'mp3_list.txt'
location_of_cases = sys.argv[1]


mp3list = open(list_of_mp3s, 'r+')


def update_audio_tags(location_of_cases):
    file_path = os.path.abspath(location_of_cases)
    # print file_path
    for line in mp3list.readlines():
        fline = line.split('casestudy')
        # case_path = line[0]
        # print case_path
        audio_path = '../..' + str(fline[1])
        #print audio_path
        # case_path = str(line[0]).split('caseconsortium')
        # print case_path
        '''for testing on one case - different path'''
        sline = line.split('casestudies')
        # print sline
        sline = str(sline[1]).split('files')
        # print sline
        # html_pg_path = str(case_path[1]) + 'casestudy/www/layout/'
        html_pg_path = str(sline[0]) + 'casestudy/www/layout/'
        # print html_pg_path
        # dir_path = location_of_cases + html_pg_path
        # print dir_path
        # print os.path.abspath()
        dir_path = os.path.abspath('.') + '/110/'
        #print dir_path
        for path, subdirs, files in os.walk(dir_path):
            # print "print inside loop"
            # print files
            files.sort()
            for f_name in files:
                if f_name.endswith(".html"):
                    # print f_name
                    file_path = os.path.join(path, f_name)
                    html_doc = open(file_path, 'r+')
                    # print html_doc
                    soup = BeautifulSoup(html_doc, 'html.parser')
                    for img_tag in soup.find_all('img'):
                        # print(img_tag.get('src'))
                        if str(img_tag.get('src')) == str(audio_path):
                            print "this file " + f_name + " contains the audio file " + audio_path
     
update_audio_tags(location_of_cases)




