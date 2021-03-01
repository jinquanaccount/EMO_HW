# -*- coding: utf-8 -*-


import json

#########################
# 工作文件夹
######################

default_file_to_name = dict(
    default_directory_file="C:/Users/seusmy/Desktop/竞赛",
    default_result_file="default_result_file.json",
    default_raw_file="default_raw_file.json",
)


class Workspace(object):
    def __init__(self, directory=None, raw=None, result=None):
        self._directory = directory
        if self._directory is None:
            self._directory = default_file_to_name['default_directory_file']
        if result is None:
            self._result = directory + '/' + default_file_to_name['default_result_file']
        else:
            self._result = directory + '/' + result
        if raw is None:
            self._raw = directory + '/' + default_file_to_name['default_raw_file.json']
        else:
            self._raw = directory + '/' + raw

    @property
    def directory(self):
        return self._directory

    @property
    def raw(self):
        return self._raw

    @property
    def result(self):
        return self._result
