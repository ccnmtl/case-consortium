'''
  replace current audio files with html5 audio
'''
import fileinput
import os
import re
import sys
import urllib
from bs4 import BeautifulSoup
from bs4 import Comment
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
                soup = BeautifulSoup(htmldoc, "html.parser")
                for img_tag in soup.find_all(has_audio_as_img):
                    '''save location of mp3 file'''
                    mp3_loc = img_tag.get('src')
                    mp3loc = mp3_loc.replace(' ', '&#32;')
                    # print mp3loc
                    paragraph = img_tag.find_parents("p")
                    '''comment out original image audio tag'''
                    audiotag = '<audio controls><source src="' + mp3loc + '" type="audio/mpeg"></audio>'
                    new_comment = Comment(str(img_tag))
                    new_comment = new_comment + audiotag
                    # audiotag = BeautifulSoup(audiotag)
                    # new_comment.extend(audiotag)
                    img_tag.replace_with(new_comment)
                    # parent = new_comment.find_parents("p")
                    # parent.append()
                    #print parent
                    #print type(parent)
                    #audiotag = '<audio controls><source src="' + mp3loc + '" type="audio/mpeg"></audio>'
                    #audiotag = BeautifulSoup(audiotag)#, "html.parser")
                    # paragraph.extend(audiotag)
                    #img_tag.replace_with(new_comment + unicode(audiotag))
                    #img_tag.replace_with(new_comment + str(audiotag))
                    #paragraph = img_tag.find_parents("p")
                    #paragraph.append(audiotag)
                    # p = paragraph.find_parents("p")
                    # print p
                    # print type(paragraph)
                    #print audiotag
                    #print type(audiotag)
                    #parent.append(audiotag)
                    #print parent
                    #print type(parent)
                    #print paragraph
                    #print type(paragraph)
                    newdoc = soup.prettify(soup.original_encoding)
                    htmldoc.close()
                    with open(file_path,"wb") as file:
                        file.write(newdoc)

search_folders(file_to_search)


