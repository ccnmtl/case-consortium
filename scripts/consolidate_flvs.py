'''
    Go through videos in video_list.txt file and
    move to one directory
'''

from subprocess import call
import os
import sys
import fileinput


fname = sys.argv[1]
dest_file = sys.argv[2]


def get_flvs(fname, dest_file):
    with open(fname, "r") as f:
        for line in f:
            line = line.rstrip('\n')
            up = call(["cp", line, dest_file])

get_flvs(fname, dest_file)
