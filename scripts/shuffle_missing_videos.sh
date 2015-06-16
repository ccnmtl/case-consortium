# A record of some of the work I did to populate missing videos that wget missed. 

# these videos were loaded by a js, and wget didn't find them.

# first, find the occurances of these videos 
find . -name \*html | xargs grep /casestudy/files/videos > global_videos_raw.txt

# extrace the case id and the video folder id 
perl -n -e 'm#./(\d+)/casestudy.*/casestudy/files/videos/(\d+)/.*#; print "$1,$2 ";' global_videos_raw.txt > global_videos_case_video.txt 

# copy all these videos (about 257) into the appropriate directory 
# the global_videos_case_video.txt contains: case1,videoid1 case2,videoid2, etc
for i in `cat global_videos_case_video.txt`; do caseid=`echo $i | cut -d \, -f 1`; videoid=`echo $i | cut -d \, -f 2`; cp -r /www/data/ccnmtl/draft/sdreher/casestudies/files/videos/${videoid} /www/data/ccnmtl/projects/caseconsortium/casestudies/${caseid}/casestudy/files/videos/; done; 
 
