import os
from git import Git, Repo

repo_dir = "."

repo = Repo(repo_dir)

g = Git(repo)
print(g.status())
print('-' * 60)

print("Untracked files:")
print(repo.untracked_files)
print('-' * 60)

print("Branches:")
for branch in repo.branches:
    print(branch.name, branch.path)
print('-' * 60)

print(f"repo.is_dirty(): {repo.is_dirty()}")
print('-' * 60)

print("repo.remotes:")
for remote in repo.remotes:
    print(remote.name, remote.url)
print('-' * 60)

