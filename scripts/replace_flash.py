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


example_string = ("""<embed type="application/x-shockwave-flash" """
                  """src="mediaplayer.swf?file=..%2F..%2Ffiles%2Fvideos%2F221%2FTextCards.flv" """
                  """width="420" height="286" style="undefined" id="movie_player_1" """
                  """name="movie_player_1" bgcolor="#ffffff" quality="high" wmode="transparent" """
                  """autoplay="false" flashvars="file=..%2F..%2Ffiles%2Fvideos%2F221%2FTextCards.flv">""")



'''
    Code for decoding... urllib.unquote(string_to_decode).decode('utf8') 
    u'../../files/videos/221/TextCards.flv'

    >>> urllib.unquote(string_to_find).decode('utf8')
    u'<embed type="application/x-shockwave-flash" src="mediaplayer.swf?file=../../files/videos/221/TextCards.flv" width="420" height="286" style="undefined" id="movie_player_1" name="movie_player_1" bgcolor="#ffffff" quality="high" wmode="transparent" autoplay="false" flashvars="file=../../files/videos/221/TextCards.flv">'
'''




def make_replacement_tag(flvid):
    '''Create replacement link'''
    # width="420" height="286" for embeds...
    # class="media {width:420, height:286}" (for a tags...)
    replacement_one = ("""<iframe width="420" height="286" """
                       """src="https://www.youtube.com/embed/""")
    replacement_two = ("""" frameborder="0" allowfullscreen></iframe>""")
    replacement_string = replacement_one + flvid + replacement_two
    return replacement_string





def open_file_and_replace_tags(htmlfile, flvname2):
    '''Open file and scan for flash tag'''
    htmldoc = open(htmlfile, 'rw')
    soup = BeautifulSoup(htmldoc, 'html.parser')

    '''Get HTML elements related to the video tag
    Videos seem to be in embed tags or center > p > span tags'''
    find_href = soup.find_all(href=re.compile(flvname2))

    '''An HTML element with this flv was found
    TODO: I don't think there will be cases were the name
    is found more than once on a page but should we account
    for it anyway?'''
    if len(find_href) == 1:
        flvid = video_table[flvname2]
        replacement_tag = make_replacement_tag(flvid)
        find_href.replace_with(replacement_tag)
        

    find_embeds = soup.find_all('embed', href=re.compile(flvname2))

    # type="application/x-shockwave-flash"

'''Create output file to log details of script run to - which files were updated'''
def record_transaction():
    pass

'''Traverse directory files for flv...'''
def go_over_directory(directory):
    pass




if __name__ == '__main__':
    argparser.add_argument("--directory", help="Directory of files to traverse",
        default=".")
    argparser.add_argument("--file", help="File to process")
    argparser.add_argument("--record-file", help="File to record processing information to")
    argparser.add_argument("--title", help="Title of flv")
    argparser.add_argument("--id", help="ID of flv on youtube")
    args = argparser.parse_args()

    # irrelevant side note - what is more efficent - saving the replacement strings globally
    # and passing to the replace tag function or creating them within the function

    # one time script - hard coding is fine for now...
    '''For each listed case video in video_ids.txt stick in a dictionary...'''
    video_ids = open('video_ids.txt', 'r') # .readlines()
    video_table = {}

    for l in video_ids:
        l = l.split('\t\t\t\t')
        id_title = l[1].strip('\n')
        video_table[id_title] = l[0]

    video_ids.close()

