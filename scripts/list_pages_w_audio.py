from subprocess import call
import os
import sys
import fileinput
import re

staging_site_1 = "http://ccnmtl.columbia.edu/projects/caseconsortium_stage/casestudies/"
staging_site_2 = "/casestudy/www/layout/"

file_to_search = sys.argv[1]

def search_folders(file_name):
    listmp3txt = "/home/oskmey/ccnmtl_github/case-consortium/scripts/pages_w_audio.txt"
    listmp3file = open(listmp3txt, 'a+')
    for path, subdirs, files in os.walk(file_name):
        files.sort()
        for f_name in files:
            if f_name.endswith(".html"):
                file_path = os.path.join(path, f_name)
                htmldoc = open(file_path, 'r').read()
                if "mp3" in htmldoc:
                    print f_name
                    num = f_name.split("_")
                    num = num[2]
                    # print num
                    link = staging_site_1 + str(num) + staging_site_2 + f_name + "\n"
                    print link
                    listmp3file.write(link)
                # hasmp3 = re.match(mp3, f_name)
                # print hasmp3
                # if hasmp3:
                #     print f_name


search_folders(file_to_search)
