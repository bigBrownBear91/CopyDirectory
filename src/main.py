from .copy import Copier
from .filelist import Filelister


class CopyAndList:
    def __init__(self, source_dir, dest_dir, with_path=False, move=False):
        copy = Copier(source_dir, dest_dir, move)

        new_dir = copy.get_target_folder()
        Filelister(dest_dir + '/' + new_dir, with_path)


class OnlyList:
    def __init__(self, dir, with_path=False):
        new_dir = Copier(dir).get_target_folder()

        Filelister(dir + '/' + new_dir, with_path)
