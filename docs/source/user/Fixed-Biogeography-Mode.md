# Fixed Biogeography Mode

## Background

Fixed Biogeography mode is a FATES switch that can be used to turn off prognostic spatial changes in the distribution of vegetation and instead, read in whether particular plant functional types (PFTs) are present a given gridcell. 

## Determining PFT area
Option 1 (DEFAULT). In fixed biogeography mode, seeds of a given PFT are present at initialisation/cold start ONLY if the areal fraction for that PFT is >0 for that gridcell on the surface dataset.  Following this filter, the model runs normally and all other processes are fully prognostic. Seed rain is turned off. 
Option 2. If you want to prescribe the AREA that is occupied by each PFT, and not allow competition to occur between plant types, then fixed biogeography mode can be combined with _use_fates_nocomp_ mode (NO COMPETITION mode). This fixes the areal fraction of each PFT by allocating a single patch for each PFT.   

## User notes
Adding _use_fates_fixed_biogeog=true_. to the user_nl file will activate this mode. 
Check the location of your surface dataset file by looking for 'fsurdat' in the lnd_in file (in the run directory). This can also be changed in user_nl file. 

## Processes turned OFF in fixed biogeography mode
* Seed rain

