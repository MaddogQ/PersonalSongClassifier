# -*- coding: utf-8 -*-
"""
A class that reads and detects the main language in a .lrc file
"""

from langdetect import detect
from Songs.SongDir import SongDir
import re


class LrcReader:

    def __init__(self, file_name):
        assert file_name[-4:] == ".lrc"
        self._name = file_name
        with open(SongDir.path + file_name, 'rb') as f:
            self._file = f.read().decode('utf8', 'ignore')

        self._lrc = ''
        self.handle_lrc()

    def __str__(self):
        return self.get_lrc()

    def handle_lrc(self):
        # a list of lines of lyrics
        lrc_line = []
        for line in self._file.split('\n'):
            # get rid of time stamp
            time_stamps = re.findall(r'\[[^\]]+\]', line)
            if time_stamps:
                lyric = line
                for tPlus in time_stamps:
                    lyric = lyric.replace(tPlus, '')
                    lrc_line.append(lyric)
        # glue processed lyrics together
        for lyric in lrc_line:
            self._lrc += lyric

    def analyze(self):
        return detect(self._lrc)

    def get_lrc(self):
        return self._lrc

    def get_name(self):
        return self._name
