from sys import argv

import access
import search

FORMATS = ['txt', 'py', 'mako', 'js', 'md']


if __name__ == '__main__':
    url = argv[1]
    print(url)
    search.delete_index()
    search.create_index()
    with access.Repository(url) as repo:
        blame = access.Blame(repo)
        for d in blame:
            if d['fname'].split('.')[-1] in FORMATS:
                print(d)
                search.add(d)
