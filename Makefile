runserver: 
	hugo server --watch --verboseLog=true --buildDrafts -v --baseUrl=""	

createjs:
	bash scripts/create_json_from_mds.sh

deploy:createjs
	rm -rf public/
	/usr/local/bin/hugo -s . -b 'https://case-consortuim.stage.ccnmtl.columbia.edu/' && \
	s3cmd --acl-public --delete-removed --no-progress sync --no-mime-magic --guess-mime-type public/* s3://case-consortuim.stage.ccnmtl.columbia.edu/

s3-deploy: createjs
	rm -rf public/
	/usr/local/bin/hugo -s . -b 'https://casestudies.ccnmtl.columbia.edu/' && \
	s3cmd --acl-public --delete-removed --no-progress sync --no-mime-magic --guess-mime-type public/* s3://casestudies.ccnmtl.columbia.edu/
