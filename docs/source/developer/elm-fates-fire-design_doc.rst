ELM-FATES Fire Data API Design Document
=======================================

Introduction
------------

The goal of this software update is to enable FATES to make use of the fire data provided by the ELM host land model.  FATES currently has a fire data API design that is compatible with CLM.

Design Considerations
---------------------

- The CLM-FATES fire API makes use of `factory type`_ methods to enable the CLM CN-fire code to utilize the same data input methods across different CN versions without having to use a lot of `case select` code.  This is the basis for the API.  ELM's fire model isn't set up this way currently.

.. _`factory type`: https://en.wikipedia.org/wiki/Factory_(object-oriented_programming)

Assumptions and Dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^




General Constraints
^^^^^^^^^^^^^^^^^^^


Solutions
---------


Design and Architecture
-----------------------


System diagram or flowchart
^^^^^^^^^^^^^^^^^^^^^^^^^^^


Algorithm or Pseudo code for main components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. pcode::
  
  \begin{algorithm}
  \caption{pseudocode}
  \begin{algorithmic}
  \PROCEDURE{Placeholder}{$input$}
  \ENDPROCEDURE
  \end{algorithmic}
  \end{algorithm}

Rollout Plan
------------


Future Update Plan
------------------


Appendix
--------
