#!/usr/bin/python3

"""7-add_item module."""
import sys
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file

try:
    obj = load_from_json_file("add_item.json")
except (FileNotFoundError, json.decoder.JSONDecodeError):
    obj = []

obj.extend(sys.argv[1:])
save_to_json_file(obj, "add_item.json")
