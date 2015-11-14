'''
  Find videos and upload to youtube
  Copied script from Google developers youtube api:
  https://developers.google.com/youtube/v3/code_samples/python#upload_a_video
'''

from subprocess import call
import os
import sys
import fileinput
import re
import httplib
import httplib2
import random
import time

from apiclient.discovery import build
from apiclient.errors import HttpError
from apiclient.http import MediaFileUpload

from oauth2client.client import flow_from_clientsecrets
from oauth2client.clientsecrets import loadfile
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow


# Explicitly tell the underlying HTTP transport library not to retry, since
# we are handling retry logic ourselves.
httplib2.RETRIES = 1

# Maximum number of times to retry before giving up.
MAX_RETRIES = 10

# Always retry when these exceptions are raised.
RETRIABLE_EXCEPTIONS = (httplib2.HttpLib2Error, IOError, httplib.NotConnected,
    httplib.IncompleteRead, httplib.ImproperConnectionState,
    httplib.CannotSendRequest, httplib.CannotSendHeader,
    httplib.ResponseNotReady, httplib.BadStatusLine)

# Always retry when an apiclient.errors.HttpError with one of these status
# codes is raised.
RETRIABLE_STATUS_CODES = [500, 502, 503, 504]


CLIENT_SECRETS_FILE = "client_secrets.json"

# This OAuth 2.0 access scope allows an application to upload files to the
# authenticated user's YouTube channel, but doesn't allow other types of access.
YOUTUBE_UPLOAD_SCOPE = "https://www.googleapis.com/auth/youtube.upload"
YOUTUBE_READ_WRITE_SCOPE = "https://www.googleapis.com/auth/youtube"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


# This variable defines a message to display if the CLIENT_SECRETS_FILE is
# missing.
MISSING_CLIENT_SECRETS_MESSAGE = """
WARNING: Please configure OAuth 2.0

To make this sample run you will need to populate the client_secrets.json file
found at:

   %s

with information from the Developers Console
https://console.developers.google.com/

For more information about the client_secrets.json file format, please visit:
https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
""" % os.path.abspath(os.path.join(os.path.dirname(__file__),
                                   CLIENT_SECRETS_FILE))

def get_authenticated_service(args):
    storage = Storage(settings.OAUTH_STORAGE_PATH)
    credentials = storage.get()

    if credentials is None or credentials.invalid:
        raise YTAuthError

    return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                 http=credentials.authorize(httplib2.Http()))


class Args(object):
    pass


def get_credentials():
    """ do the oauth dance to get new credentials file """
    args = Args()
    args.logging_level = 'DEBUG'
    args.noauth_local_webserver = 'http://localhost:8000/'
    flow = flow_from_clientsecrets(
        settings.YOUTUBE_CLIENT_SECRETS_FILE,
        # it complains if you don't set something as the redirect_uri,
        # even though it's not used
        redirect_uri="http://localhost:8000/",
        scope=YOUTUBE_UPLOAD_SCOPE)

    storage = Storage("youtube_oauth.json")
    credentials = run_flow(flow, storage, args)
    return credentials


def get_authenticated_service(args):
    flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE,
        scope=YOUTUBE_UPLOAD_SCOPE,
        message=MISSING_CLIENT_SECRETS_MESSAGE)
    storage = Storage("some-oauth2.json")
    credentials = storage.get()
    if credentials is None or credentials.invalid:
        credentials = run_flow(flow, storage, args)

    return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
        http=credentials.authorize(httplib2.Http()))

def initialize_upload(youtube, options):
    tags = None
    if options.keywords:
        tags = options.keywords.split(",")

    body=dict(
        snippet=dict(
        title=options.title,
        description=options.description,
        tags=tags,
        categoryId=options.category
    ),
    status=dict(
        privacyStatus="unlisted"
    )
    )

    # Call the API's videos.insert method to create and upload the video.
    insert_request = youtube.videos().insert(
        part=",".join(body.keys()),
        body=body,
        # The chunksize parameter specifies the size of each chunk of data, in
        # bytes, that will be uploaded at a time. Set a higher value for
        # reliable connections as fewer chunks lead to faster uploads. Set a lower
        # value for better recovery on less reliable connections.
        #
        # Setting "chunksize" equal to -1 in the code below means that the entire
        # file will be uploaded in a single HTTP request. (If the upload fails,
        # it will still be retried where it left off.) This is usually a best
        # practice, but if you're using Python older than 2.6 or if you're
        # running on App Engine, you should set the chunksize to something like
        # 1024 * 1024 (1 megabyte).
        media_body=MediaFileUpload(options.file, chunksize=-1, resumable=True)
    )

    resumable_upload(insert_request)



# The JSON structure below shows the format of a videos resource:
# player.embedHtml
if __name__ == '__main__':
    argparser.add_argument("--directory", help="Directory of files to upload",
        default="Test Description")
    argparser.add_argument("--playlist", help="Playlist",
        default="Test Description")
    argparser.add_argument("--file", help="Video file to upload")
    argparser.add_argument("--title", help="Video title", default="Test Title")
    argparser.add_argument("--privacyStatus", choices=VALID_PRIVACY_STATUSES,
        default=VALID_PRIVACY_STATUSES[0], help="Video privacy status.")
    args = argparser.parse_args()


    youtube = get_authenticated_service(args)
    print youtube
    try:
        for path, subdirs, files in os.walk(directory):
            for file_name in files:
                if ".flv" in file_name: # file_name.endswith(".flv"):
                    print "Uploading file : " + str(file_name)
                    file_path = os.path.join(path, file_name)
                    args.file = file_name
                    print args
                    initialize_upload(youtube, file_path, filename)
    except HttpError, e:
        print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)


#./ve/bin/python upload_videos.py --directory="../ccnmtl-caseconsortium" --privacyStatus="unlisted"


