FATES-HLM API compatibility tables
=============================================

The following table list the FATES API and the corresponding HLM tag associated with that API update.  Note that CTSM provides a specific tag for each of its merge commits to the master branch whereas E3SM does not.  As such, the hash for the relevant merge commit is provided for E3SM.  Entries that specifically link to a pull request (e.g. PR#XXXX) are provided to note updates which have not been integrated yet, but are pending.  The table may also include future planned API updates without links to provide users an advanced look at what updates are forthcoming.

API 39
------

This API update corrects issues with restarting FATES two-stream radiation and changes how zenith angles are updated and passed to FATES.

+---------------------------+----------------+------------+-------------+----------------------------------------------------------------+
| FATES Tag                 | CTSM Tag       | E3SM Hash  | Update Type | Short description                                              |
+===========================+================+============+=============+================================================================+
| `sci.1.83.0_api.39.0.0`_  |                |            | Science     | Two-stream sun-shade fraction update                           |
+---------------------------+                +            +-------------+----------------------------------------------------------------+
| `sci.1.82.8_api.39.0.0`_  |                |            | Software    | Refactor of vegetation bin indexing                            |
+---------------------------+                +            +-------------+----------------------------------------------------------------+
| `sci.1.82.7_api.39.0.0`_  |                |            | Bug fix     | Radation transmission bug fix                                  |
+---------------------------+                +            +-------------+----------------------------------------------------------------+
| `sci.1.82.6_api.39.0.0`_  |                |            | Bug fix     | Excess respiration unit fix for mass balance issue             |
+---------------------------+                +            +-------------+----------------------------------------------------------------+
| `sci.1.82.5_api.39.0.0`_  |                |            | Science     | Add site x pft expansions of seed bank history output          |
+---------------------------+                +            +-------------+----------------------------------------------------------------+
| `sci.1.82.4_api.39.0.0`_  |                |            | Bug fix     | Correct missing fire-induced carbon mortality history output   |
+---------------------------+                +            +-------------+----------------------------------------------------------------+
| `sci.1.82.3_api.39.0.0`_  | `ctsm5.3.034`_ | `64046ec`_ | Bug fix     | Fixes two-stream radiation exact restart issue                 |
+---------------------------+----------------+------------+-------------+----------------------------------------------------------------+

API 38
------

This breaking API update is due to the migration of the global FATES switches from the parameter file to the HLM namelists.  This update
will help improve testing and calibration automation by avoiding the need to generate a FATES parameter file if only the switch setting
changes.

+---------------------------+----------------+------------+-------------+----------------------------------------------------------------+
| FATES Tag                 | CTSM Tag       | E3SM Hash  | Update Type | Short description                                              |
+===========================+================+============+=============+================================================================+
| `sci.1.82.2_api.38.0.0`_  |                |            | Bug fix     | Harvesting bug fix for unoccupied canopy area                  |
+---------------------------+                +            +-------------+----------------------------------------------------------------+
| `sci.1.82.1_api.38.0.0`_  |                |            | Bug fix     | Storage calculation issue due to incorrect nutrient targets    |
+---------------------------+                +            +-------------+----------------------------------------------------------------+
| `sci.1.82.0_api.38.0.0`_  |                |            | Software    | Refactor to leaf biophysics and addition of unit tests         |
+---------------------------+                +            +-------------+----------------------------------------------------------------+
| `sci.1.81.2_api.38.0.0`_  |                |            | Software    | Refactor spitfire order of operations                          |
+---------------------------+                +            +-------------+----------------------------------------------------------------+
| `sci.1.81.1_api.38.0.0`_  | `ctsm5.3.027`_ | `64046ec`_ | Software    | Migrate global FATES switches from parameter file to namelist  |
+---------------------------+----------------+------------+-------------+----------------------------------------------------------------+

API 37
------

API 37 captures the spitfire fuel equations refactor changes which renames and moves related variables into a new module.

+---------------------------+----------------+------------+-------------+----------------------------------------------------------------+
| FATES Tag                 | CTSM Tag       | E3SM Hash  | Update Type | Short description                                              |
+===========================+================+============+=============+================================================================+
| `sci.1.81.1_api.37.1.0`_  |                |            | Software    | Patch convservation method added for two-stream radiation      |
+---------------------------+                +            +-------------+----------------------------------------------------------------+
| `sci.1.81.0_api.37.1.0`_  | `ctsm5.3.025`_ | `64046ec`_ | Science     | Grazing feature added and default parameter file update        |
+---------------------------+----------------+------------+-------------+----------------------------------------------------------------+
| `sci.1.80.14_api.37.0.0`_ |                |            | Software    | Patch numbering and no-competition clean up                    |
+---------------------------+                +            +-------------+----------------------------------------------------------------+
| `sci.1.80.13_api.37.0.0`_ |                |            | Software    | Refactor cohort insertion and sorting methods                  |
+---------------------------+                +            +-------------+----------------------------------------------------------------+
| `sci.1.80.12_api.37.0.0`_ |                |            | Bug fix     | Fix sort_cohorts to make sure cohort ordering is preserved     |
+---------------------------+                +            +-------------+----------------------------------------------------------------+
| `sci.1.80.11_api.37.0.0`_ |                |            | Bug fix     | Land use bug fixes and updates to the history output           |
+---------------------------+                +            +-------------+----------------------------------------------------------------+
| `sci.1.80.10_api.37.0.0`_ |                |            | Software    | Add runtime checks on the allometry mode settings              |
+---------------------------+                +            +-------------+----------------------------------------------------------------+
| `sci.1.80.9_api.37.0.0`_  |                |            | Bug fix     | Fix vegetation temperature weighting during phenology          |
+---------------------------+                +            +-------------+----------------------------------------------------------------+
| `sci.1.80.8_api.37.0.0`_  |                |            | Bug fix     | Corrects hydro sapflow output                                  |
+---------------------------+                +            +-------------+----------------------------------------------------------------+
| `sci.1.80.7_api.37.0.0`_  |                |            | Software    | Adds mechanism to avoid LAI exceeding allometry maximums       |
+---------------------------+                +            +-------------+----------------------------------------------------------------+
| `sci.1.80.6_api.37.0.0`_  |                |            | Bug fix     | Corrects when burnt fuel is zero'd and litter mass update      |
+---------------------------+                +            +-------------+----------------------------------------------------------------+
| `sci.1.80.5_api.37.0.0`_  |                |            | Software    | Refactor to the SPITFIRE rate-of-spread subroutine             |
+---------------------------+                +            +-------------+----------------------------------------------------------------+
| `sci.1.80.4_api.37.0.0`_  |                |            | Bug fix     | Corrects lack of direct mortality with area-based logging      |
+---------------------------+                +            +-------------+----------------------------------------------------------------+
| `sci.1.80.3_api.37.0.0`_  |                |            | Software    | Comprehensive singularity correction update to two-stream      |
+---------------------------+                +            +-------------+----------------------------------------------------------------+
| `sci.1.80.2_api.37.0.0`_  |                |            | Bug fix     | Avoids divide-by-zero crash when 100% allocation is to seeds   |
+---------------------------+                +            +-------------+----------------------------------------------------------------+
| `sci.1.80.1_api.37.0.0`_  |                |            | Bug fix     | Grass-specific cross-sectional area calculation fix            |
+---------------------------+                +            +-------------+----------------------------------------------------------------+
| `sci.1.80.0_api.37.0.0`_  |                |            | Science     | Growth respiration moved to daily timestep                     |
+---------------------------+                +            +-------------+----------------------------------------------------------------+
| `sci.1.79.3_api.37.0.0`_  | `ctsm5.3.012`_ | `13abf59`_ | Software    | Refactor SPITFIRE fuel equations                               |
+---------------------------+----------------+------------+-------------+----------------------------------------------------------------+

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

Pre-API 36
----------

For compatibility with API 35 and earlier, please see :doc:`/user/Table-of-FATES-API-and-HLM-STATUS`.


.. [#] Users wanting to run non-land use run modes should avoid this tag due `issue #1221`_.  The next fates tag addresses this issue.

.. _sci.1.83.0_api.39.0.0: https://github.com/NGEET/fates/releases/tag/sci.1.83.0_api.39.0.0
.. _sci.1.82.8_api.39.0.0: https://github.com/NGEET/fates/releases/tag/sci.1.82.8_api.39.0.0
.. _sci.1.82.7_api.39.0.0: https://github.com/NGEET/fates/releases/tag/sci.1.82.7_api.39.0.0
.. _sci.1.82.6_api.39.0.0: https://github.com/NGEET/fates/releases/tag/sci.1.82.6_api.39.0.0
.. _sci.1.82.5_api.39.0.0: https://github.com/NGEET/fates/releases/tag/sci.1.82.5_api.39.0.0
.. _sci.1.82.4_api.39.0.0: https://github.com/NGEET/fates/releases/tag/sci.1.82.4_api.39.0.0
.. _sci.1.82.3_api.39.0.0: https://github.com/NGEET/fates/releases/tag/sci.1.82.3_api.39.0.0

.. _sci.1.82.2_api.38.0.0: https://github.com/NGEET/fates/releases/tag/sci.1.82.2_api.38.0.0
.. _sci.1.82.1_api.38.0.0: https://github.com/NGEET/fates/releases/tag/sci.1.82.1_api.38.0.0
.. _sci.1.82.0_api.38.0.0: https://github.com/NGEET/fates/releases/tag/sci.1.82.0_api.38.0.0
.. _sci.1.81.2_api.38.0.0: https://github.com/NGEET/fates/releases/tag/sci.1.81.2_api.38.0.0
.. _sci.1.81.1_api.38.0.0: https://github.com/NGEET/fates/releases/tag/sci.1.81.1_api.38.0.0
.. _sci.1.81.1_api.37.1.0: https://github.com/NGEET/fates/releases/tag/sci.1.81.1_api.37.1.0
.. _sci.1.81.0_api.37.1.0: https://github.com/NGEET/fates/releases/tag/sci.1.81.0_api.37.1.0
.. _sci.1.80.14_api.37.0.0: https://github.com/NGEET/fates/releases/tag/sci.1.80.14_api.37.0.0
.. _sci.1.80.13_api.37.0.0: https://github.com/NGEET/fates/releases/tag/sci.1.80.13_api.37.0.0
.. _sci.1.80.12_api.37.0.0: https://github.com/NGEET/fates/releases/tag/sci.1.80.12_api.37.0.0
.. _sci.1.80.11_api.37.0.0: https://github.com/NGEET/fates/releases/tag/sci.1.80.11_api.37.0.0
.. _sci.1.80.10_api.37.0.0: https://github.com/NGEET/fates/releases/tag/sci.1.80.10_api.37.0.0
.. _sci.1.80.9_api.37.0.0: https://github.com/NGEET/fates/releases/tag/sci.1.80.9_api.37.0.0
.. _sci.1.80.8_api.37.0.0: https://github.com/NGEET/fates/releases/tag/sci.1.80.8_api.37.0.0
.. _sci.1.80.7_api.37.0.0: https://github.com/NGEET/fates/releases/tag/sci.1.80.7_api.37.0.0
.. _sci.1.80.6_api.37.0.0: https://github.com/NGEET/fates/releases/tag/sci.1.80.6_api.37.0.0
.. _sci.1.80.5_api.37.0.0: https://github.com/NGEET/fates/releases/tag/sci.1.80.5_api.37.0.0
.. _sci.1.80.4_api.37.0.0: https://github.com/NGEET/fates/releases/tag/sci.1.80.4_api.37.0.0
.. _sci.1.80.3_api.37.0.0: https://github.com/NGEET/fates/releases/tag/sci.1.80.3_api.37.0.0
.. _sci.1.80.2_api.37.0.0: https://github.com/NGEET/fates/releases/tag/sci.1.80.2_api.37.0.0
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

.. _ctsm5.3.034: https://github.com/ESCOMP/CTSM/releases/tag/ctsm5.3.034
.. _ctsm5.3.027: https://github.com/ESCOMP/CTSM/releases/tag/ctsm5.3.027
.. _ctsm5.3.025: https://github.com/ESCOMP/CTSM/releases/tag/ctsm5.3.025
.. _ctsm5.3.012: https://github.com/ESCOMP/CTSM/releases/tag/ctsm5.3.012
.. _ctsm5.3.003: https://github.com/ESCOMP/CTSM/releases/tag/ctsm5.3.003
.. _ctsm5.2.013: https://github.com/ESCOMP/CTSM/releases/tag/ctsm5.2.013

.. _PR 6918: https://github.com/E3SM-Project/E3SM/pull/6918
.. _PR 7027: https://github.com/E3SM-Project/E3SM/pull/7027
.. _64046ec: https://github.com/E3SM-Project/E3SM/commit/64046ec75587d9fcd035f22553192665dd540f56
.. _ef0abe7: https://github.com/E3SM-Project/E3SM/commit/ef0abe727bb4f3286a40d2350aaded5030197615
.. _377b2d3: https://github.com/E3SM-Project/E3SM/commit/377b2d31d77977efc0f5edf79ba243377f668517
.. _f14a3cf: https://github.com/E3SM-Project/E3SM/commit/f14a3cf738fc56f287665a49231b461878770958

.. _13abf59: https://github.com/E3SM-Project/E3SM/commit/13abf5991f234f8c64237566e228441465180f7e

.. _issue #1221: https://github.com/NGEET/fates/issues/1221
