from sys import argv
from os import system

from traverser import TraverseIterator


def clone_repo(url):
    system('git clone {}'.format(url))


def traverse(path):
    ti = TraverseIterator(path)
    for file_ in ti:
        print(file_)


if __name__ == "__main__":
    url = argv[1]
    name = url.split('/')[-1] or url.split('/')[-2]
    print(name)
    clone_repo(url)
    traverse(name)
