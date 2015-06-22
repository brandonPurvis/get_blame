import logging
import os
import re
from datetime import datetime
from sys import argv

from traverser import TraverseIterator

logger = logging.Logger(__name__)


TEMP_FILENAME = '.temp'


def clone_repo(url):
    os.system('git clone {}'.format(url))


def remove_repo(name):
    os.system('rm -rf {}'.format(name))


def traverse(dir_path):
    ti = TraverseIterator(dir_path)
    return ti


def get_blame(path):
    """ Return the lines of a files `git blame`. 
    """
    directory = path.split('/')[0]
    path = '/'.join(path.split('/')[1:])

    # into projects directory
    os.chdir(directory)
    os.system('pwd')
    os.system('git blame {} > {}'.format(path, TEMP_FILENAME))
    try:
        # Get text from temp file
        with open(TEMP_FILENAME, 'r') as f:
            lines = f.readlines()
    except IOError:
        return []

    # out of projects directory
    os.system('rm {}'.format(TEMP_FILENAME))
    os.chdir('..')
    return lines


def line_to_dict(line):
    LINE_PATTERN = re.compile('\^?([\w\d]+)\s.*\s?\((.+?)\s+([\d[-]+\s[\d:]+)\s-\d+[\s\d]*\)\s(.*)')
    DATE_PATTERN = '%Y-%m-%d %H:%M:%S'
    match = re.match(LINE_PATTERN, line)
    try:
        return {
            'commit': match.group(1),
            'uname': match.group(2),
            'datetime': datetime.strptime(match.group(3), DATE_PATTERN),
            'code': match.group(4),
        }
    except ValueError:
        logger.warning('Failed on {}'.format(line))
        return {
            'commit': match.group(1),
            'uname': match.group(2),
            'datetime': None,
            'code': match.group(4),
        }


if __name__ == "__main__":
    url = argv[1]
    name = url.split('/')[-1] or url.split('/')[-2]
    # print(name)
    clone_repo(url)
    ti = traverse(name)
    for file_ in ti:
         blame_lines = map(line_to_dict, get_blame(file_))
         if blame_lines:
             print(blame_lines[0])
