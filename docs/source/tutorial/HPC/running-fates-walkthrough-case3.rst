Case 3 - PFTs and Global Runs
-----------------------------

The third simulation gives a practical learning experience on the following objectives:
- Learn about FATES Plant Functional Types (PFTs)
- Learn about changing the PFT parameter file
- Do a global run
- Plot output of global run. (matlab)

1. The FATES Parameter File
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Parameter files are required to be in the NETCDF binary format to be read in by both E3SM and CTSM.  

NETCDF binary files can also be transcribed into a text file, these files are commonly called the "CDL" version of the netcdf file.

============= ===========
Netcdf Binary Netcdf Text 
============= ===========
.nc           .cdl      
============= ===========

FATES maintains a few "default" parameter files in the "CDL" text form.  These default values have no expectation of being scientifically valid. Their primary purpose is to help us test the features of the model, and also provide a reasonable starting point for users.

Both of these files can be found in the fates folder system as well.  Change into that directory.

For E3SM: 

.. code-block:: shell
    
    $ cd <path>/FatesTutorial_Feb2019/E3SM/components/clm/src/external_models/fates/parameter_files

For CTSM:

.. code-block:: shell
    
    $ cd <path>/FatesTutorial_Feb2019/ctsm/src/fates/parameter_files


Our next objective is to modify the contents of the 2 PFT tropical parameter file.  But start by making a copy of it, so the original is not changed.

.. code-block:: shell
    
    $ cp fates_params_default.cdl fates_params_tutorial_run3.cdl
    $ emacs -nw fates_params_tutorial_run3.cdl

2. Modifying the parameter file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Lets create a trait trade-off, with wood density and the soil water potential at stomatal closure.  High density wood will take more carbon to grow in size, yet a lower negative suction will allow it to be productive in dry conditions.

=========================== ================== ======= =======
Trait                       Variable Name      PFT 1   PFT 2 
=========================== ================== ======= =======
Wood Density                fates_wood_density 0.65    0.75 
Suction at stomatal closure fates_smpsc        -200000 -300000
=========================== ================== ======= =======

There are at least two ways to do this change:

Option 1.  Edit the CDL text file and convert back to netcdf

The text file has three sections. The top section describes the dimensions, the second section describes the variables' metadata, and the final section holds the actual values for the variables (i.e. data). Navigate to the last section looking for "fates_wood_density" and "fates_smpsc" to make the changes (or be creative).

.. code-block:: shell
    
    $ ncgen -o fates_params_tutorial_run3.nc fates_params_tutorial_run3.cdl

Option 2. Use a the FATES parameter modification python `script`_ (ideal of batch processes). Note that you must first convert your text file to binary format, and copy the script into the parameter file folder.

.. _script: https://github.com/NGEET/fates/blob/master/tools/modify_fates_paramfile.py

**Remember to load the same python environment described in run 2**

.. code-block:: shell
    
    $ ncgen -o fates_params_tutorial_run3.nc fates_params_tutorial_run3.cdl
    $ cp ../tools/modify_fates_paramfile.py .
    $ ./modify_fates_paramfile.py --help
    $ ./modify_fates_paramfile.py --var fates_wood_density --pft 1 --val 0.65 --fin fates_params_tutorial_run3.nc --fout fates_params_tutorial_run3.nc --O
    $ ./modify_fates_paramfile.py --var fates_wood_density --pft 2 --val 0.75 --fin fates_params_tutorial_run3.nc --fout fates_params_tutorial_run3.nc --O 
    $ ./modify_fates_paramfile.py --var fates_smpsc --pft 1 --val -200000.0 --fin fates_params_tutorial_run3.nc --fout fates_params_tutorial_run3.nc --O 
    $ ./modify_fates_paramfile.py --var fates_smpsc --pft 2 --val -300000.0 --fin fates_params_tutorial_run3.nc --fout fates_params_tutorial_run3.nc --O 

3. Build a Global Simulation with Modified Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Next we will create a global simulation that uses this modified parameter file.  And if you guessed this would be an unrealistic parameter set to use globally, as it has only two tropical plants, you are right.  

You can use the file you just made, or one that is pre-made found here:

.. code-block:: shell

    <path>/FatesTutorial_Feb2019/Data/ParameterFiles/fates_params_tutorial_run3.nc

Change to the scripts directory again.

For CTSM:

.. code-block:: shell
    
    $ cd FatesTutorial_Feb2019/ctsm/cime/scripts

For E3SM:

.. code-block:: shell
    
    $ cd FatesTutorial_Feb2018/E3SM/cime/scripts

A pre-made build script is available, **create_run3_f45_2pfts_fates.sh**. Read through and evaluate its contents.

**Important note: This is a bigger simulation (its the whole globe), so we will NOT be using the tutorial job-queue R4231271 for the simulation itself (which has a limited allocation),  We WILL use that queue to build the model though... (See below). When no job-queue is specified, the default "regular" is used.  This queue may take longer to be submitted, so expect it to run over-night.**

Execute the build script.

On cheyenne:  

.. code-block:: shell
    
    $ qcmd -A UCGD0004 -q R4231271 -- ./create_run3_f45_2pfts_fates.sh

On systems with no tasking-queue: 

.. code-block:: shell
    
    $ ./create_run3_f45_2pfts_fates.sh

Note that our new parameter file is being specified in the user_nl_clm file:

.. code-block:: shell
    
    #!/bin/bash                                                                                                                                                                             

    #=============================================================================================                                                                                          
    #                                                                                                                                                                                       
    # This script will BUILD a CESM/E3SM single point simulation for the 1x1_brazil resolution.                                                                                             
    # 1x1_brazil is a pre-made "resolution", meaning the support files domain/surface/etc are                                                                                               
    # already available. This is a single-site, located roughly in the southern Amazon.                                                                                                     
    #                                                                                                                                                                                       
    # This script takes NO ARGUMENTS                                                                                                                                                         
    #                                                                                                                                                                                       
    # IMPORTANT:  If you are on cheyenne, you must call this script via their qcmd command                                                                                                  
    #             This will launch a job to run this script, and is important to cheyenne.                                                                                                  
    #             You will get booted if you don't do this (well...maybe, probably).                                                                                                        
    #             Assuming your PROJECT ID IS UCGD0004, execute this script as follows:                                                                                                     
    #                                                                                                                                                                                       
    #             qcmd -A UCGD0004 -q R4231271 -- ./create_run3_f45_2pfts_fates.sh                                                                                                          
    #                                                                                                                                                                                       
    # contact rgknox@lbl.gov, rfisher@ucar.edu and cdkoven@lbl.gov with questions/comments/cake.                                                                                            
    #                                                                                                                                                                                       
    #                                                                                                                                                                                       
    # THIS SCRIPT ASSUMES YOU HAVE CREATED THE DIRECTORY "fates_tutorial", and can be found in                                                                                              
    # ${CASEROOT}                                                                                                                                                                           
    #                                                                                                                                                                                       

    #=============================================================================================                                                                                          

    # UNCOMMENT AND MODIFY FOR CESM/CTSM SYSTEM                                                                                                                                             
    CIME_MODEL=cesm
    MACH=cheyenne
    COMP=I2000Clm50Fates
    PROJECT=UCGD0004                                                                                                                                                                       

    # USER MAY WANT TO RE-NAME THESE FILES OR TRY SOMETHING DIFFERENT                                                                                                                       
    # JUST ENSURE CONSISTENCY WITH WHAT IS IN FILE: "user_nl_clm"                                                                                                                           

    FATES_PARAM_FILE=fates_params_tutorial_run3.nc
    FATES_PARAM_FILE_PATH=../../../../Data/ParameterFiles/

    ./create_newcase --case run3_f45_2pfts --res f45_f45_mg37 --compset ${COMP} --mach ${MACH} --project ${PROJECT} --run-unsupported

    cd run3_f45_2pfts

    CASEDIR=`pwd`

    cp ${FATES_PARAM_FILE_PATH}/${FATES_PARAM_FILE} .

    ./xmlchange --id DEBUG --val FALSE
    ./xmlchange --id STOP_N --val 10
    ./xmlchange --id RUN_STARTDATE --val '2001-01-01'
    ./xmlchange --id STOP_OPTION --val nyears
    ./xmlchange --id CLM_FORCE_COLDSTART --val on
    ./xmlchange --id JOB_WALLCLOCK_TIME --val 3:00
    ./xmlchange --id DATM_CLMNCEP_YR_START --val 1996
    ./xmlchange --id DATM_CLMNCEP_YR_END --val 2001

    ./case.setup

    cat >> user_nl_clm <<EOF                                                                                                                                                                
    fates_paramfile = "`pwd`/${FATES_PARAM_FILE}"                                                                                                                                           
    EOF                                                                                                                                                                                     

    ./case.build

    cd $WORKDIR

7. Submit the run
^^^^^^^^^^^^^^^^^

.. code-block:: shell
    
    $ cd run3_f45_2pfts
    $ ./case.submit

8. Visualizing Global/Gridded Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
An example of the output from this simulation is pre-made.  Change over to that directory:

.. code-block:: shell
    
    $ cd <path>/FatesTutorial_Feb2019/Data/run3_f45_2pfts_output

A MATLAB script in this folder provides an example method for regional analysis. The file is set to read a history file from December of 2010 in the current directory, but can also be changed to look in other locations.  This file corresponds to the last month of simulation for our example simulation, it is provided in the folder.  

This analysis may require some processing power, so we will first request an interactive node to perform the work:

On Cheyenne:

.. code-block:: shell

    $ qsub -I -l select=1:ncpus=1 -l walltime=00:30:00 -A UCGD0004 -q R4231271

if the R4231271 queue is not loading, you can use the regular queue

.. code-block:: shell
    
    $ qsub -I -l select=1:ncpus=1 -l walltime=00:30:00 -A UCGD0004 -q regular

On NERSC:

Please consult their documentation, this may or may not be allowed on the head-node.

Once the interactive queue has been loaded, go ahead and load the matlab module and run matlab: 

.. code-block:: shell

    $ module load matlab
    $ matlab -nodesktop -nosplash

After starting matlab, you will then be given a prompt inside matlab's environment. Go ahead and execute the script like so: 

.. code-block:: shell
    
    $ matlab-prompt> fates_pft_climate_envelopes_tutorial

9. Discussion Time!
^^^^^^^^^^^^^^^^^^^
Sometimes its nice to just sit back, put your feet up, and think about global Mean Annual Temperature and its effects on competition, right?

Question 1: Take a look at the map of biomass fraction of the second PFT in your test.  Given how the parameters of PFT 2 differ from PFT 1, do the locations around the world where it is more or less competitive make sense to you?

Question 2: One of the plots showed the biomass fraction as a function of mean annual temperature and mean precipitation.  Can you think of other metrics that may also show structure or pattern differences in biomass fraction?

This completes the Run 3 unit.