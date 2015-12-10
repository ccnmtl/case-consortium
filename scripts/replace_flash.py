import BeautifulSoup
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




'''Convert video name to url encoding...'''
# urllib.urlencode()
'''Open file and scan for flash tag'''

def open_file_and_replace_tags(htmlfile, flvname):
    htmldoc = open(htmlfile, 'rw')
    soup = BeautifulSoup(htmldoc, 'html.parser')
    '''Get HTML elements related to the video tag'''
    '''Videos seem to be in embed tags or center > p > span tags'''
    find_href = soup.find_all(href=re.compile(flvname))
    print find_href
    print type(find_href)
    find_embeds = soup.find_all('embed', href=re.compile(flvname))
    print find_embeds
    print type(find_embeds)
    # type="application/x-shockwave-flash"







'''Traverse directory files for flv...'''
def go_over_directory(args.directory):
    pass



youtube = get_authenticated_service(args.)
try:
  initialize_upload(youtube, args)
except HttpError, e:
  print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)



if __name__ == '__main__':
    argparser.add_argument("--directory", help="Directory of files to traverse",
        default=".")
    argparser.add_argument("--file", help="File to process")
    argparser.add_argument("--title", help="Title of flv")
    argparser.add_argument("--id", help="ID of flv on youtube")
    args = argparser.parse_args()

    # one time script - hard coding is fine for now...
    '''For each listed case video in video_ids.txt stick in a dictionary...'''
    video_ids = open('video_ids.txt', 'r') # .readlines()
    video_table = {}

    for l in video_ids:
        l = l.split('\t\t\t\t')
        id_title = l[1].strip('\n')
        video_table[id_title] = l[0]
    video_ids.close()


#   if not os.path.exists(args.file):
#     exit("Please specify a valid file using the --file= parameter.")
# 
#   youtube = get_authenticated_service(args)
#   try:
#     initialize_upload(youtube, args)
#   except HttpError, e:
#     print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)

