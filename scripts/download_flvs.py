'''
  Go through videos in video_list.txt  file and
  download them locally to a designated folder
'''

from subprocess import call
import os
import sys
import fileinput
import re
import httplib
import httplib2
import random
import time


fname = sys.argv[1]
dest_file = sys.argv[2]


def get_flvs(fname):
    with open(fname, "r") as f:
        for line in f:
            location = "cld2156@cunix.columbia.edu:" + line
            up = call(["scp", location, dest_file]).stdout.read()
            print "up"
            print up

get_flvs(fname)



up = Popen(["ssh", "cld2156@cunix.columbia.edu"], stdout=PIPE)
text = up.stdout.read()