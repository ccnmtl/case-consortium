'''
  replace current audio files with html5 audio
'''
import fileinput
import os
import re
import sys
import urllib
from bs4 import BeautifulSoup
from bs4 import Comment, NavigableString
from subprocess import call


file_to_search = sys.argv[1]


def has_audio_as_img(tag):
    return tag.has_attr('src') and str(tag.get('src')).endswith(".mp3")


def search_folders(file_name):
    for path, subdirs, files in os.walk(file_name):
        files.sort()
        for f_name in files:
            if f_name.endswith(".html"):
                file_path = os.path.join(path, f_name)
                htmldoc = open(file_path, 'r+')
                audiotag = ''
                '''Use beautiful soup to replace img tag with comment and get
                information on location of audio file'''
                soup = BeautifulSoup(htmldoc, "html5lib")
                for img_tag in soup.find_all(has_audio_as_img):
                    '''save location of mp3 file'''
                    # print "\n\n"
                    # print img_tag
                    mp3_loc = img_tag.get('src')
                    mp3loc = mp3_loc.replace(' ', '&#32;')
                    # print mp3loc
                    '''comment out original image audio tag'''
                    audiotag = '<audio controls><source src="' + mp3loc + '" type="audio/mpeg"></audio>'
                    print audiotag
                    new_comment = Comment(str(img_tag))
                    img_tag.replace_with(new_comment)
                    newdoc = soup.prettify(soup.original_encoding)
                    htmldoc.close()
                    with open(file_path,"wb") as file:
                        file.write(newdoc)
                    file.close()
#                     '''Open the file again and add the html 5 audio tag'''
#                     htmldoc = open(file_path, 'r+')
#                     soup = BeautifulSoup(htmldoc, "html5lib")
#                     comments = soup.findAll(text=lambda text:isinstance(text, Comment))
#                     for comment in comments:
#                         if comment.startswith("<img ") and comment.endswith("/>") and (".mp3" in comment):
#                             getsrc = comment.split("src=")
#                             getsrc = getsrc[-1].strip('/>')
#                             getsrc = getsrc[-1].strip('"')
#                             getsrc = getsrc.replace(' ', '&#32;')
#                             print getsrc
#                             print "getsrc"
#                             # audiotag = NavigableString('<audio controls><source src="' + getsrc + '" type="audio/mpeg"></audio>').encode("ascii")
#                             # audiotag = BeautifulSoup('<audio controls><source src="' + getsrc + '" type="audio/mpeg"></audio>').encode("ascii")
#                             audiotag = '<audio controls><source src="' + getsrc + '" type="audio/mpeg"></audio>'
#                             comment.parent.append(audiotag)
#                             # print comment.parent
#                             print "parent\n\n"
#                             print comment.parent
#                     newdoc = soup.prettify(soup.original_encoding)
#                     htmldoc.close()
#                     with open(file_path,"wb") as file:
#                         file.write(newdoc)
#                     file.close()

#                     '''Couldn't get this working with beautiful soup'''
#                     imgtag = "case_id_\d+.html"
#                     try:
#                         newfile = open(file_path, 'r+')
#                         for line in fileinput.input(file_path):
#                             newfile.write(line.replace(duplicate_page, home_page))
#                         newfile.close()
#                     except:
#                         pass
#                     # <!-- <img alt="" border="0" class="audiofile" src="../../files/audios/305/Fiona2.mp3" /> -->
#                     for each in temphold:
#                         print "in second file loop"
#                         print audiotag
#                         if '<!--<img' in each and '.mp3"' in each:
#                         # if each.startswith('<!--<img') and each.endswith('.mp3"/>-->'):
#                             print "img tag"
#                             print temphold.index(each)
#                             ind = temphold.index(each)
#                             print each
#                             temphold.insert(ind, audiotag)
#                     temphold = "".join(temphold)
#                     f.write(temphold)
#                     f.close()


                

search_folders(file_to_search)


