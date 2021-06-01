# LCP_B-CMS_FCNC

A brief summary of the typical actions to be performed for an effective collaboration.

***

The virtual machine already has a `.gitignore` file with all the not interesting files and directories. This allows everyone to simply use `git add . ` command
to udpate the files for commit. Be aware that changes in the directory composition not reflected in the `.gitignore` file would cause these (eventually) not
interesting files to be committed. To be sure the command `git status` can be run: the files in the output should be only the interesting ones; if not so
use `git add <filename>` instead of `git add . `. The most updated version is always the one on this repo, so to work effectively on the VM one should always fetch
for updates, merge, work, add the changed files, commit and push again to this repo. Moreover, in order to have a proper merge one should always commit the local
changes before. Also, before pushing one should always commit, merge with the remote one wants to push to, and then push. In the previous example of development
cycle it could happen that before pushing one could need to fetch and merge again (this happen if someone update this repo in during the work-time on the VM).

### Working on the VM

* `git fetch upstream`
* `git merge upstream/master`
* work on the project
* `git add . `
* `git commit -m "commit label"
* `git push upsteam/master`
* if push doesn't work then additional steps are needed:
  - `git fetch upstream`
  - `git merge upstream/master`
  - `git push upsteam/master`






