# Veracode Check Build Status

A simple example script to check if a Veracode app profile (or sandbox) is currently running a scan.
If a build is running you can delete it if you have the appropriate permissions using the --delete option.

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

usage: check_build_status.py [-h] -a APP [-s SANDBOX] [--delete]

Note: at a minimum APP is required and if there are builds running it exit with a 1 otherwise a 0  

## Run

If you have saved credentials as above you can run:

    python check_build_status.py -a <your app name>
    or
    python check_build_status.py -a <your app name> -s <your sandbox name>

To delete use the following commands:

    python check_build_status.py -a <your app name> --delete
    or
    python check_build_status.py -a <your app name> -s <your sandbox name> --delete


Otherwise you will need to set environment variables before running `example.py`:

    export VERACODE_API_KEY_ID=<YOUR_API_KEY_ID>
    export VERACODE_API_KEY_SECRET=<YOUR_API_KEY_SECRET>
    python check_build_status.py -a <your app name>
    or
    python check_build_status.py -a <your app name> -s <your sandbox name>
