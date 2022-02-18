# Tagging Methodology

## Definition of a Tag

A "tag" is a git concept.  In brief, a tag is a snap-shot, encapsulation, or time-point in the history of the software's version control.  Whereas branches are things that can change in time by accumulating commits; tags are immovable and frozen in time. For a deeper explanation, see here: https://git-scm.com/book/en/v2/Git-Basics-Tagging

## When We Tag

In FATES we create a tag following every merge of new content into the master branch. In other words, every time we integrate a pull-request, we issue a new tag.  Here is where you can find our history of tags:

https://github.com/NGEET/fates/tags

## How We Name Tags

The tag name is designed to convey the order of which the new content occurred in the progression of the code's history as well as the type of content that was added.   There are two broad components to our tag naming convention.  The first part is the "sci" part of the tag, and the second is the "api" part of the tag.  Both of these parts roughly follow the Semantic versioning system (aka SemVer), where a major, minor and bug-fix version number is associated.  If the new content in the tag only modifies how FATES operates internally, without 1) influencing how it communicates with a host model (ELM/CLM) and without 2) modifying how the user controls FATES use (ie changes to the namelist, or structure of the parameter file), then we increment one of the "sci" version numbers.  Alternatively, if the new content does fall under the previous two classifications, then we increment one of the "api" version numbers.

More on SemVer can be found here: https://semver.org/spec/v2.0.0.html  

In brief, here is how we update the version numbers:

sci major: If there is some fundamental change to the nature of FATES which we deem suitably noteworth (this may never happen as its a qualitative thing)
sci minor: If content has been added that changes scientific hypotheses, or changes that change answers without being a bug fix
sci bugfix: As the name implies, if a bug has been fixed, or there have been cosmetic-only changes, or accessory changes

api major: If we change the communication with FATES and its host, in such a way that FATES is no-longer backwards compatible with the HLM. When this happens, we must make synchronized API changes to the host land model. For the compatability match history, see here: https://github.com/NGEET/fates/wiki/Table-of-FATES-API-and-HLM-STATUS
api minor: If changes are made to the FATES API that are still  backwards compatible. An example of this would be an update to structure of the FATES parameter file.  The user would not need to update which version of the HLM they use, but they would need to use a new parameter file structure.
api bugfix: Any changes that are to the API, but do not fall into the previous categories would be incremented here. Particularly, bug-fixes that do not require updates on the HLM side of code, or cosmetic changes and updates to documentation or syntax.

## Patch Tags

Patch tags are issued when we identify bug fixes, that must be applied retro-actively to already released tags. This will typically happen when the bug is identified in conjunction with a host-model that has not had its code updated to the most recent FATES API.  For instance, if the latest FATES API is 16, but changes to enabled compatibility with E3SM have not finished review and integration, such that it is only compatible with API 15. If a bug was identified that needs to be applied to API 15 so that tests can pass and the API can be updated, we would release a patch.  Here, the patch will inherit the name of its base, and will also use suffix "_patch<increment>".  Each patch is unique, and can be applied to multiple base tags.  For instance, "_patchA" will only be used once, and will reflect one bug fix potentially applied to multiple tags.

Here is an example: https://github.com/NGEET/fates/releases/tag/sci.1.44.1_api.14.2.0_patchA
