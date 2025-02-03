Case 2 - Adding Variables and Investigating Ecosystem Structure
---------------------------------------------------------------

The second simulation gives a practical learning experience on the following objectives:
- Learn about different FATES output
- Learn about adding new history variables
- Visualizing long-term FATES-specific size-structured dynamics

1. The FATES code - output handling
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Before jumping into the creation of a new case, lets first open up the FATES source file that handles "history" output.  See: https://github.com/NGEET/fates/blob/master/main/FatesHistoryInterfaceMod.F90

Or, this file can be found in your local copy of FATES, in main/FatesHistoryInterfaceMod.F90.

Some take-aways from this file:
- History variables handle all of our "diagnostic" outputs that are written to file
- These variables are stored in "derived type" objects, via a registry
- These objects have metadata that define each variable (dimensions, number types, unit definitions, long name definitions)
- These types are necessary because we need to pass an arbitrary list of things to the host model, because it handles output
- We have some special "multi-plexed" dimensions
- The naming convention of variables indicates its dimensioning

The object lists are passed to the host model in "the interface".  The process is similar in E3SM/CTSM, where the land-model's native functions are used to set-up pointers to the FATES object arrays.

https://github.com/ESCOMP/ctsm/blob/master/src/utils/clmfates_interfaceMod.F90#L1867

2. Selecting Output Variables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Looking at main/FatesHistoryInterfaceMod.F90 is the best way to understand what variables are available for output.  

In this example, lets craft a simulation that will generate the following diagnostics:

- Productivity and canopy structure (site x patch-age)
- Tree abundance and basal area (site x size x canopy position)
- Growth rate (site x size x canopy position)
- Mortality rate (site x size x canopy position)

After reviewing main/FatesHistoryInterfaceMod.F90, and using keyword searches, we have the following variables:

- GPP_BY_AGE   (inactive)
- PATCH_AREA_BY_AGE (active)
- CANOPY_AREA_BY_AGE (active)
- BA_SCLS      (active)
- NPLANT_CANOPY_SCLS         (active)
- NPLANT_UNDERSTORY_SCLS     (active)
- DDBH_CANOPY_SCLS    (active)
- DDBH_UNDERSTORY_SCLS    (active)
- MORTALITY_CANOPY_SCLS (active)
- MORTALITY_UNDERSTORY_SCLS  (active)

3. Specifying Output Variables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Many variables, those set to "active", will be added to the "h0" history file by default.  Although, to save space the user can set a variable ``hist_empty_htapes = .true.``, where no variables unless explicitly stated, will be sent to output.

Because this is a long simulation, with complex dimensions, we will save space, and explicitly list the variables we want.  

These variables should be added to the user_nl_clm file in the case directory.  In a simple example, with only 1 type of output file, and all other variables removed except explicitly this group of variables:

.. code-block:: shell

    hist_empty_htapes = .true.
    hist_fincl1       = 'GPP_BY_AGE','PATCH_AREA_BY_AGE','CANOPY_AREA_BY_AGE','BA_SCLS','NPLANT_CANOPY_SCLS',\
    'NPLANT_UNDERSTORY_SCLS','DDBH_CANOPY_SCLS','DDBH_UNDERSTORY_SCLS','MORTALITY_CANOPY_SCLS','MORTALITY_UNDERSTORY_SCLS'

4. Build the Run
^^^^^^^^^^^^^^^^
Building the model takes time.  We _could_ modify our Run 1 case to try out our new simulation conditions. We would avoid building the model.  But for simplicity's sake, we will perform a new build with a new case.

Return to the scripts directory, open and modify "create_run2_1x1brazil_structured_fates.sh"

Execute the build script.

On cheyenne:  

.. code-block:: shell

    $ qcmd -A UCGD0004 -q R4231271 -- ./create_run2_1x1brazil_structured_fates.sh

On systems with no tasking-queue: 

.. code-block:: shell

    $ ./create_run2_1x1brazil_structured_fates.sh

The script is provided below for convenience.

.. code-block:: shell
    
    #!/bin/bash                                                                                                                                                       

    #=============================================================================================                                                                    
    #                                                                                                                                                                 
    # This script will BUILD a CESM/E3SM single point simulation for the 1x1_brazil resolution.                                                                       
    # 1x1_brazil is a pre-made "resolution", meaning the support files domain/surface/etc are                                                                         
    # already available. This is a single-site, located roughly in the southern Amazon.                                                                               
    #                                                                                                                                                                 
    # This script taks NO ARGUMENTS                                                                                                                                   
    #                                                                                                                                                                 
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
    COMP=I2000Clm50FatesGs
    PROJECT=UCGD0004
    JOB_QUEUE=R4231271

    ./create_newcase --case run2_1x1brazil_structure --res 1x1_brazil --compset ${COMP} --mach ${MACH} --project ${PROJECT}  --queue ${JOB_QUEUE} --run-unsupported


    cd run2_1x1brazil_structure

    ./xmlchange --id STOP_N --val 10
    ./xmlchange --id RUN_STARTDATE --val '1900-01-01'
    ./xmlchange --id STOP_OPTION --val nyears
    ./xmlchange --id CLM_FORCE_COLDSTART --val on
    ./xmlchange --id RESUBMIT --val 2
    ./xmlchange --id DATM_CLMNCEP_YR_START --val 1996
    ./xmlchange --id DATM_CLMNCEP_YR_END --val 2001

    ./case.setup

    cat >> user_nl_clm <<EOF
    hist_empty_htapes = .true.
    hist_fincl1       = 'GPP_BY_AGE','PATCH_AREA_BY_AGE','CANOPY_AREA_BY_AGE', \
    'BA_SCLS','NPLANT_CANOPY_SCLS','NPLANT_UNDERSTORY_SCLS','DDBH_CANOPY_SCLS',\
    'DDBH_UNDERSTORY_SCLS','MORTALITY_CANOPY_SCLS','MORTALITY_UNDERSTORY_SCLS'
    EOF                                                                                          

    ./case.build

    cd $WORKDIR

5. Submit the Run
^^^^^^^^^^^^^^^^^
Execute the simulation when the build is complete:

.. code-block:: shell

    $ cd run2_1x1brazil_structure
    $ ./case.submit

6. How about adding new output variables?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
See :ref:`How to add a new FATES history variable` section

7. Visualizing structured FATES output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
A sample of output data has been pre-generated for visualizing run 2.  Head back to the Data directory in the packet.  Also, load python and matplotlib if not already done.

.. code-block:: shell

    $ cd <path>/FatesTutorial_Feb2019/Data/run2_1x1brazil_structured

On cori: 

.. code-block:: shell

    $ pip install --user matplotlib

On cheyenne:

.. code-block:: shell

    $ module load python/2.7.14
    $ pip install --user matplotlib
    $ pip install --user scipy

A python script has been prepared to visualize out variables of interest, it will use these newly installed modules.  See, ``plot_fates_structuredvariables.py``.   

To execute the script, simply run the python command with the script as the only argument:

.. code-block:: shell

    $ python plot_fates_structuredvariables.py

The script is also shown below:

.. code-block:: python

    import numpy as np
    from scipy.io import netcdf as nc
    from matplotlib import pyplot as plt
    from matplotlib.colors import BoundaryNorm
    from matplotlib.ticker import MaxNLocator

    ############################################################
    ### open the file and read in coordinate data
    ############################################################

    ##  get and open the history file
    ##  change the line below to point to the file that you've made,
    ##  which should be a concatenation of a bunch of FATES history files into a single file
    filename_in = 'run2_1x1brazil_structure.77years.nc'
    fin = nc.netcdf_file(filename_in)

    ## read the coordinate data for the various dimensions
    time = fin.variables['time'][:] / 365.  ### time dimension, put in unit of years
    patch_age_bins = fin.variables['fates_levage'][:]
    cohort_size_bins = fin.variables['fates_levscls'][:]

    ## define the sizes of each dimension
    ntim = len(time)
    nagebins = len(patch_age_bins)
    nsizebins = len(cohort_size_bins)

    ## because the bin edges read in define the lower edges, add a last index to each to
    ## represent the upper edge of the distribution (even though there isn't one, really)
    patch_age_bins = np.append(patch_age_bins,patch_age_bins[nagebins-1]*1.5)
    cohort_size_bins = np.append(cohort_size_bins,cohort_size_bins[nsizebins-1]*1.5)

    ############################################################
    ### read in the various variables to visualize
    ############################################################

    # productivity and canopy structure as a function of patch age
    GPP_BY_AGE = fin.variables['GPP_BY_AGE'][:]  * 86400 * 365 ## change units from per second to per year
    PATCH_AREA_BY_AGE = fin.variables['PATCH_AREA_BY_AGE'][:]
    CANOPY_AREA_BY_AGE = fin.variables['CANOPY_AREA_BY_AGE'][:]

    # population numbers and basal area as a functino of cohort size
    BA_SCLS = fin.variables['BA_SCLS'][:]
    NPLANT_CANOPY_SCLS = fin.variables['NPLANT_CANOPY_SCLS'][:]
    NPLANT_UNDERSTORY_SCLS = fin.variables['NPLANT_UNDERSTORY_SCLS'][:]

    # growth and mortality rates as a function of plant size
    DDBH_CANOPY_SCLS = fin.variables['DDBH_CANOPY_SCLS'][:]
    DDBH_UNDERSTORY_SCLS = fin.variables['DDBH_UNDERSTORY_SCLS'][:]
    MORTALITY_CANOPY_SCLS = fin.variables['MORTALITY_CANOPY_SCLS'][:]
    MORTALITY_UNDERSTORY_SCLS = fin.variables['MORTALITY_UNDERSTORY_SCLS'][:]

    # close the file
    fin.close()

    ############################################################
    ### first, look at the productivity and canopy structure
    ############################################################

    # set up the page
    fig1, (f1ax0, f1ax1, f1ax2) = plt.subplots(nrows=3, figsize=(7, 7))

    ## set up the first plot: the fractional area of patches of a given age range
    levels = np.arange(0.,1.1, 0.1)
    cmap = plt.get_cmap('Blues')
    norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)
    im = f1ax0.pcolormesh(time, patch_age_bins, PATCH_AREA_BY_AGE[:,:,0].transpose(), cmap=cmap, norm=norm)
    fig1.colorbar(im, ax=f1ax0)
    f1ax0.set_title(r'Patch Area by Age (m$^2$ patch m$^{-2}$ site)')
    f1ax0.set_xlabel('Time (yr)')
    f1ax0.set_ylabel('Patch Age (yr)')

    ## set up the second plot: the canopy coverage of patches of a given age (where 1 means canopy closure)
    levels = np.arange(0.,2.1, 0.1)
    cmap = plt.get_cmap('Greens')
    norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)
    im = f1ax1.pcolormesh(time, patch_age_bins, (CANOPY_AREA_BY_AGE / PATCH_AREA_BY_AGE)[:,:,0].transpose(), cmap=cmap, norm=norm)
    fig1.colorbar(im, ax=f1ax1)
    f1ax1.set_title(r'Canopy Area Index by Patch Age (m$^2$ canopy m$^{-2}$ patch)')
    f1ax1.set_xlabel('Time (yr)')
    f1ax1.set_ylabel('Patch Age (yr)')

    ## set up the third plot: the GPP, conditional on patch age
    levels = np.arange(0.,2500, 100)
    cmap = plt.get_cmap('Greens')
    norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)
    im = f1ax2.pcolormesh(time, patch_age_bins, (GPP_BY_AGE )[:,:,0].transpose(), cmap=cmap, norm=norm)
    fig1.colorbar(im, ax=f1ax2)
    f1ax2.set_title(r'GPP by Patch Age (g C m$^{-2}$ patch yr$^{-1}$)')
    f1ax2.set_xlabel('Time (yr)')
    f1ax2.set_ylabel('Patch Age (yr)')

    # show the plot
    fig1.tight_layout()
    plt.show()

    ############################################################
    ### next, look at the evolution of the plant size structure
    ############################################################

    # set up the page
    fig2, ((f2ax0, f2ax1), (f2ax2, f2ax3)) = plt.subplots(nrows=2, ncols=2, figsize=(9, 7))

    ## set up the first plot: evolution of basal area of plants of a given size
    levels = np.arange(0.,50, 1)
    cmap = plt.get_cmap('Greens')
    norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)
    im = f2ax0.pcolormesh(time, cohort_size_bins, BA_SCLS[:,:,0].transpose(), cmap=cmap, norm=norm)
    fig2.colorbar(im, ax=f2ax0)
    f2ax0.set_title(r'Basal Area by Size (m$^2$ ha$^{-1}$)')
    f2ax0.set_xlabel('Time (yr)')
    f2ax0.set_ylabel('Cohort Size (cm)')

    ## set up the second plot: evolution of the population density of plants of a given size
    # sum the canopy and understory plants to get size distribution of all plants
    levels = np.array([0.1,0.3,1.,3.,10.,30., 100.,300.,1000., 3000., 10000.]) # do a pseudo-log scale here
    cmap = plt.get_cmap('Greens')
    norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)
    im = f2ax1.pcolormesh(time, cohort_size_bins, (NPLANT_CANOPY_SCLS + NPLANT_UNDERSTORY_SCLS)[:,:,0].transpose(), cmap=cmap, norm=norm)
    fig2.colorbar(im, ax=f2ax1)
    f2ax1.set_title(r'# of plants by size (n ha$^{-1}$)')
    f2ax1.set_xlabel('Time (yr)')
    f2ax1.set_ylabel('Cohort Size (cm)')

    ## set up the third plot: evolution of the population density of canopy plants of a given size
    # use same levels & colorbar as second plot above
    im = f2ax2.pcolormesh(time, cohort_size_bins, (NPLANT_CANOPY_SCLS)[:,:,0].transpose(), cmap=cmap, norm=norm)
    fig2.colorbar(im, ax=f2ax2)
    f2ax2.set_title(r'# canopy plants by size (n ha$^{-1}$)')
    f2ax2.set_xlabel('Time (yr)')
    f2ax2.set_ylabel('Cohort Size (cm)')

    ## set up the fourth plot: evolution of the population density of understory plants of a given size
    # use same levels & colorbar as second plot above
    im = f2ax3.pcolormesh(time, cohort_size_bins, (NPLANT_UNDERSTORY_SCLS)[:,:,0].transpose(), cmap=cmap, norm=norm)
    fig2.colorbar(im, ax=f2ax3)
    f2ax3.set_title(r'# understory plants by size (n ha$^{-1}$)')
    f2ax3.set_xlabel('Time (yr)')
    f2ax3.set_ylabel('Cohort Size (cm)')

    # show the plot
    fig2.tight_layout()
    plt.show()



    ############################################################
    ### next, look at the growth and mortality rates
    ### for all of these rates, you need to divide the rate by the population
    ### size in post-processing to get meaningful units
    ############################################################

    # set up the page
    fig3, ((f3ax0, f3ax1), (f3ax2, f3ax3)) = plt.subplots(nrows=2, ncols=2, figsize=(9, 7))

    ## set up the first plot: growth rate (in diameter increment) in the canopy
    levels = np.arange(0.,1.5, 0.05)
    cmap = plt.get_cmap('Greens')
    norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)
    im = f3ax0.pcolormesh(time, cohort_size_bins, (DDBH_CANOPY_SCLS / NPLANT_CANOPY_SCLS)[:,:,0].transpose(), cmap=cmap, norm=norm)
    fig3.colorbar(im, ax=f3ax0)
    f3ax0.set_title(r'Growth rate of canopy plants (cm DBH yr$^{-1}$)')
    f3ax0.set_xlabel('Time (yr)')
    f3ax0.set_ylabel('Cohort Size (cm)')

    ## set up the second plot: growth rate in the understory, units as above
    levels = np.arange(0.,0.15, 0.005)
    cmap = plt.get_cmap('Greens')
    norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)
    im = f3ax1.pcolormesh(time, cohort_size_bins, (DDBH_UNDERSTORY_SCLS / NPLANT_UNDERSTORY_SCLS)[:,:,0].transpose(), cmap=cmap, norm=norm)
    fig3.colorbar(im, ax=f3ax1)
    f3ax1.set_title(r'Growth rate of understory plants (cm yr$^{-1}$)')
    f3ax1.set_xlabel('Time (yr)')
    f3ax1.set_ylabel('Cohort Size (cm)')

    ## set up the third plot: mortality rate in the canopy, in units of fraction of trees per year of a given size class and canopy position
    levels = np.arange(0.,0.1, 0.01)
    cmap = plt.get_cmap('Reds')
    norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)
    im = f3ax2.pcolormesh(time, cohort_size_bins, (MORTALITY_CANOPY_SCLS / NPLANT_CANOPY_SCLS)[:,:,0].transpose(), cmap=cmap, norm=norm)
    fig3.colorbar(im, ax=f3ax2)
    f3ax2.set_title(r'Mortality rate of canopy plants (yr$^{-1}$)')
    f3ax2.set_xlabel('Time (yr)')
    f3ax2.set_ylabel('Cohort Size (cm)')

    ## set up the fourth plot: mortality rate in the understory, units as above
    levels = np.arange(0.,1.0, 0.1)
    cmap = plt.get_cmap('Reds')
    norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)
    im = f3ax3.pcolormesh(time, cohort_size_bins, (MORTALITY_UNDERSTORY_SCLS / NPLANT_UNDERSTORY_SCLS)[:,:,0].transpose(), cmap=cmap, norm=norm)
    fig3.colorbar(im, ax=f3ax3)
    f3ax3.set_title(r'Mortality rate of understory plants (yr$^{-1}$)')
    f3ax3.set_xlabel('Time (yr)')
    f3ax3.set_ylabel('Cohort Size (cm)')

    # show the plot
    fig3.tight_layout()
    plt.show()

8. Discussion Time!
^^^^^^^^^^^^^^^^^^^
Take some time out of that daily grind to chat with your neighbor about the output generated.

.. figure:: images/run2_fig1.png
    :scale: 100%
    :alt: Figure 1: patch area, canopy area, and gpp by patch-age over time
    
    Figure 1: Exploring patch age data 

Question: Why are there two time axes? What is the difference between the date on the x axis and the "age" on the y axis?

.. figure:: images/run2_fig2.png
    :scale: 100%
    :alt: Figure 2: basal area, # of plants, # canopy plants, # understory plants for cohort size over time
    
    Figure 2: Exploring cohort size data 

Question: Why is it possible to have newly recruited plants in the canopy?  And why is it possible to have large trees in the understory?

Question: Can you rationalize why the plots for basal area and the number of plants have different patterns? 

.. figure:: images/run2_fig3.png
    :scale: 100%
    :alt: Figure 3: Growth and mortality for canopy and understory plants
    
    Figure 3: Exploring cohort growth and mortality

Question: If you were a plant, would you want to live in the under-story, or the upper-story?  For instance, how does the survival of newly recruited plants compare in understory versus canopy plants?

Question: Look at figure 2 compare it with figure 3.  How is the changing number density in figure 2 reflected in the growth and mortality rates of figure 3?

This completes the Run 2 unit.
