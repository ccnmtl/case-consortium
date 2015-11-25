bootstrap:
	python ./virtualenv.py --extra-search-dir requirements/virtualenv_support ve
	ve/bin/pip install --requirement requirements/requirements.txt

clean-creds:
	rm like_video.py-oauth2.json
	rm upload_video.py-oauth2.json

clean:
	rm like_video.py-oauth2.json
	rm upload_video.py-oauth2.json
	rm -rf ve