from sys import argv
from os import system

def clone_repo(url):
    system('git clone {}'.format(url))


if __name__ == "__main__":
    url = argv[1]
    clone_repo(url)
