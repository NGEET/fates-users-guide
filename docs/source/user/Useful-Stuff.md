# Useful Things

***

Please Feel Free to List and Link Useful Scripts


***

## Testing Scripts

[Ryan's Fates Developer Test Script on Cheyenne (super old by now)](https://drive.google.com/file/d/1SPNF9HqyA1GJNpC-Ya8HBjMUsBoHSVKm/view?usp=sharing)

[Script for generating 100+ year runs on Cheyenne (f45 and 1x1 brazil) (also super old)](https://drive.google.com/file/d/0B_5e7rc3QoQqc3lXWlp5SkN3ajQ/view?usp=sharing)

## Simulation on User-defined Grid (example: four tropical sites)
1) see Gautam Bisht's method (Matlab) of generating surface and domain datasets [here](https://github.com/bishtgautam/matlab-script-for-clm-sparse-grid)
2) Here are example [surface data](https://drive.google.com/file/d/0B_5e7rc3QoQqY1ZNVU5wWjd3NTA/view?usp=sharing) and [domain data](https://drive.google.com/file/d/0B_5e7rc3QoQqVDd2TEdYOWVDSXc/view?usp=sharing) generated with GB's script
3) Example [script](https://drive.google.com/file/d/0B_5e7rc3QoQqejRiaVRvbnFrak0/view?usp=sharing) to run this user defined grid (for the eddi machine)

## Python Scripts for Evaluation

This python script in the ACRE toolset requires the "basemap" library.  basemap is not the easiest library to intall, but it is useful:

[ACRE Grid Comparison](https://github.com/NGEET/acre/blob/master/acre_gridcomp.py)

[Ryan's Gridded Python Evaluation Tools](https://github.com/rgknox/FatesMapTools)


## Examples of FATES parameter files:
1) Template for using 13 PFTs. You can change the number of PFTs that you would like to use by changing "fates_initd" and "fates_seed_rain". If these values are left as zero, then no PFT will be simulated for that index.
2) DISCLAIMER - the actual parameter fields and values have NOT been tested and validated.
3) Note - strict PPA is "turned on" in this file
4) Note - fates_initd is 0.3 for all fields, so all 13 PFTs will run if you use as is.
5) Note - all the fates_allom parameters are still the default values from the tropical file, and are not PFT specific.
6) Note - there are some "older" parameters that existed prior to FATES (so older CLM parameters). These parameters have been updated with the PFT specific parameters from CLM, and correspond to the first 13 PFTs as found in the CLM parameter file, in the same order. Please contact Jennifer Holm if this doesn't make sense.
7) Netcdf parameter file here [fates_params](https://drive.google.com/file/d/0B3YITWoECxo5eVpldF90ZTNTMW8/view?usp=sharing)

***

## Scripts for Manipulating FATES Parameter Files

Some useful scripts are stored and added to the fates tools/ directory.  

[fates/tools/PFTIndexSwapper.py](https://github.com/NGEET/fates/blob/master/tools/FatesPFTIndexSwapper.py) is a python script that allows a user to cherry pick the pfts (allowing for redundancy) of an existing FATES parameter file and use the selected pfts to populate a new file. It will copy all non-pft dimensioned variables with it. Execute the script with the "--help" flag for usage.

[fates/tools/modify_fates_paramfile.py](https://github.com/NGEET/fates/blob/master/tools/modify_fates_paramfile.py) is a python script that allows a user to change the values of specific variables in the FATES parameter file, and optionally generate a new file, or overwrite the existing file.  See comments at the top of the script for usage.


[fates/tools/BatchPatchParams.py](https://github.com/NGEET/fates/blob/master/tools/BatchPatchParams.py) works together with an xml file to apply a set of modifications to one parameter file thereby generating a new parameter file, treating the xml file as a patch.  The base (old) and new parameter files are specified in the patch (xml) file.  Examples of the xml patch files can be found in the directory [fates/parameter_files](https://github.com/NGEET/fates/tree/master/parameter_files).

***

## Scripts for setting up, compiling, and executing your runs

It's useful to set up a case all at once, following a template script.  Attached a couple examples, which both do the same thing for different build environments (CTSM model on Cheyenne, and E3SM model on Edison). These both set up a run on a regional grid over California, but ought to be useful in setting up a general case.
* get info on the git hashes of both the host model and fates version
* set up a case, and include the git hashes in the case name for purposes of provenance-tracking
* modify a bunch of options
* use scripts to take the default cdl-format parameter file and then generate and modify a netcdf-format parameter file
* set some namelist options
* compile the model
* submit the case to a queue

[CTSM/Cheyenne](files/fates_ctsm_cheyenne_template.csh) 

[E3SM/Edison](files/fates_e3sm_edison_template.csh)

***

## RStudio-based workflow to create drivers, run, and evaluate the model for single site.

Multiple [FATES utilities](https://github.com/mpaiao/FATES_Utils/edit/master/) for running ELM-FATES or CLM-FATES for single sites. These will help creating the input data sets, generating the simulation case, and producing some simple time series from the model output. For additional details on these scripts, check the [documentation here](https://mpaiao.github.io/FATES_Utils/index.html).

1. [**make_fates_met_driver.Rmd**](make_fates_met_driver.Rmd) – This R Markdown script generates a meteorological driver from an ascii file containing the time series of variables relevant to ELM and CLM (with or without FATES).
2. [**make_fates_domain+surface.Rmd**](make_fates_domain+surface.Rmd) – This R Markdown script produces the domain and the surface data files needed to initialise ELM and CLM (with or without FATES).
3. [**create_case_hlm-fates.Rmd**](create_case_hlm-fates.Rmd) - This R Markdown script sets up a single-point simulation using ELM or CLM (with or without FATES) directly from RStudio.  Alternatively, there is a [**shell script**](create_case_hlm-fates.sh) version with most of the same functionality (though variable handling is less efficient) 
4. [**fates_plot_monthly.Rmd**](fates_plot_monthly.Rmd) - This R Markdown script produces time series of multiple variables.  It works best with CLM-FATES, but it can be used for ELM-FATES, ELM, and CLM too.
5. [**make_fates_tower_summary.Rmd**](make_fates_tower_summary.Rmd) - This R Markdown script takes eddy covariance data, convert units to be compatible with ELM and CLM, computes averages by month and year, and creates a netCDF file that can be used for benchmarking the model.
6. [**c6_modis-lai_poi.Rmd**](c6_modis-lai_poi.Rmd). This R Markdown compiles leaf area index data derived from MODIS (Collection 6) downloaded using [A&rho;&rho;EEARS](https://lpdaacsvc.cr.usgs.gov/appeears/)
7. [**fates_tower_compare_monthly.Rmd**](fates_tower_compare_monthly.Rmd) - This R Markdown script loads the tower benchmarking file (see 5) and MODIS LAI (see 6) and plots a series of comparisons with the model predictions.

**Important notes**.

* Rmd files work best in [RStudio](https://www.rstudio.com), but it is possible to run it in the terminal too. For the first time, you may need to install package `rmarkdown`.
```
> install.packages("rmarkdown")
```
then it can be run using the following commands (it will also produce a html file with the notes).
```
> require(rmarkdown)
> rmarkdown::render("fates_tower_compare_monthly.Rmd")
```
* In most cases, you will need to edit the beginning of the scripts, to adjust paths, case names, and a few additional settings.
* Make sure to download the directory [RUtils](RUtils) also available on GitHub, and set variable `util_path` accordingly for scripts that have this variable.
* These scripts are (permanently?) under development.  Contributions, suggestions, and bug fixes are always welcome, just submit an [issue](https://github.com/mpaiao/FATES_Utils/issues) on FATES_Utils.  If you fix a bug or add a new feature, please consider submitting a [pull request](https://github.com/mpaiao/FATES_Utils/pulls) to FATES_Utils.
