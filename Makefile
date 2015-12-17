STAGING_URL=https://case-consortium.stage.ccnmtl.columbia.edu/
PROD_URL=https://casestudies.ccnmtl.columbia.edu/
STAGING_BUCKET=case-consortium.stage.ccnmtl.columbia.edu
PROD_BUCKET=casestudies.ccnmtl.columbia.edu
INTERMEDIATE_STEPS ?= make $(PUBLIC)/js/api/cases.json

JS_FILES=static/js/facetedsearch.js static/js/FeedEk.js static/js/main.js static/js/search.js static/js/util.js

all: jshint jscs

include *.mk

$(PUBLIC)/js/api/cases.json: $(PUBLIC)/json/index.html
	mv $< $@

# jenkins still expects some other target names
deploy: deploy-stage

s3-deploy: deploy-prod
