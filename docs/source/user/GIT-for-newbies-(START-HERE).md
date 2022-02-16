# Git for newbies

Rosie Fisher. 24 Feb 2016. 

(EDIT RGK 10-2017) The following walk-through was written before we made FATES a submodule.  Many of the steps explained here are useful, but does not cover that there is a host repository (fates-clm) and a submodule repository (fates))

This document explains the process for basic use of GIT for modification of the NGEE-T model code, starting from checking out the code, through creating a branch, modifying it, and committing changes.  It should hopefully assume no prior github knowledge. 

1. **Log in to github.com** (in browser, not terminal).  I am already added to the NGEET repository, but if you aren't then that needs to happen first. Email rgknox@lbl.gov to ask permission. 

2. Go to https://github.com/NGEET/fates-clm. This is the **REFERENCE REPOSITORY.** 

3. **Fork the repository** using the 'fork' button in the top right. This will create your own mirror/sandbox of the reference repository, for you to do with what you please. 

4. **Go to a terminal.** Ideally one on which you are already set up to run CESM/ACME, such that the code will work and all of the needed libraries will be there.  

5. **Confirm you have an SSH key.** In your user profile on GitHub open settings. In Settings open 'SSH and GPG keys'. If you do not have an SSH key, follow the links to generate and add an SSH key in your terminal where you will run the code. (This should be the same as the location for step 4. My key was on Yellowstone.) Then add the SSH key to your GitHub account using the instructions in the link at the bottom of the page "Adding a new SSH key to your GitHub account" Ask for help if you get stuck.

6. **Clone the repository** onto your server. The command I used was : `git clone git@github.com:rosiealice/fates-clm.git fates-clm`

7. Now you have a version of the code on your machine. It should look like CESM/ACME and have 'cime' and 'components' directories, among other things. 

8. **Make yourself a branch** on which to change things you might care about. For example. `git checkout -b rosie/newbranchname` would make that happen. 'rosie' is a coding convention so that we know whose branch it is (obv. you should add your own name there). Look at your new branch, and all the others, with `git status`
Use `git branch -v -a` to look at the list of all available branches.  
Here is a note on branch naming https://github.com/NGEET/fates/wiki/Feature-Branch-Naming-Convention
and here is a description of the NGEE branch development protocol 
https://github.com/NGEET/fates/wiki/NGT-ED-Development-Workflow

9. **Edit code** Change stuff in the branch.  Start with something small and easy as a proof of concept. Ideally test it. Use the NGEE style guide to avoid making embarrassing mistakes:
https://github.com/NGEET/fates/wiki/Coding-Practices-and-Style-Guide 
Here is a presentation, on the 2016 CLM tutorial site, which includes basic workflow instructions on how to test your changes by creating cases using CIME (the scripting infrastructure used in CESM & ACME). 
http://www.cesm.ucar.edu/events/tutorials/20160912-clm/2016CLMTutorial_day1-practical-lombardozzi.pdf

10. **Look at what you did**. Use `git diff`

11. **'Stage' your changes**. This has no analogue in svn. These are changes you will commit to the branch, the need to be put in this staging area one file at a time, before that can happen. Like a big 'are you sure?' button.  This works using `git add components/clm/src/dir/file.F90` where dir/file are the directory and filename you modified.  

12. **Look at what you did**. Use `git diff --staged` to see code mods or `git status` to see the files you changed and staged. 

13. **Commit changes to local branch**. Use `git commit` to make a new revision to your local branch. 'git commit -m "text of message" will automatically add the description of the commit. This should only be use for small (a few lines of changes) commits. See here for a more comprehensive description of proper message protocol. https://github.com/NGEET/fates/wiki/Commit-and-Pull-Request-Protocols
n.b. staging and committing can be combined with 'git commit -a -m "message"' where -a is 'add'. 

14.  **Look at what you did**. Use `git log` to show what you did. `git log -1` (or 2,3) shows the last 1,2,3, commits. 

15. **Push your local branch into your github repository**.  Use `git push origin rosie/newbranchname` where 'origin' directs it to _your_ repository, not the main one, and of course, rosie/newbranchname should be changed to the appropriate path. 

15. **Check for updates from the reference repository**. First, add a remote link to the reference repository `git remote add NGEET_main git@github.com:NGEET/fates.git` 

16. **Update code to the new master** First, change to your local 'master' branch: `git checkout master`  

17. **Checkout the code from the ref. repo.** into your local master `git pull NGEET_main master` 

18. **Move back to your branch**, e.g.  `git checkout rosie/newbranchname`

19. **Merge the local master code into your local branch**. `git merge master`

20. **Test code** One you've done this for a while and are confident with it, then you'll want to test your code to make sure you didn't break it, following these instructions. https://github.com/NGEET/fates/wiki/Testing-Protocols

21. **Submit pull request** Then you'll want to try and submit a pull request to get your changes back into the reference repository. https://github.com/NGEET/fates/wiki/Commit-and-Pull-Request-Protocols

## Some other commands that are handy:

* add another remote repository to your cloned repository (e.g. for pulling from a branch on someone else's repository); here using rgknox as the remote repository:
  * if using https: `git remote add rgknox_repo https://github.com/rgknox/fates.git`
  * or if using ssh:  `git remote add rgknox_repo git@github.com:rgknox/fates.git`

* fetch the contents of that remote repository into your local repository:
  * `git fetch rgknox_repo`

* see what remote repos you have locally
  * `git remote -v`

* to see what changes have happened in your branches. 
  * git log --oneline origin/master..master

* check out a specific branch from a specific external repo into a new local repo
  * `git checkout -b rgknox-bcs rgknox_repo/rgknox-bcs` where _rgknox-bcs_ is the branch on the _rgknox_repo_ repository

* lets say you have a modified branch on your repository and want to merge it up to the head of the master:
  * lets assume _origin_ is your repository, _ngeet_repo_ is the NGEE repository, and the branch that you want to make up to date with master is called _test_branch_
  * first check to make sure I am where I think I am: `git branch`
  * go to the local master branch: `git checkout master`
  * pull up most recent version from origin onto local machine: `git fetch origin` and `git fetch ngeet_repo`
  * if you need to make a local copy of a branch: `git checkout -b test_branch origin/test_branch`; otherwise if you have this already: `git checkout test_branch` and then `git pull origin`
  * check to make sure you are where you think you are: `git log`
  * go back to master and bring the local version of master up to date with whats on the ngeet_repo: `git checkout master` and then `git pull ngeet_repo`
  * check to make sure you are where you think you are: `git log`
  * switch branches to the one you are interested in: `git checkout test_branch`
  * bring the new changes from master onto that branch: `git merge master`
  * check to make sure you are where you think you are: `git log` and `git branch`
  * to push the changes back to that branch on the origin: `git push origin test_branch`

* pull a specific commit into a new local branch:
  * `git checkout -b tag_abcd123 abcd123`

* a thing that's useful is to tag the git hash as part of a casename when running a simulation to keep track of what code you used.  you can do this, e.g., in a bash script, by outputting the git log command and feeding it into a variable: `git log -n 1 --format=%h`