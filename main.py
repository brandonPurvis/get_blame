from sys import argv

import access
import search

FORMATS = ['txt', 'py', 'mako', 'js', 'md']


def reset_index():
    search.delete_index()
    search.create_index()


def main(repo_url):
    with access.Repository(url) as repo:
        blame = access.Blame(repo)
        for d in blame:
            if d['fname'].split('.')[-1] in FORMATS:
                print(d)
                search.add(d)


if __name__ == '__main__':
    url = argv[1]
    print(url)
    main(url)
