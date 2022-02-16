# Authentication the NCAR SVN repository

New users will eventually run into a road-block when first running the fates-clm code on a new machine.  When the build sequence first tries to download data from NCAR's SVN repository it will have trouble authenticating.

Very often the user has to manually try to list the contents of the repository's directory, which will trigger a manual authentication:

svn ls https://svn-ccsm-inputdata.cgd.ucar.edu --

Once this manual authentication has been done once, the authentication will be saved, and the build process will be able to automatically download data.