'''
This is a command line application to compress/backup folders

USAGE

`python pyback path/to/source -d compressed_file_name`
'''
import os
import argparse
from shutil import make_archive


# _DESTINATION = '/Users/i536332/Documents/personal_p/py/DEFAULT_DEST_FLDR'
_FORMATS = ['tar', 'gztar', 'zip', 'bztar', 'xztar']

def compress(src, file_name, frmt):
    '''
    compress src to `file_name`
    '''
    # default destination path will be adjacent to source folder
    if not file_name:
        file_name = os.path.abspath(os.path.join(src, os.pardir, os.path.basename(src)))

    # get absolute path of this
    src_abs = os.path.abspath(src)
    try:
        make_archive(file_name, root_dir=src, format=frmt)
    except ValueError as e:
        print(e)
        print('Available formats are {}'.format(', '.join(_FORMATS)))


if __name__ == '__main__':
    '''
    Ensures this python file is run like
    `python pyback.py`
    '''
    parser = argparse.ArgumentParser()

    # compulsory argument
    parser.add_argument('source', type=str, help='Enter source path of a directory to be backed-up')

    # destination path - optional argument
    parser.add_argument('-d', '--destination', type=str, help='Enter expected filename of the compressed file')

    # expected format
    parser.add_argument('-f', '--format', type=str, default=_FORMATS[0], help='Format from one of tar, gztar, zip, bztar, xztar')

    args = parser.parse_args()
    compress(args.source, args.destination, args.format)
