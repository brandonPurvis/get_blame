# get_blame

## What
Makes a repository git blame, searchable.

## How To...
### Install
 * get elasticsearch
 * clone this repository
 * pip install -r requirements
 
### Use
  * follow install instructions
  * `invoke index_repo <url_or_repo>` to put that repo's data into elasticsearch.
  * Optional: clone [seeblame](http://github.com/brandonPurvis/see_blame) for a Django frontend.