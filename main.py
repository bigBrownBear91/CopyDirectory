#!/usr/bin/env python3
import sys
from src.main import CopyAndList, OnlyList

if '--help' in sys.argv[1:] or '-h' in sys.argv[1:]:
    print("""Move or copy a directory to a new directory. In the destination folder a log-file will be created. 
    Moreover, in the moved directory will be created a .txt-file with a list of all files contained in the moved folder.
    Necessary arguments are the directories to be moved. If only one directory is given, only the file list is made.
    
    -w\t\t\tIf given, the .txt-file listing all files will list the full path to the files
    -m\t\t\tIf given, the directory will be moved instead of copied
    -v\t--version\tOutput version information 
    -h\t--help\t\tOtput this help
    """)
    quit()

if '--version' in sys.argv[1:] or '-v' in sys.argv[1:]:
    print("""Dircopier 1.0""")
    quit()


opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

source_dir = args[0]  # '/home/danilo/Downloads/vouchers'
dest_dir = args[1]  # '/home/danilo/Documents'

with_path = False
if '-w' in opts:
    with_path = True

move = False
if '-m' in opts:
    move = True

if dest_dir:
    copyandlist = CopyAndList(source_dir, dest_dir, with_path, move)
else:
    OnlyList(source_dir, with_path)
