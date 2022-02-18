# FATES Development workflow

Here is a helpful and straightforward guide to help new users understand the basics of a work-flow:

https://guides.github.com/introduction/flow/

We also use git **submodule**, this was decided for consistency sake with the ACME project (although that may change.


***


## Some key points:

The FATES is a collection of modules with a communication interface, not a stand-alone model itself.  Thus, it must be called by a land-model.  Coupling with E3SM's land-model and CESM's land-model is currently supported.

Because FATES is not a stand-alone module, the development process and process to build the model uses a **submodule** system.  In short, you must clone the land-model repository, which will indirectly handle the cloning of FATES.

The central (i.e. NGEET/) repository contains a master branch, numerous potential **feature** branches, and public release branches.
* **Master** is the continuously tested, stable version of the code that is updated by new features when they become vetted and available.
* **Feature** branches are created by developers who wish to contribute, a feature branch is supposed to encapsulate the changes associated with a targeted development concept.

***
## Fork-and-Pull System:

The NGEET fates project uses a "fork-and-pull" system.  Meaning, developers are expected to keep their feature branches synced with their own personal forks of the fates repository.  The users' forks will be the server-side location from which they can collaborate with team-mates, and allow others push/pull access to their feature branch.

Pull requests to the central ed-clm repository "NGEET/ed-clm", should be issued from one of these forked repositories.

For more on how to fork and what forks are, see: https://help.github.com/articles/fork-a-repo/

***

##  Process:

* A developer creates a new branch in the code based off of "master" that will contain a specific feature or requested bug fix to be added to the code ([naming convention here](https://github.com/NGEET/ed-clm/wiki/Feature-Branch-Naming-Convention)).
```
   git checkout master
   git fetch origin
   git pull origin master
   git checkout -b rgknox-IO-historyfix
```

* The developer modifies code, and periodically commits those changes:
```
   git add ChangedFile1.F90
   git add ChangedFile2.F90
   git commit -m "Two generic changes were applied to two generic files."
```
* The developer periodically tests their changes ([protocol here](https://github.com/NGEET/ed-clm/wiki/Testing-Protocols)) as they make commits.
* The developer periodically pushes their committed changes to their fork. This is also useful for sharing work with team-members, and allows the developer a place to save work that can be retrieved on another computer (PUSHING, PULLING AND WORKING WITH FORKS)
* The developer may then decide that their features are complete, or they simply decide that it is time to submit what they have been doing to the NGEET/ team for feedback, help and/or ultimately to get merged into the master version of the code. ([protocol here](https://github.com/NGEET/ed-clm/wiki/Commit-and-Pull-Request-Protocols))
* The developer issues a pull request to merge their feature branch into the “master” (ISSUING PULL REQUESTS )

## Expanded Descriptions