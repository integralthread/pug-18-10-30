import errno
import os
from pathlib import Path
from sh import git as git_cmd
from sh import keybase 

edwin = "mcguffinn"
send   = keybase.bake('chat', 'send', '--exploding-lifetime', '30s')
git = git_cmd.bake(__tty_out=False)

class status:
    def __init__(self, path):
        self.path = path
    
    def __enter__(self):
        self.cwd = Path.cwd()
        os.chdir(self.path)
        return self 

    def __exit__(self, *args):
        os.chdir(self.cwd)

def repos():
    home = Path("~/dev/integralthread/").expanduser()

    for repo in [p.parent for p in home.glob("**/.git")]:
        with status(repo):
            print("{}\n REPO {}".format("*" * 20, repo))
            result = git.status('--short')
            print(result)

def main():
    repos()

if __name__ == '__main__':
    main()