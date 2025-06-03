# Model Initialization Modes

== Overview ==

The state of the terrestrial ecosystem in FATES can be initialized in roughly three different ways:

1. A "restart" simulation: During the initialization phase, the model will read in detailed information of the complete "state" of the FATES model, and its host model (ALM/CLM), that was generated during a previous simulation.  A restart simulation should generate bit-for-bit results with the previous simulation in absolutely all aspects, including carbon, water, energy, demography and nutrients.

2. A "cold-start", spin-up type simulation.  The energy, water, nutrient and soil carbon states will be initialized with nominal values.  The vegetation in this case, is initialized by creating a single cohort for each of the represented plant functional types in the fates parameter file, with a an initial number density as specified in the fates parameter file, and a starting size that equals the smallest size of a cohort (the size of a new recruit, defined by h_min).  It is assumed that over a suitably long enough period of time, the relevant quantities of interest in the simulation will have responded and reacted to the model boundary conditions such that no (or limited) memory of the arbitrary initial conditions remain.

3. A "cold-start", with inventory initialization.  This mode is similar to Case 2, in that the soil biogeochemistry, hydrology and energy states are given nominal values.  However, in this case, the user can direct the initialization to read plant demographic data from a set of files.  The canopy structure and composition that is defined in the files is generally limited to the size, type and number of plants that exist, and potentially information on existing litter pools and coarse woody debris.


== Guide for Restarting a FATES Simulation  (Case 1) ==

To start up a new case using the restart file from a prior case as your initial conditions, add a line like this to your user_nl_clm file:

```
finidat=‘full_path_to_restart_file.clm2.r.0000.nc’

```

To extend a case using a restart file from that case, from the case directory run:

```
./xmlchange CONTINUE_RUN=TRUE
./case.submit

```

== Guide for a Cold Start Simulation w/o Inventory (Case 2) ==

CONTENT TBA


== Guide for a Cold Start Simulation with Inventory (Case 3) ==

The key element in an inventory initialization, is specifying what inventory data is available and what format the data is provided in.  While we have the software mechanisms to accommodate various different file formats, only 1 is currently used.

All of the inventory initialization code is contained in this file:[main/FatesInventoryInitMod.F90](https://github.com/NGEET/fates/blob/master/main/FatesInventoryInitMod.F90)


=== Namelist Entries ===

Two namelist entries are required: a flag that turns on inventory initialization, and the full path to a control file, these entries can be specified in the main parameter group (clm_inparm) of user_nl_clm.

```
use_fates_inventory_init = .true.
fates_inventory_ctrl_filename = '<full path to the control file>'

```

=== Control File Specification ===

The control file should be text formatted.  It should contain 1 header row. It should contain any number of rows greater than 1, that each specify inventory site data that the user would like the model to interperate.  This description of the site data should contain: a format specifier for the data at that site, the latitude and longitude in decimal degrees (both 0-360 and -180 to 180 conventions allowed), and then the full path to both the patch file and the cohort file.  More on format specifications in the next sub-section.  Below is an example of the control file.

```
TYPE LATITUDE LONGITUDE PSS_PATH CSS_PATH
1 -7.0 305.0 /home/rgknox/Models/tools_benchmarking_evaluation/forestgeo_2_dembmarks/bci_cens_30Jul83_c13300617.pss  /home/rgknox/Models/tools_benchmarking_evaluation/forestgeo_2_dembmarks/bci_cens_30Jul83_c13300617.css
```

=== Inventory Format Type 1 ===


''Patch'' file format (*.pss)

| Variable  | Units | Description |
|-----------|-------|------------ |
| time      |years  | Year        |
|patch      |String |Patch identifier (arbitrary, any unique string that can be used to match cohorts) |
|trk        |0 – non-forest, 1 – secondary, 2 - primary |Vegetation type/history |
|age        |years  |Patch age since disturbance |
|area |proportion |Fractional area represented by patch.  For format 1 is area in m2 |


''Cohort'' file format (*.css)

| Variable | Unit | Description |
|----------|------|-------------|
| time  | year | year |
| patch | string | Unique identifier (the string matching with the patch its on) |
| dbh |cm |Stem diameter breast height |
| height | m | Plant height |
| pft |integer |Plant Functional Type |
| n |Stem/m2 |Stem density |

*Important: The cohort file with use either the dbh __or__ the height of the plant to specify the size. But, it can't use both! Make sure one of the two is set to zero. Plant biomass will be assessed based off of allometry relative to plant size.

