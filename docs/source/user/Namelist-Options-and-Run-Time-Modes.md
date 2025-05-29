# Namelist Options

Note: These options are governed by the host-model that drives FATES.  Efforts are made to keep these options consistent in the different driving models (e.g. E3SM/CSTM/etc).

For more information on how to set and use these modes, click on the links in the table where available.


| Option                        | Type              | Default w/FATES compset | Description |
| ------------------------------|:-----------------:| :----------------------:|------------:|
| use_fates                     | true/false        | `.true.`                | Turns on/off fates! (for CTSM this is done by changing the XML variable CLM_BLDNML_OPTS to have "-bgc fates" rather than changing this in the namelist) Compsets with for example `_CLMXX%FATES_` turn this on [XX is for the specific version number) |
| fates_paramfile               | String (filepath) | default file            | path to an alternative netcdf fates parameter file |
| fates_spitfire_mode           | int 0-4           | `0`                     | {doc}`SPITFIRE Namelist Options <SPITFIRE-Namelist-Options>` |
| fates_history_dimlevel | int 0-2 | `2` |  0 = no fates history variables are calculated or allocated, 1 = only time x space (3d) fates history variables allowed, 2 = multiplexed dimensioned fates history is also allowed |
| use_fates_planthydro          | true/false        | `.false.`               | Turns on/off the plant hydrodynamics module |
| use_fates_ed_st3              | true/false        | `.false.`               | Turns on/off Static Stand Structure mode |
| use_fates_ed_prescribed_phys  | true/false        | `.false.`               | Turns on/off Prescribed Physiology mode |
| use_fates_inventory_init      | true/false        | `.false.`               | {doc}`Turns on/off initialization from plant inventory data <Model-Initialization-Modes>` |
| fates_parteh_mode             | integer           | `1`                     | {doc}`Specifies which plant allocation model to use <PARTEH-Modes>` |
| fates_inventory_ctrl_filename | String (filepath) | blank                   | When inventory initialization true, points to control file |
| use_fates_cohort_age_tracking | true/false        | `.false.`               | Turns on/off Cohort age tracking mode |
| use_fates_fixed_biogeog       | true/false        | `.false.`               | Turns on/off {doc}`fixed biogeography mode <Fixed-Biogeography-Mode>` |
| use_fates_nocomp              | true/false        | `.false.`               | Turns on/off no-competition mode |
| use_fates_sp                  | true/false        | `.false.`               | Turns on/off {doc}`satellite phenology mode <SP-(satellite-phenology)-mode>` |
| use_fates_tree_damage         | true/false        | `.false.`               | Turns on/of {doc}`tree crown damage <fates-doc:fates_tech_note>` |
| fates_electron_transport_model | String | `'FvCB1980'`, `'JohnsonBerry2021'`     | Selects the type of electron transport model |
| fates_harvest_mode            | String            | `no_harvest`            | Set FATES harvesting mode. {doc}`Land use Namelist Options <Land-use-Namelist-Options>` |
| fates_seeddisp_cadence        | int 0-3 | `1` | Switch defining the cadence at which seeds are dispersed across gridcells, 0 = no seed dispersal, 1 = daily, 2 = monthly, 3 = yearly. |
| fates_radiation_model         | String            | `norman`                | `'norman'`,  `'twostream'` Sets the FATES radiation model |
| fates_hydro_solver            | String            | `1D_Taylor`             | `'1D_Taylor'`, `'2D_Picard'`,  `'2D_Newton'` Sets the FATES hydro solver method  |
| fates_regeneration_model      | String            | `default`               | `'default'`, `'trs'`, `'trs_no_seed_dyn'` Sets the FATES seed regeneration model |
| fates_cstarvation_model       | String            | `linear`                | `'linear'`, `'exponential'` Sets the FATES carbon starvation model | 
| fates_leafresp_model          | String            | `ryan1991`              | `'ryan1991'`, `'atkin2017'` Sets the FATES leaf maintenance respiration model |
| fates_stomatal_assimilation   | String            | `net`                   | `'net'`, `'gross'` Set net or gross asslimiation for the FATES stomatal model |
| fates_stomatal_model          | Strng             | `ballberry1987`         | `'ballberry1987'`, `'medlyn2011'` Set the FATES stomatal conductance model |
| fates_photosynth_acclimation  | String            | `nonacclimating`        | `'nonacclimating'`, `'kumarathunge2019'` Set the FATES photosynthesis temperature acclimation model |
| use_fates_daylength_factor    | true/false        | `.true.`                | Switch to enable FATES to use the day length factor from the host land model |
| use_fates_luh                 | true/false        | `.false.`               | Turns on/off land use. |
| use_fates_lupft               | true/false        | `.false.`               | If true, enables the use of fates land use x pft mapping data file. |
| use_fates_potentialveg        | true/false        | `.false.`               | If true, assert that all lands are primary and that there is no harvest. |
| fluh_timeseries               | String (filepath) | blank                   | Full pathname of  unified land use harmonization data file. |
| flandusepftdat                | String (filepath) | bland                   | Full pathname of FATES landuse x pft data map. |    



For the nocomp and fixed biogeography, there are logical interactions between them, so what happens is related to the values of both switches.  This logic looks like:

| | use_fixed_biogeog = true | use_fixed_biogeog = false |
| -------------------- |:-----------------:| :------:             |
| **use_fates_nocomp = true** | Every PFT is given its own patch and the patch area for each PFT corresponds to the observed map | Every PFT is given its own patch and every PFT is given the same amount of patch area everywhere |
| **use_fates_nocomp = false** | Competition happens, but only between the PFTs that are allowed on a given gridcell | Competition occurs and governs the distribution of PFTs |

For namelist entries that control the soil properties, or biogeochemical cycling, please refer to the host land-model documentation.  Also, compare the desired namelist entries with the defaults generated by a FATES compset.  Please create issues with questions regarding incompatibilities until more comprehensive documentation becomes available.


***

## How to modify Namelist options

Both E3SM and CTSM (as of Jan 2018) use the file "user_nl_clm" as the means of modifying the namelist entries from the default values generated by different compsets.  In this file, append a line for each option, with syntax "<option_name> = <option_value>".  Each line should be appended to the end of the file, usually just below the comments at the header of the file.

Example:

> use_fates_planthydro = .true.

This user control file will be interpreted when the script "./case.build" is called.  It will then use this information to generate the "lnd_in" file located in the run directory."



