Release, tag and HLM API compatibility tables
=============================================

The following table list the FATES API and the corresponding HLM tag associated with that API update.  Note that CTSM provides a specific tag for each of its merge commits to the master branch whereas E3SM does not.  As such, the hash for the relevant merge commit is provided for E3SM.  Entries that specifically link to a pull request (e.g. PR#XXXX) are provided to note updates which have not been integrated yet, but are pending.  The table may also include future planned API updates without links to provide users an advanced look at what updates are forthcoming.

API 36
------

+--------------------------+----------------+------------+----------------------------------------------------------------+
| FATES Tag                | CTSM Tag       | E3SM Hash  | Description                                                    |
+==========================+================+============+================================================================+
| `sci.1.79.2_api.36.1.0`_ |                |            | Correction to inventory write statement                        |
+--------------------------+                +            +----------------------------------------------------------------+
| `sci.1.79.1_api.36.1.0`_ |                |            | Updates to the patch insertion method                          |
+--------------------------+                +            +----------------------------------------------------------------+
| `sci.1.79.0_api.36.1.0`_ |                |            | Time integrated flux diagnostics                               |
+--------------------------+                +            +----------------------------------------------------------------+
| `sci.1.78.3_api.36.1.0`_ | `ctsm5.3.003`_ | `ef0abe7`_ | Default parameter file update (arctic shrubs, grass allometry) |
+--------------------------+----------------+------------+----------------------------------------------------------------+
| `sci.1.78.2_api.36.0.0`_ |                |            | Fire-weather refactor (not-bfb)                                |
+--------------------------+                +            +----------------------------------------------------------------+
| `sci.1.78.1_api.36.0.0`_ |                |            | Patch-level memory structure refactor                          |
+--------------------------+                +            +----------------------------------------------------------------+
| `sci.1.78.0_api.36.0.0`_ |                |            | New sapwood, agb, and leaf allometries for grasses             |
+--------------------------+                +            +----------------------------------------------------------------+
| `sci.1.77.2_api.36.0.0`_ |                |            | Bug fix for initializing land use transition matrix init       |
+--------------------------+                +            +----------------------------------------------------------------+
| `sci.1.77.1_api.36.0.0`_ |                |            | Bug fix for non-land use run modes                             |
+--------------------------+                +            +----------------------------------------------------------------+
| `sci.1.77.0_api.36.0.0`_ | `ctsm5.2.013`_ | `377b2d3`_ | Land use version 2                                             |
+--------------------------+----------------+------------+----------------------------------------------------------------+

.. _sci.1.79.2_api.36.1.0: https://github.com/NGEET/fates/releases/tag/sci.1.79.2_api.36.1.0
.. _sci.1.79.1_api.36.1.0: https://github.com/NGEET/fates/releases/tag/sci.1.79.1_api.36.1.0
.. _sci.1.79.0_api.36.1.0: https://github.com/NGEET/fates/releases/tag/sci.1.79.0_api.36.1.0
.. _sci.1.78.3_api.36.1.0: https://github.com/NGEET/fates/releases/tag/sci.1.78.3_api.36.1.0

.. _sci.1.78.2_api.36.0.0: https://github.com/NGEET/fates/releases/tag/sci.1.78.2_api.36.0.0
.. _sci.1.78.1_api.36.0.0: https://github.com/NGEET/fates/releases/tag/sci.1.78.1_api.36.0.0
.. _sci.1.78.0_api.36.0.0: https://github.com/NGEET/fates/releases/tag/sci.1.78.0_api.36.0.0
.. _sci.1.77.2_api.36.0.0: https://github.com/NGEET/fates/releases/tag/sci.1.77.2_api.36.0.0
.. _sci.1.77.1_api.36.0.0: https://github.com/NGEET/fates/releases/tag/sci.1.77.1_api.36.0.0
.. _sci.1.77.0_api.36.0.0: https://github.com/NGEET/fates/releases/tag/sci.1.77.0_api.36.0.0

.. _ctsm5.3.003: https://github.com/ESCOMP/CTSM/releases/tag/ctsm5.3.003
.. _ctsm5.2.013: https://github.com/ESCOMP/CTSM/releases/tag/ctsm5.2.013

.. _ef0abe7: https://github.com/E3SM-Project/E3SM/commit/ef0abe727bb4f3286a40d2350aaded5030197615
.. _377b2d3: https://github.com/E3SM-Project/E3SM/commit/377b2d31d77977efc0f5edf79ba243377f668517
