#NOTICE COMMENTS BEFORE TESTING

from git import Repo
import os

#function for uploading to Github
def git_push():
    try:
        repo = Repo('/home/pi/test/FlatSatChallenge')
        repo.git.add('/home/pi/test/FlatSatChallenge')
        repo.index.commit('New Git Test')
        print('made the commit')
        origin = repo.remote('origin')
        print('added remote')
        origin.push()
        print('pushed changes\n')
    except:
        print('couldn\'t upload to git\n')

#ADD YOUR NAME HERE
name = "STEVENWU"

#REPLACE 'yourfolder' with the name of your directory, then Run it!
f = open(r'/home/pi/test/FlatSatChallenge/%s.txt' % name,'w')
f.write('%s' % name)
f.close()

git_push()



