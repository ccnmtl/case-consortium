from subprocess import call
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