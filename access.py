import utils


class Repository(object):
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


class Blame(object):
    def __init__(self, repo, merged=False):
        self.repo = repo
        self.merged = merged

    def __iter__(self):
        file_paths = utils.traverse(self.repo.name)
        for file_ in file_paths:
            dicts = []
            for line in utils.get_blame(file_):
                new_dict = utils.line_to_dict(line)
                self.expand_dict(new_dict, file_)
                dicts.append(new_dict)
            if self.merged:
                dicts = self.merge(dicts)
            for d in dicts:
                yield d

    def get(self):
        return [d for d in self]

    def expand_dict(self, d, filepath):
        path_parts = filepath.split('/')
        d['path'] = path_parts[:-1]
        d['fname'] = path_parts[-1]

    def merge(self, dict_list):
        merged = {}
        for d in dict_list:
            c = merged.get(d['uname'], {k: v for k, v in d.items() if k != 'code'})
            code = c.get('code', [])
            code.append(d['code'])
            c['code'] = code
            merged[c['uname']] = c
        print(merged)
        return [d for k, d in merged.items()]

if __name__ == '__main__':
    from pprint import pprint
    url = 'http://github.com/CenterForOpenScience/osf.io/'
    import os
    with Repository(url) as repo:
        print(repo)
        blame = Blame(repo)
        pprint(blame.get()[:5])
        os.system('ls')
