Overview
========

Discussion about the material
Understanding oriented section


.. toctree::
   :maxdepth: 1
   
   faq
   notable
   Canopy-Layering-Convention
   Communal-slides-related-to-FATES
   Current-Unsupported-or-Broken-Features
   Fixed-Biogeography-Mode
   Model-Initialization-Modes
   Namelist-Options-and-Run-Time-Modes
   Notes-on-the-Parameter-File
   PARTEH-Modes
   Reference-List
   Relevant-References
   SP-(satellite-phenology)-mode
   SPITFIRE-Namelist-Options
   Useful-Stuff

Chosing a FATES version
-----------------------

FATES is a research model that is currently undergoing rapid development and improvement (at the time of writing this, May 2019).  As such, some users may want to choose a version of the model that has the most recent features, and some users may want to choose the version that is the most stable. 

Important Note: **The FATES integration team only merges changes into the master branch that have undergone the full testing protocol**.  

This testing protocol always uses the standard "FATES" test suite in the CIME framework.  For any pull requests that is non trivial, we will also perform tests that are potentially multi-decadal, global and compare against previous answers.  We may also perform long-term simulations at specific sites and do a more comprehensive evaluation. 

However, some changes may be integrated that are so complex that testing may not catch all problems before they can be patched.  Therefore:

1) For users who want the most feature rich version of the code that works with ELM and CTSM, simply checkout the master branch of NGEET/fates.*

2) For users who want the most stable version of the code.  Checkout that most recently released
"tag" that is **NOT a "pre-release"**.  This should be labelled as "Latest Release".  See: https://github.com/NGEET/fates/releases

Note on option 1.  The master branch will typically match the most recent tag released. If the most recent tag is a bug fix (particularly a simple one), and the most recent tag is heavily tested and has shown low instability through repeated use; it is very possible that the master branch may match a fully release tag (not pre-release).
