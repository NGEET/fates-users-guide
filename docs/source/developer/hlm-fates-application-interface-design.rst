
HLM-FATES Interface Design Document
=======================================

Introduction
------------
.. Discuss the design origins, intent and goals.  What is the problem statement?  If there are any specification documents, link them in Appendix.
The interface between the host land models (HLMs) and FATES is designed with the following goals in mind:

1. Reduced the amount of necessary shared code
2. Provide for a common vocabulary between the HLM and FATES for associated variables
3. Provide a standard design pattern for associating HLM and FATES variables
4. Improve development management of different interface needs based on HLM

Note that this document is being written in the context of a refactor associated with pull request `NGEET/fates#1477`_.  The impetus for this work is to allow FATES to operate with multiple soil columns in the host land model, which is driven by scientific goals per NGEE-Arctic Phase 4 (specifically Cross-cut Task 4).  Prior to this design implimentation, the interface made some assumptions about how FATES and HLM variables are associated with each other that would make accomplishing the multi-column operation difficult.

.. _`NGEET/fates#1477`: https://github.com/NGEET/fates/pull/1477

Design Considerations
---------------------
.. Describe the issues that need to be addressed before creating a design solution.

Assumptions and Dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. Describe any assumptions that may be wrong or any dependencies on other things

General Constraints
^^^^^^^^^^^^^^^^^^^
.. Describe any constraints that could have an impact on the design of the software.

Solutions
---------
.. Section should include alternative implementations/solutions.  Is it feasible? How much effort does it need for each approach? Pros/cons of each approach.  Document alternatives, why you made the decision and how it will affect the team and project.


Design and Architecture
-----------------------
..  Provide a general overview of the software layout

System diagram or flowchart
^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. Interaction diagram of various inputs, outputs, sub systems and dependencies.
Order of operations:

1. Initialize the interface registry arrays (InitializeInterfaceRegistry)
2. Register data variables associated with keys (RegisterInterfaceVariables)
3. Initialize the FATES sites (InitializeFatesSites)
4. Initialize the boundary conditions (InitialBoundaryConditions)
5. Update registered interface variables (UpdateInterfaceVariables)
6. Update “specialized” variable sets as necessary (e.g. UpdateLitterFluxes)


Rollout Plan
------------
.. Define the roll-out phases and tests you plan to do

Future Update Plan
------------------
.. Sketch out future updates if known

Implementation Notes and Lessons Learned
----------------------------------------
.. Optional section summarizing lessons learned after the design has been successfully implemented

Appendix
--------
.. References, links to additional documentation
