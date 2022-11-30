# import sys
import os
import time
import argparse
import google.auth
import urllib.request as rqlib
from google.cloud import storage
from google.oauth2 import service_account

def upload_img_gcs(GCP_PROJECT, GCP_BUCKET):
    """
    The library can auto-detect the credentials of Google Cloud Client to use.
    Only if:
    * Before running this sample, run in terminal `gcloud auth application-default login`
    as described in https://cloud.google.com/docs/authentication/external/set-up-adc
    * To ensure, the credentials (default) will available on:\n
    `Linux, macOS: $HOME/.config/gcloud/application_default_credentials.json`;
    `Windows: %APPDATA%/gcloud/application_default_credentials.json`
    https://cloud.google.com/docs/authentication/application-default-credentials#personal
    * For the credentials file (.json) need to copy inside this file.
    """

    for fcd in os.listdir():
        if fcd.endswith('.json'): # U must only give one json file inside
            GCP_CREDS = fcd

    CREDS_AUTH = service_account.Credentials.from_service_account_file(GCP_CREDS)

    scoped_credentials = CREDS_AUTH.with_scopes(
        ['https://www.googleapis.com/auth/cloud-platform'])
    # credentials, project_id = google.auth.default()

    # Setting Credentials using SERVICE ACCOUNT CREDENTIALS if use ADC just remove the 'credentials param'
    storage_client = storage.Client(project=GCP_PROJECT, credentials=CREDS_AUTH)

    buckets_list = storage_client.list_buckets() # list all bucket
    bck_ls = [bc.name for bc in buckets_list if (bc.name in GCP_BUCKET)] # get all bucket name

    if not bool(bck_ls):
        bucket = storage_client.create_bucket(GCP_BUCKET) # make new bucket
    
    bucket = storage_client.get_bucket(GCP_BUCKET) # set to the current bucket
    return bucket

def args_p():
    """Argument to pass into terminal/script"""
    parser = argparse.ArgumentParser(description='> Image Uploader to Google Cloud Storage <')
    parser.add_argument('project_id',type=str,
    metavar='PROJECT_GCP',
    help='Type in your GCP project id (existed)')
        
    parser.add_argument('bucket_name',type=str,
    metavar='BUCKET_GCP',
    help='Type your GCP bucket name (existed or create new)')

    parser.add_argument('-i', '--img_url',type=str,
    metavar='IMAGE_URL',
    help='Type your online image URL',
    default='https://images.unsplash.com/photo-1553550319-d8d5393e1c80?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8c25vdyUyMGhvdXNlfGVufDB8fDB8fA%3D%3D&w=1000&q=80.jpg')

    # "https://wordpress.org/plugins/about/readme.txt" ~ to test for non-image
    
    t = time.localtime()
    current_time = str(time.strftime("%y%m%d%H%M%S", t)) # now time yymmddHHMMSS

    parser.add_argument('-n', '--img_name', type=str,
    metavar='IMAGE_NAME',
    help='Type your online image name for uploaded to the GCS',
    default=f'snow_house_{current_time}.jpg')

    args = parser.parse_args()
    return args

def get_img_online(URL_IMG):
    """Retrieved and opened image from the internet by URL"""
    file = rqlib.urlopen(URL_IMG)
    return file

if __name__ == '__main__':
    try:
        prgs = args_p()

        img_file = get_img_online(prgs.img_url)
        buckt = upload_img_gcs(prgs.project_id, prgs.bucket_name)
        blob = buckt.blob(prgs.img_name)
        blob.upload_from_string(img_file.read(), content_type='text/plain')

        print('image uploaded v')
    except:
        print('failed x')
    finally:
        print('~ thank you for using this script ~')