# -*- coding: utf-8 -*-
"""
A class that implements LrcReader and sorts songs by the language of its lyrics
"""

from Songs.LrcReader import LrcReader
from Songs.SongDir import SongDir
import os
import shutil


class SongSorter:

    def __init__(self, path = SongDir.path):
        self._path = path
        self._lrc_reader = []
        self._songs = {}
        self._folders_name = ['IDOLM@STER', 'Rock', 'Russian', '中文', '日本語']

    def __str__(self):
        return "Current Path is" + self._path

    def process_all_files(self):
        all_files = os.listdir(self._path)
        for file in all_files:
            extension = file[-4:]
            if extension == '.lrc':
                self._lrc_reader.append(LrcReader(file))
            elif extension in ['.mp3', '.flac', '.ncm']:
                self._songs[str(file)] = 

    def sort(self):
        assert len(self._lrc_reader) != 0
        for lrc in self._lrc_reader:
            lang = lrc.analyze()
            print(lang)
            if lang == 'zh-cn':
                shutil.move(self._path + lrc.get_name(), self._path + '中文')
                shutil.move(self._path + lrc.get_name()[:-4] + '.mp3', self._path + '中文')
            elif lang == 'en':
                pass
            elif lang == 'ru':
                shutil.move(self._path + lrc.get_name(), self._path + 'Russian')
                shutil.move(self._path + lrc.get_name()[:-4] + '.mp3', self._path + 'Russian')
            elif lang == 'ja':
                shutil.move(self._path + lrc.get_name(), self._path + '日本語')
                shutil.move(self._path + lrc.get_name()[:-4] + '.mp3', self._path + '日本語')

    def get_lrc_reader(self):
        return self._lrc_reader


test = SongSorter()
test.process_all_files()
test.sort()
