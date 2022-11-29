import os
import sys
import argparse
from google.cloud import storage

def authenticate_implicit_with_adc(project_id="your-google-cloud-project-id"):
    """
    The library can auto-detect the credentials of Google Cloud Client to use.
    Only if:

    * Before running this sample, run in terminal `gcloud auth application-default login`
    as described in https://cloud.google.com/docs/authentication/external/set-up-adc
    * To ensure, the credentials (default) will available on:\n
    `Linux, macOS: $HOME/.config/gcloud/application_default_credentials.json`;
    `Windows: %APPDATA%/gcloud/application_default_credentials.json`
    https://cloud.google.com/docs/authentication/application-default-credentials#personal
    """
    storage_client = storage.Client(project=project_id)
    buckets = storage_client.list_buckets()
    print("Buckets:")
    for bucket in buckets:
        print(bucket.name)
    print("Listed all storage buckets.")

def args_p():
    parser = argparse.ArgumentParser(description='input for gcp_project_id, gcp_bucket_name, and image_url')
    parser.add_argument('project_id', type=str, help='Type in your GCP project id')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    try:
        authenticate_implicit_with_adc(args_p().project_id)
        print('image uploaded')
    except:
        print('failed!!!')
    finally:
        print('~ thank you for using this script ~')