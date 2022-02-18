# Commit and Pull Request Protocol

Version control is the living history of the project. It not only provides backups and a way to share changes, but is a critical component of scientific reproducibility of results by the wider community and helps future developers understand the code. Good commit messages are a essential to ensure the history of the project is useful. Messages should follow the template below, with an emphasis on the **why** of a set of changes, not just the **what**. It only take as few seconds to minutes to fill out the template, and can save future developers, including future you, hours to days in understanding the code.

We follow the commit protocol imposed by the CIME development team.  See: 

[https://github.com/CESM-Development/cime/wiki/CIME-Git-Workflow](https://github.com/CESM-Development/cime/wiki/CIME-Git-Workflow)


## Commits

### Commit Template

With a couple of simple configuration settings, explained below, you can automatically open and editor with the template pre-inserted into the message by typing `git commit`. Commits **MUST** use the following template (that we stole from CIME):

    [ 50 character, one line summary ]
    
    [ Description of the changes in this commit. It should be enough
      information for someone not following this development to understand. 
      Lines should be wrapped at about 72 characters. ]
    
    Fixes: [NGT-ED Github issue #]
    
    User interface changes?: [Yes (describe what changes), No]

    Code review: [Names]
    
    Test suite: [suite name, machine, compilers]
    Test baseline:
    Test namelist changes:
    Test answer changes: [bit for bit, roundoff, climate changing]
    Test summary:


Please always include a testing block in your commit messages, especially if you didn't do any testing. Simply put `Testing: none, not expected to compile` or `Testing: none, compiles but not tested`, or `Testing: manually with test/compset/grid/user_nl/changes`.

### Configure Automatic Use of the Template

You can configure git to use this template automatically.  First, save the above text to a template on the machine where you commit: `~/cime-commit-template.txt`

Option 1: Issue the following onetime setup for all repos you use on this machine.  

* `git config --global commit.template $HOME/cime-commit-template.txt`


Option 2: If you want to use this template with only one project (ie NGT-ED)

* `cd /path/to/sandbox`

* `git config commit.template $HOME/cime-commit-template.txt`



### Configure a Default Editor

`git config --global core.editor [editor of your choice: emacs, vi, vim, etc]`

## Pull requests

Pull requests should be for a single atomic set of changes. Mixing multiple unrelated changes together makes it hard to review code, and hard to debug when something unexpected happens. The more code that is changed at once and the more unrelated things that are changed, the more likely we are to make mistakes and introduce bugs.

### Code cleanup
Prior to submitting a pull request, please review your changes and ensure:

1. All debug output should be removed or placed into a logical block that limits when it is written, e.g. `if (fates_global_verbose())` or `if (DEBUG)`, and disabled by default. Do *not* simply comment out debug statements.

1. All debug output must be directed to the fates log file, i.e. `write(fates_log(), *)`. Pull requests that use standard out or the host log, e.g. `write(*, *) or write(iulog, *)` will not be accepted.

1. The Fortran standard specifies a maximum line length of 132 characters. Most compilers, i.e. intel, gnu, pgi, allow this requirement to be ignored. The NAG compiler enforces this and it can not be turned off. Since we are required to support NAG, we must continue lines that extend past 132 characters. It's also just bad practice to have such long lines because they are hard to read. Both vim and emacs can be configured to show column numbers.

### Test your changes

1. If your changes are runtime configurable, you should add a new test that exercises the non-default state. See [adding tests](https://github.com/NGEET/ed-clm/wiki/Testing-Protocols).

1. Follow the [testing protocols](https://github.com/NGEET/ed-clm/wiki/Testing-Protocols) for scientists.

1. It is expected that all test functionality will always pass. This includes bit for bit restart and threading. Baseline tests for ed/fates may or may not be bit for bit depending on the nature of your changes. Include a list of *failing* test results in the pull request, along with an explanation of why they are failing. Do **not** include passing results.

### Submitting a pull request

1. Push your branch from your development machine to your github fork. This should be a location like `github.com/user-name/ed-clm`. You can see the remote forks your development clone knows about on the command line:
    ```
    $ git remote -v
    me  git@github.com:my-user-name/ed-clm.git (fetch)
    me  git@github.com:my-user-name/ed-clm.git (push)
    origin	git@github.com:NGEET/ed-clm.git (fetch)
    origin	git@github.com:NGEET/ed-clm.git (push)
    $ git push me my-dev-branch
    Counting objects: 7, done.
    Delta compression using up to 32 threads.
    Compressing objects: 100% (7/7), done.
    Writing objects: 100% (7/7), 833 bytes | 0 bytes/s, done.
    Total 7 (delta 5), reused 0 (delta 0)
    remote: Resolving deltas: 100% (5/5), completed with 5 local objects.
    To git@github.com:my-user-name/ed-clm.git
     + 18fa785...f835a81 my-dev-braanch -> my-dev-branch
    ```
     
1. Open your github fork in a web browser: `https://github.com/my-user-name/ed-clm.git`

1. You should see a big green button labeled 'Compare & Pull Request'. Click it. If you don't see it, then look for a button 'New pull request'.

1. At the top of the new page, you should see a beige area showing the base, NGEET/ed-clm master, and your fork and branch. It should say 'Able to merge'. If not, please contact one of the software engineers to discuss if they want you to merge it.

1. Next is a text box where you can edit the title of your pull request and the description. The description contains a template of the required information. Fill out the required information. Set the title the same as the 50 character summary.

1. Click 'Create pull request'.

