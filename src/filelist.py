import os


class Filelister:
    def __init__(self, directory, with_path=False):
        with open(directory + '/all_files.txt', 'w', newline='\n') as f:
            for root, dirs, files in os.walk(directory, topdown=False):
                if with_path:
                    self._list_with_path(f, root, files)
                else:
                    self._list_without_path(f, files)

    @staticmethod
    def _list_without_path(opened_file, files):
        for file in files:
            opened_file.write(file + '\n')

    @staticmethod
    def _list_with_path(opened_file, root, files):
        for name in files:
            opened_file.write(os.path.join(root, name) + '\n')
