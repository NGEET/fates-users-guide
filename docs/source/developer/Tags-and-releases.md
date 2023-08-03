# Tag and Releases

This page presents the workflow for tagging recently integrated pull request.  Only FATES repository administrators are permitted to integrate pull requests and create tags/releases.

## Versioning format

Tagging is a somewhat subjective and a conceptual exercise.  The tag format is as follows:

`sci.x.y.z_api.a.b.c`

The first three version numbers after `sci` are related to the scientific code updates:
- `x`: Major stable scientific release
- `y`: Scientific feature update
- `z`: Bug fix update

The major stable release number increments rarely and are based upon large long-term devlopment milestones.  The vast majority of updates to the FATES code are individual feature updates.  This includes, but is not limited to, new scientific features, submodule refactors, performance improvements, etc.  As such, the number of lines of code may vary widely for such updates and are not necessarily answer-changing.  Bug fixes are given their own version number.

The three version numbers after `api` are related to code changes on the host land model (e.g. [CTSM](https://github.com/ESCOMP/ctsm)) side that are necessary for the use of the FATES code:  
- `a`: major API update
- `b`: minor API update
- `c`: API bug fix

The difference between major and minor version updates is based more closely related to the scope of the host land model code that is changed concurrently with the associated FATES feature update.  An update that adds only a few lines of code to pass new information to the FATES model or refactors the existing host land model code without changing functionality would be considered a minor update.  Minor updates are not necessarily backwards incompatible changes, whereas major api updates are always backwards incompatible changes.  API bug fixes are given their own version number.

Note that updates to comments, documentation or code not directly associated with FATES, but held in the repo are not associated with specific tags as they do not fall under any of the above versioning categories.  The current exception to this is with [tools](https://github.com/NGEET/fates/tree/master/tools) for which we append a `tools` suffix like so: `sci.x.y.z_api.a.b.c_tools.i.j.k`.  We only append this to a new tag if a tool update is included.  Note that the if the tool update does not accompany a scienctific or api update, the previous tag for those updates is used.  The first three version numbers after `tools` denote the following updates:
- `i`: new tool or major stable release
- `j`: update to existing tool
- `k`: bug fix to existing tool

### Tagging procedure

1. After merging a PR, pull in latest changes and tags to your local fates master branch.  

    - `git checkout <ngeet/fates master branch>`
    - `git pull <ngeet/fates remote repo name> `

2. Verify that you have the latest tag available by comparing github release/tags page by comparing against the output from:

    - `git tag`

3. Create a new *annotated* tag for the currently checkout ngeet/fates master branch.  Annotated tags have been recommended by CSEG as they are full-featured objects in git and [have many features](https://git-scm.com/book/en/v2/Git-Basics-Tagging/#creating-tags).  Make sure to include a descriptive message:

    - `git tag -a <sci.x.xx.x_api.x.x.x> -m "*put message here*"`

4. Push the tag to ngeet/fates remote:

    - `git push <ngeet/fates remote repo name> <sci.x.xx.x_api.x.x.x>`

5. Go to the [release/tags page](https://github.com/NGEET/fates/tags) on the ngeet/repo and check that the tag is there.

## Releases

The FATES dev team does not have a formal 'release' or 'pre-release' schedule and as such, the majority of tags are not associated with either.  Releases are used primarily to generate a new [Zenodo DOI tag](https://zenodo.org/record/3825474) as necessary.

### Release procedure

1. Create a release based on the tag (as necessary).  Click the ellipses on the far right and select 'create release'.

2. It's ok to just copy/paste the tag message and use that as the release message.  If this is a major changes that should be considered the latest 'stable', leave the 'pre-release' unchecked.  Check the 'pre-release' box if the change is an upgrade that has not been extensively used by users yet.

