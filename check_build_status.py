import sys
import requests
import argparse
from lxml import etree
import datetime as dt
from dateutil.parser import parse
from veracode_api_signing.plugin_requests import RequestsAuthPluginVeracodeHMAC
from veracode_api_py import VeracodeAPI

def main():

    parser = argparse.ArgumentParser(
        description='This script checks to see if an app is currently building a policy scan and returns 0 if not and 1 otherwise.')
    parser.add_argument('-a', '--app', help='App name to check',required=True)
    args = parser.parse_args()

    data = VeracodeAPI().get_app_list()
    results = etree.fromstring(data)
    found = False
    for app in results:
        if app.attrib["app_name"] == args.app:
           found = True
           build_list = VeracodeAPI().get_build_list(app.attrib["app_id"]) 
           builds=etree.fromstring(build_list)
           for build in builds:
              if 'policy_updated_date' not in build.attrib: 
                 print ('Current build running is ' + build.attrib['version'])
                 exit(1)
           print ('No currently running scans')
           exit(0)
    if found:
       print ('App: '+args.app+' does not exist')
       exit(0)

if __name__ == '__main__':
    main()