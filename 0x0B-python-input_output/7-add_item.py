#!/usr/bin/python3

"""7-add_item module add arguments to a python list and saved to a json file"""
import sys
import json
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file

if __name__ == "__main__":

    try:
        obj = load_from_json_file("add_item.json")
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        obj = []

    obj.extend(sys.argv[1:])
    save_to_json_file(obj, "add_item.json")
