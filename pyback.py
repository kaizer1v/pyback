'''
This is a command line application to compress/backup folders

USAGE

`python pyback path/to/source -d compressed_file_name`

TODO
    - source folder cannot be inside the destination folder
    [X] = resolved since now source file is being compressed

    - choose default destination path (if not provided), by creating in '~' directory
    - if destination path doesn't exist, create the path
    - ...
'''
import os
import zipfile
import argparse
from shutil import make_archive


_DESTINATION = '/Users/i536332/Documents/personal_p/py/DEFAULT_DEST_FLDR'
_FORMATS = ['tar', 'gztar', 'zip', 'bztar', 'xztar']

def compress(src, file, frmt):
    '''
    compress src to file name
    '''
    # get absolute path of this
    src_abs = os.path.abspath(src)
    make_archive(file, root_dir=src, format=frmt)


if __name__ == '__main__':
    '''
    Ensures this python file is run like
    `python prj1.py`
    '''
    parser = argparse.ArgumentParser()

    # compulsory argument
    parser.add_argument('source', type=str, help='Enter source path of a directory to be backed-up')

    # destination path - optional argument
    parser.add_argument('-d', '--destination', type=str, default=_DESTINATION, help='Enter expected filename of the compressed file')

    # expected format
    parser.add_argument('-f', '--format', type=str, default=_FORMATS[0], help='Format from one of tar, gztar, zip, bztar, xztar')

    args = parser.parse_args()
    compress(args.source, args.destination, args.format)