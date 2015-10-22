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

def get_trail_number(somestring):
    somestring = somestring.split('_')
    sl = somestring[4]
    sl = sl[4].split('.')
    return sl[0]

def potential_homepage(string):
    '''exclude saving numbers for case pages like
    case_id_20_id_53_c_bio.html'''
    pass

def is_casefile(somestring):
    '''only process names of case files - the rest is a waste of time'''
    if somestring.endswith(".html") and "case_id" in somestring:
        return True
    else:
        return False


def replace_homepage(directory):
    '''Still figuring out how to integrate this with the rest of the script'''
    '''Attempt 1 - check if it is a case html file - if so save first case go
    through the filenames - check the length of the name AND if the name has
    a trailing number save that '''
    file_name = os.getcwd()
    print file_name
    shortestname == ""
    '''Should probably move this check to the outer search folders function'''
    if file_name == "layout":
        list = os.listdir(file_name)
        print list
        type(list)
        shortest_file = list[0]
        lowest_number = 0
        for each in list:
            '''We find a case html file with shorter name'''
            print each
            if len(shortest_file) > len(each):
                shortest_file = each



def search_folders(file_name):
    for path, subdirs, files in os.walk(file_name):
        files.sort()
        for f_name in files:
            '''Remove duplicate html files ending with _pid_0.html'''
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

    for path, subdirs, files in os.walk(file_name):
        '''need to account for homepage - has shortest name
        and corresponding duplicate has the lowest ending id number'''
        pass



search_folders(file_to_search)
