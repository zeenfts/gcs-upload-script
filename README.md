# gcs-upload-script
A python script for upload Online File to Google Cloud Storage (GCS) built on Docker

Info:
1. Need Google Cloud Platform (GCP) Account.
2. Docker installed locally.
3. GCloud CLI SDK Installed locally.
4. If above prerequisites already met. `Clone or Download this repository`.
5. Inside GCP you need to go to [Service Account](https://console.cloud.google.com/iam-admin/serviceaccounts) and set the credentials until you get the key (json) - you only need one file!.
6. Copy that key inside this repository locally on your PC (be careful that this can expose it, **no secret!**).
7. Then you can run the script as shown on [this shell file (.sh)](https://github.com/zeenfts/gcs-upload-script/blob/main/run_script.sh), just provide the necessary or correct value inside `< >` brackets.

*<sup>note that this way using Service Account was [not the best](https://cloud.google.com/docs/authentication/provide-credentials-adc)! {Better to use the Application Default Credentials (ADC) -> Works seamslessly without Docker} ©2022</sup>*
