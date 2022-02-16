# Satellite Phenology Mode

## Background 
The Satellite Phenology (SP) mode is designed to run with Leaf Area Index (LAI) as an input to the model, as well as canopy height (HTOP) and steam area index (SAI).  In doing so, all processes that in other modes contribute to the calculation of leaf area and plant size are **turned off.**.  

The purpose of this mode is thus to isolate the biophysical processes from the ecological dynaics of FATES, allowing testing of gas exchange processes, surface energy balance and hydrology. FATES-SP is thus analogous to the previously existing SP mode in CLM & ELM.  

## PFT areas
SP mode determines the area of plant functional types (PFTs) based on the areal fractions provided by the surface dataset. The surface dataset is a feature of the host land model and so by defaulr the input areas will be indexed by the PFTs of the host land model.  To map from the Host Land Model PFTs to the FATES PFTs, we use a 2D input variable called '_hlm_pft_map_'.  For each HLM PFT, we must assign, using this matrix, where (all) of its area goes.   It is possible to split the area of a single HLM PFT into multiple FATES PFTs. It is possible to assign >1 HLM PFT to a single FATES PFT, to reduce the complexity of the FATES PFT representation. 

## Implementation 
SP mode follows the following logic to implement the FATES cohort structure. 
1. Read the canopy height  (HTOP) from the surface dataset for each plant functional type. 
2. Determine the DBH (diameter at breast height) consistant with this height and the allmetric equations. 
3. Determine the crown area associated with that DBH (assuming a fixed canopy spread). 
4. Determine the number of trees that will _entirely_ fill the PFT-patch area **ONCE**. 

5. Read the leaf area index from the surface dataset for each PFT. 
6. Invert the _bleaf-> treelai_ function, so that we can find the leaf carbon equivalent to the input TLAU. 
7. Give the single cohort of each PFT the leaf carbon that will result in the input TLAI. 
8. Read the total steam area index (_**TSAI**_) for each PFT. Impose this on the relevant cohort (SAI is not functionally linked (yet) to any particular cohort properties. 
9. The model will generate a prognostic snow depth. This is used to determine the **_exposed_** leaf and stem areas from the total . 

## Processes turned OFF in SP mode. 
* Autotrophic respiration
* Plant allocation and growth
* Recruitment and mortality
* Fire and disturbance
* Litter dynamics
* Patch and cohort fusion and splitting
* Canopy trimming. 


## User notes
Adding **_use_fates_sp=.true._** to the user_nl_clm file will activate SP mode. 

 Note that in SP mode, '_use_fates_nocomp'_ and _use_fates_fixediogeog_' are also true. These will be automatically changed. 

