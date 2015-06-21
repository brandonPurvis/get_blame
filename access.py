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


class Blame():
    def __init__(self, repo):
        self.repo = repo
    
    def get(self):
        file_paths = utils.traverse(self.repo.name)
        dicts = []
        for file_ in file_paths:
            print(file_)
            for line in utils.get_blame(file_):
                dicts.append(utils.line_to_dict(line))
        return dicts


if __name__ == '__main__':
    url = 'http://github.com/CenterForOpenScience/osf.io/'
    import os
    with Repository(url) as repo:
        print(repo)
        blame = Blame(repo)
        print(blame.get())
        os.system('ls')
