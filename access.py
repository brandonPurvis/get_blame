import utils


class Repository():
    def __init__(self, url):
        url_parts = url.split('/')
        self.url = url
        self.name = url_parts[-1] or url_parts[-2]

    def __enter__(self):
        utils.clone_repo(self.url)
        return self


    def __exit__(self, type, value, traceback):
        utils.remove_repo(self.name)

    def __repr__(self):
        return '<{} :{}>'.format(self.__class__, self.name)

    def __str__(self):
        return repr(self)


if __name__ == '__main__':
    url = 'http://github.com/CenterForOpenScience/modular-file-renderer/'
    import os
    with Repository(url) as repo:
        print(repo)
        os.system('ls')
