#!/usr/bin/env python3
import shutil
import os

from src.my_logging import Logger


class Copier:
    def __init__(self, source, dest, move=False):
        self.source = source
        self.dest = dest
        self.new_dir = self.get_target_folder()

        self.log = Logger(logging_file=self.dest + '/log_file.txt')

        if os.path.isdir(self.dest + '/' + self.new_dir):
            self._remove_dir(self.dest + '/' + self.new_dir)

        if move:
            self._move()
        else:
            self._copy()

        del self.log

    def get_target_folder(self):
        return self.source.split('/')[-1]

    def _copy(self):
        shutil.copytree(self.source, self.dest + '/' + self.new_dir)
        self.log.log_info(f'Copying {self.source} to {self.source}')

    def _move(self):
        shutil.move(self.source, self.dest, copy_function=shutil.copytree)
        self.log.log_info(f'Moving {self.new_dir} to {self.source}')

    def _remove_dir(self, directory):
        shutil.rmtree(directory)
        self.log.log_info(f'Deleting {directory}')
