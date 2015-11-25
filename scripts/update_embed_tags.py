'''
  For each video that has been uploaded to youtube, 
  Copied script from Google developers youtube api:
  https://developers.google.com/youtube/v3/code_samples/python#upload_a_video
  <iframe width="560" height="315" src="https://www.youtube.com/embed/iNBqh7g2q8c" frameborder="0" allowfullscreen></iframe>
  <embed type="application/x-shockwave-flash" src="mediaplayer.swf?file
  <embed type="application/x-shockwave-flash" src="mediaplayer.swf?file=..%2F..%2Ffiles%2Fvideos%2F221%2FTextCards.flv" width="420" height="286" style="undefined" id="movie_player_1" name="movie_player_1" bgcolor="#ffffff" quality="high" wmode="transparent" autoplay="false" flashvars="file=..%2F..%2Ffiles%2Fvideos%2F221%2FTextCards.flv">
'''

from subprocess import call
import os
import sys
import fileinput
import re


file_to_search = sys.argv[1]


def search_folders(file_name):
    # open video_ids.txt
    with open("video_ids.txt", 'r+') as f:
        for line in f:
            vid_inf = line.split("\t\t\t\t")
            video_id = vid_inf[0]
            video_name = vid_inf[1]
            for path, subdirs, files in os.walk(file_name):
                files.sort()
                for f_name in files:
                    if "case_id_" in f_name:
                        file_path = os.path.join(path, f_name)
                        old_string = '<embed type="application/x-shockwave-flash" src="mediaplayer.swf?file=..%2F..%2Ffiles%2Fvideos%2F222%2F' + video_name + '" width="420" height="286" style="undefined" id="movie_player_1" name="movie_player_1" bgcolor="#ffffff" quality="high" wmode="transparent" autoplay="false" flashvars="file=..%2F..%2Ffiles%2Fvideos%2F222%2FPointingGun.flv">'
                new_string = ".html"
                newfile = open(file_path, 'r+')
                for line in fileinput.input(file_path):
                    newfile.write(line.replace(old_string, new_string))
                newfile.close()

search_folders(file_to_search)

    
    # <embed type="application/x-shockwave-flash" src="mediaplayer.swf?file=..%2F..%2Ffiles%2Fvideos%2F222%2FPointingGun.flv" width="420" height="286" style="undefined" id="movie_player_1" name="movie_player_1" bgcolor="#ffffff" quality="high" wmode="transparent" autoplay="false" flashvars="file=..%2F..%2Ffiles%2Fvideos%2F222%2FPointingGun.flv">
    # split input line, search case html files for the video name
    # find the flv html element.
    def search_folders(file_name):
        
        for path, subdirs, files in os.walk(file_name):
            files.sort()
            for f_name in files:
                '''Remove duplicate html files ending with _pid_0.html'''
                if "_pid_0" in f_name:
                    print "Removing file : " + str(f_name)
                    file_path = os.path.join(path, f_name)
                    call(["git", "rm", file_path])

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
    for line in fileinput.input(file_path):
        newfile.write(line.replace(old_string, new_string))
        newfile.close()
    try:
        for path, subdirs, files in os.walk(args.directory):<div class="media {width:420, height:286}" style="width: 420px; background-color: rgb(255, 255, 255);"><embed type="application/x-shockwave-flash" src="mediaplayer.swf?file=..%2F..%2Ffiles%2Fvideos%2F222%2FPointingGun.flv" width="420" height="286" style="undefined" id="movie_player_1" name="movie_player_1" bgcolor="#ffffff" quality="high" wmode="transparent" autoplay="false" flashvars="file=..%2F..%2Ffiles%2Fvideos%2F222%2FPointingGun.flv"><div>Nathan frequently played with loaded guns.</div></div>
            for file_name in files:
                if ".flv" in file_name: # file_name.endswith(".flv"):
                    file_path = os.path.join(path, file_name)
                    initialize_upload(youtube, args, file_path, file_name)
    except HttpError, e:
        print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)


#./ve/bin/python update_embed_tags.py





