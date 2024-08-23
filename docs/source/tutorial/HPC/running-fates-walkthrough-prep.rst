Preparations
------------

1. Connect to your HPC

.. code-block:: shell
   
   $ ssh -Y <user-name>@cheyenne.ucar.edu

.. code-block:: shell
   
   $ ssh -Y <user-name>@edison.nersc.gov

**Windows users**:  There are various ssh applications available, it seems most users using `MobaXterm`_ have had success connecting to HPC machines and getting windowing to work.  Winslow Hansen found this helpful `thread`_ that may help solve problems related to authentication and windows forwarding:

.. _MobaXterm: https://mobaxterm.mobatek.net/
.. _thread: https://unix.stackexchange.com/questions/412065/ssh-connection-x11-connection-rejected-because-of-wrong-authentication

1. Two important locations, home and scratch

**Home** **Folder**:

You log-into your home folder.  You can return to the home folder, from anywhere, by the "cd" command with no other arguments.

.. code-block:: shell
   
   $ cd
   $ pwd

**Scratch** **Folder**:

Scratch folders are large file-system partitions, often with high input-output rates, and are used for storing model output.  The CIME software will automatically place model output in your scratch folder, unless you tell it otherwise.

- For cheyenne (has a system environment variable), the scratch folder has the path /glade/scratch/$USER, where $USER is the environment variable for your user name.   1) Print out your user name, 2) change into your scratch directory, 3) verify that you have moved into your scratch folder by "Printing" you "working directory" (PWD), and then 4) change back to your home directory.

.. code-block:: shell
   
   $ echo $USER
   $ cd /glade/scratch/$USER
   $ pwd
   $ cd

3. Retrieve and open the tutorial data package

The tutorial package is stored in a shared folder on OSF: https://osf.io/rp6g8/. Use ``wget`` to retrieve it. We recommend downloading it to your home folder for simplicity sake, your user's scratch space is also a good location.

Note: The tutorial package was last updated for tag ``sci.1.43.3_api.14.2.0``, as of March 2nd 2021.  Use the updated package, and update the name of the tutorial folder in the instructions accordingly. 

On any workstation:

.. code-block:: shell
   
   $ cd ~/
   $ wget -O FatesTutorial_Mar2021.tar.gz https://osf.io/6uz83/download

Once this is downloaded, untar the file.
	
.. code-block:: shell
   
   $ gunzip FatesTutorial_<>.tar.gz
   $ tar -xvf FatesTutorial_<>.tar

or optionally

.. code-block:: shell
   
   $ tar -xzvf FatesTutorial_<>.tgz

Wherever you put this folder, we will call this "**FATES** **Tutorial** **Root**".

Contents of packet:

.. code-block:: shell
   
   $ cd FatesTutorial_<>
   $ ls 
   ./  ../  Data/  TestCloneSpace/  Tools/  ctsm/  doc/

4. (optional) Practice a git clone

The package provides all the necessary setup for this tutorial and it is assumed that you already have trained on how to download or clone CTSM/E3SM.  The remaining sections provide optional practice guiding you through the necessary steps for cloning, checking out and syncing fates to the terrestrial models.  Feel free to :ref:`return to walk-through home <Introduction to Running FATES>` if you would like to skip the following optional sections.

Move into the folder space provided for the optional practice:

.. code-block:: shell
   
   $ cd TestCloneSpace

Clone the terrestrial models:

- For E3SM:

.. code-block:: shell
   
   $ git clone https://github.com/E3SM-Project/E3SM.git
   $ cd E3SM

- For CTSM:

.. code-block:: shell
   
   $ git clone https://github.com/ESCOMP/ctsm.git
   $ cd ctsm

5. (optional) FATES as a component 

Important step! FATES is a **component** of the CLM and ELM land-models. Each has its own method of initializing and retrieving FATES:

- For E3SM, fates is handled as a "sub-module".  Retrieve and update all sub-modules in ACME via:

.. code-block:: shell
   
   $ git submodule update --init --recursive

- For CTSM, a script is used to import fates.

.. code-block:: shell
   
   $ ./manage_externals/checkout_externals

6. (optional) Directory structure.

FATES source code is found in the fates/ folder with the following paths. Take a look!

- For E3SM:

.. code-block:: shell
   
   $ cd components/clm/src/external_models/fates

- For CTSM:

.. code-block:: shell
   
   $ cd src/fates/

7. (optional) Distinguishing "remotes" 

Now inside fates/ folder. Note the git origin, and its implications:

.. code-block:: shell
   
   $ git remote -v

- For E3SM:


.. code-block:: shell
   
   $ git remote -v
   origin	git@github.com:NGEET/fates.git (fetch)
   origin	git@github.com:NGEET/fates.git (push)

- For CTSM:

.. code-block:: shell
   
   $ git remote -v
   origin	https://github.com/NCAR/fates-release (fetch)
   origin	https://github.com/NCAR/fates-release (push)

The FATES folder points to a different git repository, compared with the rest of the land-model.  Move back into the parent directory and compare.

.. code-block:: shell
   
   $ cd ..
   $ git remote -v

- For E3SM: 

.. code-block:: shell
   
   $ git remote -v
   origin	https://github.com/E3SM-Project/E3SM.git (fetch)
   origin	https://github.com/E3SM-Project/E3SM.git (push)

- For CTSM:

.. code-block:: shell
   
   $ git remote -v
   origin	https://github.com/ESCOMP/ctsm.git (fetch)
   origin	https://github.com/ESCOMP/ctsm.git (push)

8. (optional) Staying up-to-date with NGEET/ master

Synchronize your "master" branch with the NGEET/ repository

.. code-block:: shell
   
   $ cd fates
   $ git remote add ngeet_repo https://github.com/NGEET/fates.git
   $ git remote -v
   $ git fetch ngeet_repo
   $ git checkout master 
   $ git pull ngeet_repo master
