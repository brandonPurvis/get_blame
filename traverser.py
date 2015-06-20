import os


class TraverseIterator(object):

    def __init__(self, path):
        self.walker = os.walk(path)

    def __iter__(self):
        for path, directories, files in self.walker:
            self.prune(directories)
            for file_ in files:
                yield '/'.join([path, file_])

    def directory_is_parsed(self, dir_name):
        return not (dir_name[0] in ['.', '_'])

    def prune(self, directories):
        to_remove = [d for d in directories if not self.directory_is_parsed(d)]
        for d in to_remove:
            directories.remove(d)


if __name__ == '__main__':
    walker = TraverseIterator('/Users/brandonpurvis/Desktop/osf.io/')
    for path in walker:
        print(path)

