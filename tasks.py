import main
from invoke import task


@task
def index_repo(url):
    main.run(url)
