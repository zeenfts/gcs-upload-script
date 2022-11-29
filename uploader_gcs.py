from google.cloud import storage

def authenticate_implicit_with_adc(project_id="your-google-cloud-project-id"):
    """
    The library can auto-detect the credentials of Google Cloud Client to use.

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

if __name__ == '__main__':
    try:
        authenticate_implicit_with_adc('abc')
        print('test')
    except:
        print('failed!!!')
    finally:
        print('~ thank you for using this script ~')