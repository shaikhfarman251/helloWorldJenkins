import requests
import os
from git import Repo
COMMITS_TO_PRINT = 1


def print_commit(commit):
    print('----')
    print(str(commit.hexsha))
    t=repo.head.commit.tree
    changed_file=str(repo.git.diff(t,name_only=True))
    print(type(changed_file))
    url = "https://raw.githubusercontent.com/farmanAbbasi/helloWorldJenkins/master"+"/"+changed_file
    r = requests.get(url)
    if r.status_code==200:
        filename = 'C:/Users/moabbasi/Desktop/gitFiles/Test1.txt'
        content=r.content.decode('ascii')
        f = open(filename,'w')
        f.write(content)
        print("Content written at Test1.txt...")
    else:
        print("Response failed")
    
   											

def print_repository(repo):
    print('Repo description: {}'.format(repo.description))
    print('Repo active branch is {}'.format(repo.active_branch))
    for remote in repo.remotes:
        print('Remote named "{}" with URL "{}"'.format(remote, remote.url))
    print('Last commit for repo is {}.'.format(str(repo.head.commit.hexsha)))


if __name__ == "__main__":
    repo_path = os.getenv('https://github.com/farmanAbbasi/helloWorldJenkins')
    #repo = git.Repo(os.path.dirname())
    repo = Repo(repo_path,search_parent_directories=True)
    if not repo.bare:
        print('Repo at {} successfully loaded.'.format(repo_path))
        print_repository(repo)
        commits = list(repo.iter_commits('master'))[:COMMITS_TO_PRINT]
        for commit in commits:
            print_commit(commit)
            pass
    else:
        print('Could not load repository at {} :('.format(repo_path))
