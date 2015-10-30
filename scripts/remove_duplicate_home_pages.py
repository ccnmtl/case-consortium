'''
  Find home page duplicates and delete them, then update links to the duplicate
'''
from subprocess import call
import os
import sys
import fileinput
import re


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


search_folders(file_to_search)
