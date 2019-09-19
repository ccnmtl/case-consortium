# VERSION=1.0.0

# Override this variable in your Makefile to use a different hugo
# version than the default on staging / production. For example:
#   HUGO=/usr/local/bin/hugo-0.19
HUGO ?= `which hugo`

S3CMD ?= s3cmd
PUBLIC ?= public
DRAFT_FLAGS ?= --buildDrafts --verboseLog=true -v
PROD_FLAGS ?= -s .
S3_FLAGS ?= --acl-public --delete-removed --no-progress --no-mime-magic --guess-mime-type
INTERMEDIATE_STEPS ?= echo nothing

runserver:
	$(HUGO) $(DRAFT_FLAGS) \
	&& $(INTERMEDIATE_STEPS) \
	&& $(HUGO) server --watch $(DRAFT_FLAGS)

deploy-stage:
	rm -rf $(PUBLIC)/*
	$(HUGO) $(PROD_FLAGS) -b '$(STAGING_URL)' \
	&& $(INTERMEDIATE_STEPS) \
	&& $(S3CMD) $(S3_FLAGS) sync $(PUBLIC)/* s3://$(STAGING_BUCKET)/

deploy-prod:
	rm -rf $(PUBLIC)/*
	$(HUGO) $(PROD_FLAGS) -b '$(PROD_URL)' \
	&& $(INTERMEDIATE_STEPS) \
	&& $(S3CMD) $(S3_FLAGS) sync $(PUBLIC)/* s3://$(PROD_BUCKET)/

.PHONY: runserver deploy-stage deploy-prod
