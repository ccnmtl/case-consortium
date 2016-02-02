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


file_to_search = sys.argv[1]


def search_folders(file_name):
    orig_homepage = "case_id_\d+.html"
    dup_homepage = "case_id_\d+_id_\d+.html"
    for path, subdirs, files in os.walk(file_name):
        if path.endswith("layout"):
            '''For each template directory'''
            files.sort()
            potential_dups = []
            home_page = ""
            duplicate_page = ""
            for f_name in files:
                '''Sort filenames'''
                homematchObj = re.match(orig_homepage, f_name)
                dupmatchObj = re.match(dup_homepage, f_name)
                if homematchObj:
                    home_page = f_name
                else:
                    pass
                if dupmatchObj:
                    potential_dups.append(f_name)
                else:
                    pass
            temp = potential_dups[0][:-5].split('_')[4]
            '''Get first of the possible home page duplicates to compare the others to'''
            for each in potential_dups:
                '''Go over potential duplicates and find the homepage'''
                test_num = each[:-5].split('_')[4]
                if test_num < temp:
                    temp = test_num
            ns = home_page.split('.html')[0]
            ns = str(ns) + '_id_' + str(temp) + '.html'
            duplicate_page = ns
            dup_path = os.path.join(path, duplicate_page)
            call(["git", "rm", dup_path])
            for f_name in files:
                '''Go over all files again and look for references to the duplicate page and remove them'''
                if "case_id_" in f_name:
                    '''this will throw an error when it tries to open the deleted file --> put in try block'''
                    file_path = os.path.join(path, f_name)
                    try:
                        newfile = open(file_path, 'r+')
                        for line in fileinput.input(file_path):
                            newfile.write(line.replace(duplicate_page, home_page))
                        newfile.close()
                    except:
                        pass





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


def replace_audio_new_tags(htmlfile):
    f = open(htmlfile, 'r+')
    temphold = f.readlines()
    f.seek(0)
    tempholdlen = len(temphold)

    '''search for old audio file references and replace with audio tags
    '''
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

