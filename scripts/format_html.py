import fileinput
import os
import re
import sys
import urllib
from bs4 import BeautifulSoup
from subprocess import call


def clean_html_file(htmlfile):
    f = open(htmlfile, 'r+')
    temphold = f.readlines()
    f.seek(0)
    tempholdlen = len(temphold)

    '''We should go through the last 10 items
    in the list and search for the </body></html>
    tags after finding these we can remove everything 
    after them. In all cases I have seen the invalid html
    is only after the valid closing tags'''
    closingtag = ''
    for i in range(-10, 0):
        pb = temphold[i]
        ph = temphold[i+1]
        if (pb == "</body>" or pb == "</body>\n") and (ph == "</html>" or ph == "</html>\n" ):
            closingtag = i+1
            tempholdlen = tempholdlen + closingtag + 1
            temphold = temphold[:tempholdlen]

    for line in temphold:
        f.write(line)

    f.truncate()
    f.close()


def prettify_html(htmlfile):
    '''finally - make the html human friendly...'''
    htmldoc = open(htmlfile, 'rw')
    soup = BeautifulSoup(htmldoc, 'html.parser')
    newdoc = soup.prettify(soup.original_encoding)
    htmldoc.close()
    with open(htmlfile,"wb") as file:
        file.write(newdoc)


file_to_search = sys.argv[1]


def search_folders(file_name):
    for path, subdirs, files in os.walk(file_name):
        files.sort()
        for f_name in files:
            if "case_id_" in f_name:
                print "Updating file " + str(f_name)
                file_path = os.path.join(path, f_name)
                clean_html_file(file_path)
                # prettify_html(file_path)

 
search_folders(file_to_search)

