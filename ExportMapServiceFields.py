# Author: @johnshiu

import os
import sys
import urllib
import urllib2
import json
import csv
import ConfigParser

#Retrieves a token from an map server
def get_token(token_url, referer, uname, pword):
    query_dict = {'username': uname, 'password': pword, 'referer': referer }

    query_string = urllib.urlencode(query_dict)
    token_json = json.loads(urllib.urlopen(token_url + "?f=json", query_string).read())

    if "token" not in token_json:
        raise Exception("Error: unable to login to " + token_url + " with credentials.")

    token = token_json['token']

    return token

#Retrieves layer info into JSON
def get_layer_info(fs_url, token, layer_id):
    query_dict = {}
    query_dict["f"] = "json"
    if (token != None):
        query_dict["token"] = token
    
    query_url = fs_url + "/" + str(layer_id) + "?" + urllib.urlencode(query_dict)

    return json.loads(urllib.urlopen(query_url).read())

#Retrieves service info into JSON 
def get_service_info(fs_url, token):
    query_dict = {}
    query_dict["f"] = "json"
    if (token != None):
        query_dict["token"] = token
    
    query_url = fs_url + "?" + urllib.urlencode(query_dict)

    return json.loads(urllib.urlopen(query_url).read())

base_dir = os.path.abspath(os.path.dirname(__file__)) #base current file directory for relative pathing

config = ConfigParser.ConfigParser()
config.read(os.path.join(base_dir, "Settings", "ExportMapServiceFields.ini"))

fs_url = config.get("SETTINGS", "fs_url")
token_url = config.get("SETTINGS", "token_url")
token_ref = config.get("SETTINGS", "token_ref")
token_uname = config.get("SETTINGS", "token_uname")
token_pword = config.get("SETTINGS", "token_pword")

#Get token if needed
token = None
if (token_url != None and token_url != ""):
    token = get_token(token_url, token_ref, token_uname, token_pword)

#Retrieve all layers
fs_info = get_service_info(fs_url, token)

#Retrieve each layer's field information
fs_layers = fs_info["layers"]
fs_tables = fs_info["tables"]

for l in fs_layers:
    l["info"] = get_layer_info(fs_url, token, l["id"])

for t in fs_tables:
    t["info"] = get_layer_info(fs_url, token, t["id"])

#Export each layer's field information into a separate CSV within the service folder
lyrtbls = fs_layers + fs_tables

for l in lyrtbls:
    filename = str(l["id"]).zfill(3) + "_" + l["name"] + ".csv"

    with open(filename, "wb") as csvfile:
        fs_writer = csv.writer(csvfile)
        fs_writer.writerow(["Name", "Type", "Alias", "Editable", "Nullable", "Length"])

        for f in l["info"]["fields"]:
            length = ""
            if (f["type"] == "esriFieldTypeString"):
                length = f["length"]

            fs_writer.writerow([f["name"], f["type"], f["alias"], f["editable"], f["nullable"], length])