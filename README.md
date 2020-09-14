# Veracode Check Build Status

A simple example script to check if a Veracode app profile is currently running a scan.

## Setup

Clone this repository:

    git clone https://github.com/christyson/check_build_status

Install dependencies:

    cd check_build_status
    pip install -r requirements.txt

(Optional) Save Veracode API credentials in `~/.veracode/credentials`

    [default]
    veracode_api_key_id = <YOUR_API_KEY_ID>
    veracode_api_key_secret = <YOUR_API_KEY_SECRET>

## usage

usage: check_build_status.py [-h] -a APP

## Run

If you have saved credentials as above you can run:

    python check_build_status.py -a <your app name>
    
Otherwise you will need to set environment variables before running `example.py`:

    export VERACODE_API_KEY_ID=<YOUR_API_KEY_ID>
    export VERACODE_API_KEY_SECRET=<YOUR_API_KEY_SECRET>
    python check_build_status.py -a <your app name>
	
NOTE: To be able to use all the endpoints of the Identity REST APIs, you must have one of these account types:

    API service account with the Admin API role.
    user account with the Administrator role.
	
as described here: https://help.veracode.com/go/c_identity_intro
