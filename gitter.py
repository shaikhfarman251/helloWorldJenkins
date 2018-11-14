#import git
#git.Git("D:/mongoDB").clone("https://github.com/farmanAbbasi/helloWorldJenkins.git")
import os
from git import Repo
repo_dir = '/mongoDB/helloWorldJenkins'
repo = Repo(repo_dir)
file_list = [
    '/readme.txt'
]
commit_message = 'Add simple regression analysis'
repo.index.add(file_list)
repo.index.commit(commit_message)
origin = repo.remote('origin')
origin.push()
