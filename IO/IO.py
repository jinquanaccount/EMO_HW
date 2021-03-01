# -*- coding: utf-8 -*-


import json

#########################
# 读任务写结果
######################
import os


def read_json_file_to_dictionary(json_file=None):
    with open(json_file, 'r') as json_file:
        data = json.load(json_file)
    return data


def read_json_file_to_string(json_file=None):
    with open(json_file, 'r') as json_file:
        data = json.load(json_file)
    data = json.dumps(data)
    return data


def write_json_file_from_dictionary(json_object, json_file=None):
    if not os.path.isfile(json_file):
        fd = open(json_file, mode="w", encoding="utf-8")
        fd.close()
    with open(json_file, 'w') as json_file:
        json.dump(json_object, json_file)
