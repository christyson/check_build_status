# Veracode Python API Credentials Expirt using HMAC Example

A simple example to get the exiration dates of api credentials for your users based off the HMAC example provided here:
https://github.com/veracode/veracode-python-hmac-example

## Setup

Clone this repository:

    git clone https://github.com/christyson/veracode-python-api_credentials_expiry-example

Install dependencies:

    cd veracode-python-api_credentials_expiry-example
    pip install -r requirements.txt

(Optional) Save Veracode API credentials in `~/.veracode/credentials`

    [default]
    veracode_api_key_id = <YOUR_API_KEY_ID>
    veracode_api_key_secret = <YOUR_API_KEY_SECRET>
	
## Run

If you have saved credentials as above you can run:

    python userapiexpiry.py
    
Otherwise you will need to set environment variables before running `example.py`:

    export VERACODE_API_KEY_ID=<YOUR_API_KEY_ID>
    export VERACODE_API_KEY_SECRET=<YOUR_API_KEY_SECRET>
    python userapiexpiry.py
	
NOTE: To be able to use all the endpoints of the Identity REST APIs, you must have one of these account types:

    API service account with the Admin API role.
    user account with the Administrator role.
	
as described here: https://help.veracode.com/go/c_identity_intro