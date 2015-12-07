from bs4 import BeautifulSoup
from subprocess import call
import urllib
import os
import sys
import fileinput
import re


string_to_find = ("""<embed type="application/x-shockwave-flash" """
                  """src="mediaplayer.swf?file=..%2F..%2Ffiles%2Fvideos%2F221%2FTextCards.flv" """
                  """width="420" height="286" style="undefined" id="movie_player_1" """
                  """name="movie_player_1" bgcolor="#ffffff" quality="high" wmode="transparent" """
                  """autoplay="false" flashvars="file=..%2F..%2Ffiles%2Fvideos%2F221%2FTextCards.flv">""")

other_string = ("""<center><p><span class="caption2"><a class="media {width:420, height:286}" """
                """href="../../files/videos/221/TextCards.flv">Death of Lance Cpl. Sharp; shots """
                """of Sgt. Nathan Harris.</a></span></p></center>""")

example_string = ("""<embed type="application/x-shockwave-flash" """
                  """src="mediaplayer.swf?file=..%2F..%2Ffiles%2Fvideos%2F221%2FTextCards.flv" """
                  """width="420" height="286" style="undefined" id="movie_player_1" """
                  """name="movie_player_1" bgcolor="#ffffff" quality="high" wmode="transparent" """
                  """autoplay="false" flashvars="file=..%2F..%2Ffiles%2Fvideos%2F221%2FTextCards.flv">""")

replacement_string = ("""<iframe width="560" height="315" """
                      """src="https://www.youtube.com/embed/{{unique_video_id_here}}" """
                      """frameborder="0" allowfullscreen></iframe>""")

replacement_one = ("""<iframe width="560" height="315" """
                   """src="https://www.youtube.com/embed/""")

replacement_two = ("""" frameborder="0" allowfullscreen></iframe>""")


'''
Code for decoding... urllib.unquote(string_to_decode).decode('utf8') 
u'../../files/videos/221/TextCards.flv'

>>> urllib.unquote(string_to_find).decode('utf8')
u'<embed type="application/x-shockwave-flash" src="mediaplayer.swf?file=../../files/videos/221/TextCards.flv" width="420" height="286" style="undefined" id="movie_player_1" name="movie_player_1" bgcolor="#ffffff" quality="high" wmode="transparent" autoplay="false" flashvars="file=../../files/videos/221/TextCards.flv">'

scan files... 
look for pattern that looks like the flash tag...
decode
see what video name it matches... 
put video name in iframe tag
replace entire flash tag with new iframe...
'''


file_to_search = sys.argv[1]
dest_file = sys.argv[2]

'''Convert video name to url encoding...'''
# urllib.urlencode()
'''Open file and scan for flash tag'''
'''Get HTML elements related to the video tag'''

'''Load video_list.txt and video_ids.txt'''
# one time script - hard coding is fine for now...
video_list = open('video_list.txt', 'r')
'''read contents of video_ids.txt into memory to avoid reopening and reading each time in the inner loop'''
video_ids = open('video_ids.txt', 'r').readlines()
video_table = {}

'''For each listed case video in video_list.txt find corresponding video id in video_ids.txt...'''
for line in video_list:
    line = line.split('/')
    title = line[-1]
    for l in video_ids:
        l = l.split('\t\t\t\t')
        id_title = l[1].strip('\n')
        # print title
        # print id_title
        if title == id_title:
            # print video_table
            video_table[title] = id_title
            print id_title
            print title


