#!/bin/bash

BLOG_DOMAIN=casestudies.jrn.columbia.edu
BLOG_URL=https://casestudies.jrn.columbia.edu/casestudy/www/layout/standard.asp?case_id=148

DOWNLOAD_DIR=${PWD}/casestudies_snapshot

set -x

# clean up after last run                                                                                                                     
#rm -rf $DOWNLOAD_DIR
#mkdir $DOWNLOAD_DIR
cd $DOWNLOAD_DIR

#CASE_IDS="119 85"
CASE_IDS=`cat /usr/local/share/sandboxes/jonah/caseconsortium/caseids_missing.txt`
for case_id in $CASE_IDS; do

    wget --save-cookies ${DOWNLOAD_DIR}/cookies.txt \
	--post-data 'username=XXXXXX&password=YYYYYY' \
	--keep-session-cookies \
	--delete-after \
	https://casestudies.jrn.columbia.edu/casestudy/login.asp

    BLOG_URL=https://casestudies.jrn.columbia.edu/casestudy/www/layout/standard.asp?case_id=${case_id}
    cd $DOWNLOAD_DIR    
    mkdir $case_id
    cd $case_id

    wget \
	--load-cookies ${DOWNLOAD_DIR}/cookies.txt \
	--no-clobber \
	--no-host-directories  \
	--include-directories=/casestudy \
	--convert-links \
	--page-requisites \
	--html-extension \
	--page-requisites \
	--recursive --level=50 \
	--domains="${BLOG_DOMAIN}" \
	$BLOG_URL

done;