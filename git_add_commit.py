from git import Git, Repo
import os

repo_folder = '/Users/administrator/MyProject'

repo = Repo(repo_folder)

os.chdir(repo_folder)

g = Git(repo)

file_name = 'dict_comps.py'
g.add(file_name)
g.commit(file_name, message="first commit")
print(g.log())

# create new branch
g.checkout('-b', 'dev001')

# work on existing branch
g.checkout('dev003')