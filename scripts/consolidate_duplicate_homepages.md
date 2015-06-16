# some post wget work to consolidate case home pages that have two different urls

# First, find the actual ids of the home pages
# e.g. case_id_1.html and case_id_1_id_18.html are both the same page

find . -regextype grep -regex ".*/[0-9]\+/casestudy/www/layout/case_id_[0-9]\+.html" | xargs grep Title > home_page_ids_raw.txt

# extract the caseid and the alternate page name
perl -n -e 'm#./(\d+)/casestudy.*href="(case_id_\d+_id_\d+.html).*#; print "$1,$2 ";' home_page_ids_raw.txt > home_page_ids.txt 

# remove the duplicate pages from git and the fs
for i in `cat home_page_ids.txt`; do caseid=`echo $i | cut -d \, -f 1`; homepageid=`echo $i | cut -d \, -f 2`; git rm $caseid/casestudy/www/layout/$homepageid ; done

# create symlinks to the real page
for i in `cat home_page_ids.txt`; do caseid=`echo $i | cut -d \, -f 1`; homepageid=`echo $i | cut -d \, -f 2`; ln -fs ./case_id_${caseid}.html $caseid/casestudy/www/layout/$homepageid ; done;

# git commit, push, done.
