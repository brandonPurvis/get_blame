import main
from invoke import task


@task
def index_repo(url, merged=False):
    main.run(url, merged)
