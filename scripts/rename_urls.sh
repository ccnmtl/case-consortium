#
# Steps to rename all the case files and their urls, that were wgotten
#

# change the filenames
cd /www/data/ccnmtl/projects/caseconsortium_jonah
for dir in `ls`; do 
    cd $dir/casestudy/www/layout; 
    for f in *html; do 
	newname="$(echo $f | sed s/standard.asp?// | sed s/=/_/g | sed s/\&/_/g)"; 
	git mv $f $newname; 
    done; 
    cd /www/data/ccnmtl/projects/caseconsortium_jonah/casestudies; 
done;

# update the internal links to match the new filenames
find . -name \*.html | perl -pi -e "s#standard.asp%3Fcase_id=#case_id_#g"
find . -name \*.html | perl -pi -e "s#&amp;id=#_id_#g"
find . -name \*.html | perl -pi -e "s#&amp;pid=#_pid_#g" 
find . -name \*.html | perl -pi -e "s#&amp;c=#_c_#g" 
