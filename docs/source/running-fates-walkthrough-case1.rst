Case 1 - A Simple Case
----------------------

1. The "Scripts" Directory
^^^^^^^^^^^^^^^^^^^^^^^^^^
Move into the scripts directory of your respective model system (E3SM/CTSM). This is the folder from which most all simulation environments will be created.

For E3SM:

.. code-block:: shell

    $ cd <path>/FatesTutorial_Feb2019/E3SM/cime/scripts

For CTSM:

.. code-block:: shell
    
    $ cd <path>/FatesTutorial_Feb2019/ctsm/cime/scripts

2. An example run script
^^^^^^^^^^^^^^^^^^^^^^^^
View "create_run1_1x1brazil_fates.sh" with your favorite editor (nedit, gedit, emacs) and review the contents of file. 

.. code-block:: shell

    $ emacs -nw create_run1_1x1brazil_fates.sh

emacs quick tips:

- save command:  ctrl-x ctrl-s
- close editor:  ctrl-x ctrl-c


Minor changes to the script, to accommodate your computer/model combination will be likely.  The script text for a CTSM run on cheyenne is provided here for convenience:

.. code-block:: shell
    
    #!/bin/bash                                                                                                                                                           
    #=============================================================================================
    #
    # This script will BUILD a CESM single point simulation for the 1x1_brazil resolution.                                                                                                    
    # 1x1_brazil is a pre-made "resolution", meaning the support files domain/surface/etc are                                                                                                 
    # already available. This is a single-site, located roughly in the southern Amazon.                                                                                                       
    #                                                                                                                                                                                         
    # This script takes NO ARGUMENTS                                                                                                                                                           
    #                                                                                                                                                                                         
    #                                                                                                                                                                                         
    # IMPORTANT:  If you are on cheyenne, you must call this script via their qcmd command                                                                                                    
    #             This will launch a job to run this script, and is important to cheyenne.                                                                                                    
    #             You will get booted if you don't do this (well...maybe, probably).                                                                                                          
    #             Assuming your PROJECT ID IS UCGD0004, execute this script as follows:                                                                                                       
    #                                                                                                                                                                                         
    #             qcmd -A UCGD0004 -q R4231271 -- ./create_run1_1x1brazil_fates.sh                                                                                                            
    #                                                                                                                                                                                         
    #                                                                                                                                                                                         
    # contact rgknox@lbl.gov with questions/comments/cake.                                                                                                                                    
    #=============================================================================================                                                                                            


    # UNCOMMENT FOR CHEYENNE CESM/CTSM SYSTEM                                                                                                                                                 
    CIME_MODEL=cesm
    MACH=cheyenne
    COMP=I2000Clm50FatesRs
    PROJECT=UCGD0004
    JOB_QUEUE=R4231271

    WORKDIR=`pwd`


    ./create_newcase --case run1_1x1brazil --res 1x1_brazil --compset ${COMP} --mach ${MACH} --project ${PROJECT} --run-unsupported --queue ${JOB_QUEUE}

    cd run1_1x1brazil

    ./xmlchange --id STOP_N --val 5
    ./xmlchange --id RUN_STARTDATE --val '2001-01-01'
    ./xmlchange --id STOP_OPTION --val nyears
    ./xmlchange --id DATM_CLMNCEP_YR_START --val 1996
    ./xmlchange --id DATM_CLMNCEP_YR_END --val 2001
    ./xmlchange --id CLM_FORCE_COLDSTART --val on


    ./case.setup
    ./case.build


3. Execute the Build
^^^^^^^^^^^^^^^^^^^^
One can either execute the script itself, or work through the scripts commands, sequentially entering them in the terminal.

On cheyenne:  

.. code-block:: shell
    
    $ qcmd -A UCGD0004 -q R4231271 -- ./create_run1_1x1brazil_fates.sh

On systems with no tasking-queue:

.. code-block:: shell

    $ ./create_1x1brazil_fates.sh

This does everything but run the job, but ultimately creates:
- An executable
- Namelist, parameter-files and pointers to the data streams in-out of execution
- A script to call the executable, one which calls the MPI environment correctly

4. Execute the Simulation
^^^^^^^^^^^^^^^^^^^^^^^^^
Step into the "case folder", and execute:

.. code-block:: shell

    $ cd run1_1x1brazil
    $ ./case.submit

5. Output
^^^^^^^^^
Output files will often take up **lots of space** , more than the scripts and code that is used to build and execute the model.  Therefore, the model developers make it so output (and other things, including the executable itself) will automatically be sent to a user's scratch folder, where space typically is unconstrained.  Lets go there:

On cheyenne:

.. code-block:: shell

    $ cd /glade/scratch/$USER/run1_1x1brazil

On NERSC:

.. code-block:: shell
    
    $ cd $SCRATCH/<user>/run1_1x1brazil

The simulation will generate "history" files. These files are for diagnosing model predictions/estimations, or simply the standard model output. While the model is running, they appear in the run/ directory, and are sometimes archived and moved again when the simulation completes.

Sample of output from Simulation 1 is available in the FatesTutorial_Feb2019 packet.

.. code-block:: shell
    
    $ cd <path>/FatesTutorial_Feb2019/Data/run1_1x1brazil_output

6. Simple Visualization
^^^^^^^^^^^^^^^^^^^^^^^
Some HPC machines, like cheyenne, have a netcdf visualization tool "ncview".  This GUI based tool can evaluate the contents of a file.

For this example, all of the output from run1 was "concatenated" together into a file called run1.nc. We will view the 1D output using ncview.

.. code-block:: shell

    $ module load ncview
    $ ncview run1.nc

7. Discussion Time!
^^^^^^^^^^^^^^^^^^^
Try to walk through the example script and explain to yourself or a bear what is being achieved in each step.  For instance, what is a compset?  What are those XMLCHANGE commands doing?

This completes the Run 1 unit.
