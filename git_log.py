from git import Git, Repo

repo = Repo('.')
g = Git(repo)

print(g.log('dict_comps.py'))
print('-' * 60)

print(g.log('SETUP'))