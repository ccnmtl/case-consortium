runserver: 
	hugo server --watch --verboseLog=true --buildDrafts -v --baseUrl=""	

createjs:
	bash scripts/create_json_from_mds.sh

deploy:
	rm -rf public/*
	/usr/local/bin/hugo -s . -b 'http://case-consortium.stage.ccnmtl.columbia.edu' && rsync -avp --delete public/ selma.ccnmtl.columbia.edu:/var/www/case-consortium/
