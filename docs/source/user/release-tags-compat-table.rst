FATES-HLM API compatibility tables
=============================================

The following table list the FATES API and the corresponding HLM tag associated with that API update.  Note that CTSM provides a specific tag for each of its merge commits to the master branch whereas E3SM does not.  As such, the hash for the relevant merge commit is provided for E3SM.  Entries that specifically link to a pull request (e.g. PR#XXXX) are provided to note updates which have not been integrated yet, but are pending.  The table may also include future planned API updates without links to provide users an advanced look at what updates are forthcoming.

API 37
------

API 37 captures the spitfire fuel equations refactor changes which renames and moves related variables into a new module.

+--------------------------+----------------+------------+-------------+----------------------------------------------------------------+
| FATES Tag                | CTSM Tag       | E3SM Hash  | Update Type | Short description                                              |
+==========================+================+============+=============+================================================================+
| `sci.1.80.1_api.37.0.0`_ |                |            | Bug fix     | Grass-specific cross-sectional area calculation fix            |
+--------------------------+                +            +-------------+----------------------------------------------------------------+
| `sci.1.80.0_api.37.0.0`_ |                |            | Science     | Growth respiration moved to daily timestep                     |
+--------------------------+                +            +-------------+----------------------------------------------------------------+
| `sci.1.79.3_api.37.0.0`_ | `ctsm5.3.012`_ | `PR 6762`_ | Software    | Refactor SPITFIRE fuel equations                               |
+--------------------------+----------------+------------+-------------+----------------------------------------------------------------+

API 36
------

API 36 captures updates and additions to the interface code for passing a new land use x pft mapping static dataset from the HLM I/O into FATES for land use run mode

+--------------------------+----------------+------------+-------------+----------------------------------------------------------------+
| FATES Tag                | CTSM Tag       | E3SM Hash  | Update Type | Short description                                              |
+==========================+================+============+=============+================================================================+
| `sci.1.79.2_api.36.1.0`_ |                |            | Bug fix     | Correction to inventory write statement                        |
+--------------------------+                +            +-------------+----------------------------------------------------------------+
| `sci.1.79.1_api.36.1.0`_ |                |            | Software    | Updates to the patch insertion method                          |
+--------------------------+                +            +-------------+----------------------------------------------------------------+
| `sci.1.79.0_api.36.1.0`_ |                |            | Science     | Time integrated flux diagnostics                               |
+--------------------------+                +            +-------------+----------------------------------------------------------------+
| `sci.1.78.3_api.36.1.0`_ | `ctsm5.3.003`_ | `ef0abe7`_ | Science     | Default parameter file update (arctic shrubs, grass allometry) |
+--------------------------+----------------+------------+-------------+----------------------------------------------------------------+
| `sci.1.78.2_api.36.0.0`_ |                |            | Software    | Fire-weather refactor (not-bfb)                                |
+--------------------------+                +            +-------------+----------------------------------------------------------------+
| `sci.1.78.1_api.36.0.0`_ |                |            | Software    | Patch-level memory structure refactor                          |
+--------------------------+                +            +-------------+----------------------------------------------------------------+
| `sci.1.78.0_api.36.0.0`_ |                |            | Science     | New sapwood, agb, and leaf allometries for grasses             |
+--------------------------+                +            +-------------+----------------------------------------------------------------+
| `sci.1.77.2_api.36.0.0`_ |                |            | Bug fix     | Land use transition matrix initialization                      |
+--------------------------+                +            +-------------+----------------------------------------------------------------+
| `sci.1.77.1_api.36.0.0`_ |                |            | Bug fix     | Non-land use run modes fix                                     |
+--------------------------+                +            +-------------+----------------------------------------------------------------+
| `sci.1.77.0_api.36.0.0`_ | `ctsm5.2.013`_ | `377b2d3`_ | Science     | Land use version 2 [#]_                                        |
+--------------------------+----------------+------------+-------------+----------------------------------------------------------------+

Pre-API 36 table
----------------

For a compatibility table prior to API 35, please see `this older API compatibility table`_.

..
   For a compatibility table prior to API 35, please see :doc:`/user/HLM-FATES-PFT-map`.


.. [#] Users wanting to run non-land use run modes should avoid this tag due `issue #1221`_.  The next fates tag addresses this issue.

.. _sci.1.80.1_api.37.0.0: https://github.com/NGEET/fates/releases/tag/sci.1.80.1_api.37.0.0
.. _sci.1.80.0_api.37.0.0: https://github.com/NGEET/fates/releases/tag/sci.1.80.0_api.37.0.0
.. _sci.1.79.3_api.37.0.0: https://github.com/NGEET/fates/releases/tag/sci.1.79.3_api.37.0.0

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

.. _ctsm5.3.012: https://github.com/ESCOMP/CTSM/releases/tag/ctsm5.3.012
.. _ctsm5.3.003: https://github.com/ESCOMP/CTSM/releases/tag/ctsm5.3.003
.. _ctsm5.2.013: https://github.com/ESCOMP/CTSM/releases/tag/ctsm5.2.013
.. _ctsm5.2.002: https://github.com/ESCOMP/CTSM/releases/tag/ctsm5.2.002

.. _ef0abe7: https://github.com/E3SM-Project/E3SM/commit/ef0abe727bb4f3286a40d2350aaded5030197615
.. _377b2d3: https://github.com/E3SM-Project/E3SM/commit/377b2d31d77977efc0f5edf79ba243377f668517
.. _f14a3cf: https://github.com/E3SM-Project/E3SM/commit/f14a3cf738fc56f287665a49231b461878770958

.. _PR 6762: https://github.com/E3SM-Project/E3SM/pull/6762

.. _issue #1221: https://github.com/NGEET/fates/issues/1221

.. _this older API compatibility table: :doc:`/user/Table-of-FATES-API-and-HLM-STATUS`
