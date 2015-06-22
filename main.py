from sys import argv

import access
import search

FORMATS = ['txt', 'py', 'mako', 'js', 'md']


def reset_index():
    search.delete_index()
    search.create_index()


def run(repo_url, merged=None):
    with access.Repository(repo_url) as repo:
        blame = access.Blame(repo, merged)
        for d in blame:
            if d['fname'].split('.')[-1] in FORMATS:
                search.add(d)
    print('Done')


if __name__ == '__main__':
    url = argv[1]
    print(url)
    run(url)
