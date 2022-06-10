from glob import glob
import time
import flask
from flask import Flask, request, redirect, url_for, session, escape, jsonify
import os, subprocess
import base64
import string
from random import *
from pip import main
import requests
import json
import random
import os.path
import requests 
import os.path 
import json 
import random 
HOST=""
USERNAME=""
PASSWORD=""


def get_creds():
    """Parses server host, username and password from a conf file in current directory"""
    with open("creds.txt", "r") as cred_file:
        global HOST, USERNAME, PASSWORD
        all_creds = cred_file.read().split("\n")
        HOST = all_creds[0]
        USERNAME = all_creds[1]
        PASSWORD = all_creds[2]


def get_temperature():
    """Gets the current temperature of the system and returns it to the caller of the function"""
    out = subprocess.Popen(f"ipmitool -I lanplus -H {HOST} -U {USERNAME} -P {PASSWORD} sdr type temperature | grep degrees | cut -d ' ' -f 16", shell=True, stdout=subprocess.PIPE).stdout.read()
    return out


def main():
    get_creds()
    print(get_temperature())


if __name__ == "__main__":
    main()