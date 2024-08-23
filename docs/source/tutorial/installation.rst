Installation
------------

This document provides a step-by step instructions to installing fates.

Clone a FATES supported host land model git repository to your machine
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

FATES is a component to a few host land models, including `E3SM`_ and `CTSM`_, both of which are the focus of this tutorial.  In a terminal shell, run the following `git clone` command to download the latest version of the host land model of your choosing:

CTSM:

.. code-block:: shell

   $ git clone git@github.com:ESCOMP/CTSM.git
   
   
E3SM:

.. code-block:: shell

   $ git clone git@github.com:E3SM-Project/E3SM.git

.. _E3SM: https://github.com/E3SM-Project/E3SM
.. _CTSM: https://github.com/ESCOMP/ctsm

Initialize the host land model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The host land models need to be initialized to pull in the correct versions of their respective component models, including FATES.  Change into the recently cloned host land model directory and run the following command:

CTSM:

.. code-block:: shell
   
   $ ./manage_externals/checkout_externals
   
E3SM:

.. code-block:: shell
   
   $ git submodule update --init --recursive
   
The host land model should now contain the appropriate version of FATES for the latest version of the host land model.  Note that the directory structure for the host land models differs.  FATES can be found by changing into the following directories from the top of the host land model directory:

CTSM:

.. code-block:: shell
   
   $ cd src/fates
   
E3SM:

.. code-block:: shell
   
   $ cd components/elm/src/external_models/fates
   
This completes the installation tutorial.