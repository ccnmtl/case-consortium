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
    for i in range(-10, 0): #(i = -10, i < 0 , i = i +1):
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

#     if temphold[0] == '\n' and temphold[1] == '\n':
#         '''If first two lines are blank get rid of them'''
#         rml = len(temphold) - 2
#         temphold = temphold[-rml:]
#  
# 
#     '''Remove blank lines from end of file - probably a better/smarter way to do this...'''
# 
# 
#     if temphold[-1] == '\n':
#         rml = len(temphold) - 1
#         temphold = temphold[:rml]
# 
# 
#     if temphold[-1] == '\n':
#         rml = len(temphold) - 1
#         temphold = temphold[:rml]
# 
# 
#     if temphold[-1] == '\n':
#         rml = len(temphold) - 1
#         temphold = temphold[:rml]
# 
# 
#     if temphold[-1] == '\n':
#         rml = len(temphold) - 1
#         temphold = temphold[:rml]
# 
# 
#     if temphold[-1] == '\n':
#         rml = len(temphold) - 1
#         temphold = temphold[:rml]
# 
# 
#     '''clean up bottom of document so beautiful soup doesn't
#     get confused and start formatting it further...'''
# 
# 
#     if temphold[-1] == '/html>':
#         rml = len(temphold) - 1
#         temphold = temphold[:rml]
# 
#     if temphold[-1] == '</html>' and temphold[-3] == '</html>' :
#         rml = len(temphold) - 1
#         temphold = temphold[:rml]
# 
#     if temphold[-1] == 'dy>':
#         rml = len(temphold) - 1
#         temphold = temphold[:rml]
# 
#     if temphold[-1] == '/html>\n':
#         rml = len(temphold) - 1
#         temphold = temphold[:rml]
# 
#     if temphold[-1] == '</html>\n' and temphold[-3] == '</html>\n' :
#         rml = len(temphold) - 1
#         temphold = temphold[:rml]
# 
#     if temphold[-1] == 'dy>\n':
#         rml = len(temphold) - 1
#         temphold = temphold[:rml]
# 
#     for line in temphold:
#         f.write(line)
# 
#     f.truncate()
#     f.close()


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

