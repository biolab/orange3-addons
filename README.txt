ORANGE ADD-ON LISTS

Orange3 allows installation of add-ons from the add-on dialog, which
is populated by add-ons from OFFICIAL_ADDONS.txt.

The script generate.py generates a file named "list", which contains
a list of package descriptions for official add-ons obtained through
PyPI's JSON API. The file "list" has to be served at
https://orange.biolab.si/addons/list

To modify the list of official add-ons, make a pull request with
corresponding OFFICIAL_ADDONS.txt edits.