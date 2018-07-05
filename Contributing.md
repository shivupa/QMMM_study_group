# Using git

For now we will keep things as simple as possible.

## 0. Fork this repository on Github
This creates a copy for you on your Github page (Click the button that says fork this repository). The changes you make to this version will not be a part of everyone's code yet.

## 1. Clone your forked repository
This creates a local copy on your computer(s) that you can edit. 

## 2. Make some changes to the files.

## 3. Add the changes to your forked version of the code.
To see what files have changed use the command `git status`.
Add the files that you have changed using `git add filename`.
Explain what changes you have made using an informative commit message with `git commit -m "My message.."`.
Push the changes to your forked version using `git push`.

## 4. Add your changes to the main repository.
Go to the (main repository)[https://github.com/shivupa/QMMM_study_group] and open a pull request from *your* master branch to *my* master branch.

## Notes:
At some point you may want to update to the latest changes on the main repository.
To do this add the main repository as an upstream source `git remote add upstream https://github.com/shivupa/QMMM_study_group`
Check that you have added the repository as upstream `git remove -v`

Now to get changes and add them to your branch, run `git pull --rebase upstream master`

