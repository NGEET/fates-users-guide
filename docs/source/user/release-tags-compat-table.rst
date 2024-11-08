Release, tag and HLM API compatibility tables
=============================================

The following table list the FATES API and the corresponding HLM tag associated with that API update.  Note that CTSM provides a specific tag for each of its merge commits to the master branch whereas E3SM does not.  As such, the hash for the relevant merge commit is provided for E3SM.  Entries that specifically link to a pull request (e.g. PR#XXXX) are provided to note updates which have not been integrated yet, but are pending.  The table may also include future planned API updates without links to provide users an advanced look at what updates are forthcoming.

API 36
------

+--------------------------+----------------+------------+----------------------------------------------------------------+
| FATES Tag                | CTSM Tag       | E3SM Hash  | Description                                                    |
+==========================+================+============+================================================================+
| `sci.1.79.0_api.36.1.0`_ |                |            | Time integrated flux diagnostics                               |
+--------------------------+                +            +----------------------------------------------------------------+
| `sci.1.78.3_api.36.1.0`_ | `ctsm5.3.003`_ | `ef0abe7`_ | Default parameter file update (arctic shrubs, grass allometry) |
+--------------------------+----------------+------------+----------------------------------------------------------------+

.. _sci.1.79.0_api.36.1.0: https://github.com/NGEET/fates/releases/tag/sci.1.79.0_api.36.1.0
.. _sci.1.78.3_api.36.1.0: https://github.com/NGEET/fates/releases/tag/sci.1.78.3_api.36.1.0

.. _ctsm5.3.003: https://github.com/ESCOMP/CTSM/releases/tag/ctsm5.3.003

.. _ef0abe7: https://github.com/E3SM-Project/E3SM/commit/ef0abe727bb4f3286a40d2350aaded5030197615
