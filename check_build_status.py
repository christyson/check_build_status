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
        description='This script checks to see if an app is currently building a policy scan and returns 0 if not and 1 otherwise. Note: Sandbox is optional')
    parser.add_argument('-a', '--app', help='App name to check',required=True)
    parser.add_argument('-s', '--sandbox', default="", help='App name to check',required=False)
    args = parser.parse_args()

    data = VeracodeAPI().get_app_list()
    results = etree.fromstring(data)
    found = False
    for app in results:
        if (app.attrib["app_name"] == args.app) and (args.sandbox == ""):
           found = True
           build_list = VeracodeAPI().get_build_list(app.attrib["app_id"]) 
           builds=etree.fromstring(build_list)
           for build in builds:
              if 'policy_updated_date' not in build.attrib: 
                 print ('Current build running is ' + build.attrib['version'])
                 exit(1)
           print ('No currently running scans in app: '+args.app)
           exit(0)
        if (app.attrib["app_name"] == args.app) and (args.sandbox != ""):
           sandbox_list=VeracodeAPI().get_sandbox_list(app.attrib["app_id"])
           sandboxes = etree.fromstring(sandbox_list)
           for sandbox in sandboxes:
              if sandbox.attrib["sandbox_name"] == args.sandbox:
                 found = True
                 build_list = VeracodeAPI().get_build_list(app.attrib["app_id"], sandbox.attrib["sandbox_id"]) 
                 builds=etree.fromstring(build_list)
                 for build in builds:
                    build_info = VeracodeAPI().get_build_info(app.attrib["app_id"], build.attrib["build_id"],sandbox.attrib["sandbox_id"])
                    if 'results_ready="false"' in str(build_info): 
                       print ('Current build running in sandbox '+ sandbox.attrib["sandbox_name"]+' is ' + build.attrib['version'])
                       exit(1)
                 print ('No currently running scans in sandbox: '+args.sandbox+' of app: '+args.app)
                 exit(0)
    if (not found) and (args.sandbox == ""):
       print ('App: '+args.app+' does not exist')
    elif (not found) and (args.sandbox != ""):
       print ('App: '+args.app+' with sandbox: '+args.sandbox+' does not exist')
    exit(0)

if __name__ == '__main__':
    main()