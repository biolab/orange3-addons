import requests
import json
import os

URL = "https://pypi.org/pypi/{package}/json"


# read add-on list

OFFICIAL_ADDONS = [a.strip() for a in open("OFFICIAL_ADDONS.txt", "rt")]
OFFICIAL_ADDONS = [a for a in OFFICIAL_ADDONS if a]


# query PyPI

package_list = []
for package in OFFICIAL_ADDONS:
    p = requests.get(URL.format(package=package)).json()
    package_list.append(p)
    
with open('list.tmp', 'wt') as f:
    json.dump(package_list, f, sort_keys=True, indent=4)


# verification

with open('list.tmp', "rt") as f:

    json_list = json.load(f)
    names_in_json = [a["info"]["name"] for a in json_list]
    assert names_in_json == OFFICIAL_ADDONS
    
    # are the expected parts there?
    for addon in json_list:
        info = addon["info"]
        _ = info["version"], info["summary"], info["description"], info["package_url"], info["package_url"]


# verification successful

os.rename('list.tmp', "list")

