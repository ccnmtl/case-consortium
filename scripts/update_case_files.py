'''
  Go through all elements of the directory tree, if the folder's name is layout,
  go through all html files in that folder and search for html files with _pid in
  their name, these files should be deleted. After deleting these files, go through
  the text of the remaining html files looking for links to files with _pid in the
  name, update these strings to remove _pid from name
'''
from subprocess import call
import os
import sys
import fileinput


file_to_search = sys.argv[1]


def search_folders(file_name):
    for path, subdirs, files in os.walk(file_name):
        files.sort()
        for f_name in files:
            if "_pid_0" in f_name:
                print "Removing file : " + str(f_name)
                file_path = os.path.join(path, f_name)
                call(["rm", file_path])

    # go over directory second time - # of files
    # to update should be smaller
    for path, subdirs, files in os.walk(file_name):
        files.sort()
        for f_name in files:
            if "case_id_" in f_name:
                print "Updating file " + str(f_name)
                file_path = os.path.join(path, f_name)
                old_string = "_pid_0.html"
                new_string = ".html"
                newfile = open(file_path, 'r+')
                for line in fileinput.input(file_path):
                    newfile.write(line.replace(old_string, new_string))
                newfile.close()


search_folders(file_to_search)
