# Namelist Option Summary Tables

The namelist options are governed by the Host Land Model (HLM) that drives FATES.  Efforts are made to keep these options consistent in the different driving models (e.g. E3SM/CSTM/etc).

For more information on how to set and use these modes, click on the links in the table where available.

## Basic Usage Options

The following table discusses the basic usage options and settings to enable FATES in the Host Land Model.  Note that compsets with `FATES` in the name, for example `_ELMXX%FATES_`, will set `use_fates` to true to automatically turn on FATES.  Also note that each HLM provides a default fates parameter file that is stored on the public input data servers.  See the page discussing the {doc}`Parameter-File` for more information on modifying the default parameter file that is provided within the FATES source code.

| Option                   | Type    | Default      | Options            | Description |
|:-------------------------|:-------:|:------------:|:-------------------|:------------|
| `use_fates`              | Boolean | `.true.`     | `.true.` `.false.` | Turns on/off fates! |
| `fates_paramfile`        | String  | default file | -                  | path to an alternative netcdf fates parameter file |

## Control of History Complexity

All FATES history output variables are categorized as either a complex variable (having more than time x space dimensions), or a simple variable (just time and space). They are also broken up by being calculated at the dynamics timescale (daily) or at the high-frequency timescale (half-hourly).  Users may wish to either competely deactivate all variables at one of these timescales. Or, perhaps they want just the simple variables. Or, perhaps they want everything, even if it slows the simulation down a little bit. This is controlled by "fates_history_dimlevel", and its slightly different in E3SM compared to CTSM.  In both cases, the high-frequency timescale variables are the first index:

| E3SM Option              | Type    | Default      | Options            | Description |
|:-------------------------|:-------:|:------------:|:-------------------|:------------|
| `fates_history_dimlevel(1)` | Integer | `2`       | `0` `1` `2`     | high-frequency: 0 = no fates history variables are calculated or allocated, 1 = only time x space (3d) fates history variables allowed, 2 = multiplexed dimensioned fates history is also allowed |
| `fates_history_dimlevel(2)` | Integer | `2`       | `0` `1` `2`     | daily frequency: ...


| CTSM Option              | Type    | Default      | Options            | Description |
|:-------------------------|:-------:|:------------:|:-------------------|:------------|
| `fates_history_dimlevel ` | Integer list | `2,2`  | `0` `1` `2`     | high-frequency, daily-frequency: 0 = no fates history variables are calculated or allocated, 1 = only time x space (3d) fates history variables allowed, 2 = multiplexed dimensioned fates history is also allowed |


## Reduced Complexity Modes

The full FATES model has a high degree of complexity.  In order to isolate different processes to allow for cleaner experimental design and facilitate calibration and testing of different model components, FATES includes a number of reduced-complexity configurations. A summary of these configurations is shown in table FATES reduced complexity modes table below:


| Option                         | Type    | Default   | Options            | Description                                                                  |
|:-------------------------------|:-------:|:---------:|:-------------------|:-----------------------------------------------------------------------------|
| `use_fates_ed_prescribed_phys` | Boolean | `.false.` | `.true.` `.false.` | Turns on/off Prescribed Physiology mode                                      |
| `use_fates_ed_st3`             | Boolean | `.false.` | `.true.` `.false.` | Turns on/off Static Stand Structure mode                                     |
| `use_fates_fixed_biogeog`      | Boolean | `.false.` | `.true.` `.false.` | Turns on/off {doc}`fixed biogeography mode <Fixed-Biogeography-Mode>`        |
| `use_fates_nocomp`             | Boolean | `.false.` | `.true.` `.false.` | Turns on/off no-competition mode                                             |
| `use_fates_sp`                 | Boolean | `.false.` | `.true.` `.false.` | Turns on/off {doc}`satellite phenology mode <SP-(satellite-phenology)-mode>` |

For the nocomp and fixed biogeography, there are logical interactions between them, so what happens is related to the values of both switches.  This logic looks like:

| | `use_fixed_biogeog = .true.` | `use_fixed_biogeog = .false.` |
| -------------------- |:-----------------:| :------:             |
| `use_fates_nocomp = .true.` | Every PFT is given its own patch and the patch area for each PFT corresponds to the observed map | Every PFT is given its own patch and every PFT is given the same amount of patch area everywhere |
| `use_fates_nocomp = .false.` | Competition happens, but only between the PFTs that are allowed on a given gridcell | Competition occurs and governs the distribution of PFTs |

For namelist entries that control the soil properties, or biogeochemical cycling, please refer to the host land-model documentation.  Also, compare the desired namelist entries with the defaults generated by a FATES compset.  Please create issues with questions regarding incompatibilities until more comprehensive documentation becomes available.

## Model Components

The namelist options for the various model components of FATES are presented in the subsections below.

### Damage and Mortality

| Option                          | Type    | Default    | Options                    | Description                                                      |
|:--------------------------------|:-------:|:----------:|:---------------------------|:-----------------------------------------------------------------|
| `use_fates_cohort_age_tracking` | Boolean | `.false.`  | `.true.` `.false.`         | Turns on/off Cohort age tracking mode                            |
| `use_fates_tree_damage`         | Boolean | `.false.`  | `.true.` `.false.`         | Turns on/of {doc}`tree crown damage <fates-doc:fates_tech_note>` |
| `fates_cstarvation_model`       | String  | `'linear'` | `'linear'` `'exponential'` | Sets the FATES carbon starvation model                           |


### Fire

| Option                | Type    | Default | Options             | Description                                                  |
|:----------------------|:-------:|:-------:|:--------------------|:-------------------------------------------------------------|
| `fates_spitfire_mode` | Integer | `0`     | `0` `1` `2` `3` `4` | {doc}`SPITFIRE Namelist Options <SPITFIRE-Namelist-Options>` |


### Hydraulics

| Option                 | Type    | Default       | Options                                   | Description                                 |
|:-----------------------|:-------:|:-------------:|:------------------------------------------|:--------------------------------------------|
| `use_fates_planthydro` | Boolean | `.false.`     | `.true.` `.false.`                        | Turns on/off the plant hydrodynamics module |
| `fates_hydro_solver`   | String  | `'1D_Taylor'` | `'1D_Taylor'` `'2D_Picard'` `'2D_Newton'` | Sets the FATES hydro solver method          |

### Inventory

| Option                          | Type    | Default   | Options            | Description                                                                               |
|:--------------------------------|:-------:|:---------:|:-------------------|:------------------------------------------------------------------------------------------|
| `fates_inventory_ctrl_filename` | String  | empty     | -                  | When inventory initialization true, points to control file                                |
| `use_fates_inventory_init`      | Boolean | `.false.` | `.true.` `.false.` | {doc}`Turns on/off initialization from plant inventory data <Model-Initialization-Modes>` |

### Land Use and Harvest


| Option                   | Type    | Default   | Options            | Description                                                              |
|:-------------------------|:-------:|:---------:|:-------------------|:-------------------------------------------------------------------------|
| `use_fates_luh`          | Boolean | `.false.` | `.true.` `.false.` | Turns on/off land use.                                                   |
| `use_fates_lupft`        | Boolean | `.false.` | `.true.` `.false.` | If true, enables the use of fates land use x pft mapping data file.      |
| `use_fates_potentialveg` | Boolean | `.false.` | `.true.` `.false.` | If true, assert that all lands are primary and that there is no harvest. |
| `fluh_timeseries`        | String  | empty     | -                  | Full pathname of unified land use harmonization data file.               |
| `flandusepftdat`         | String  | empty     | -                  | Full pathname of FATES landuse x pft data map.                           |
| `fates_harvest_mode`     | String  | `'no_harvest'` | `'no_harvest'` `'event_code'` `'landuse_timeseries'` `'luhdata_area'` `'luhdata_mass'`| See {doc}`Land use namelist options <landuse-harvest-modes>` |

### Nutrients

| Option              | Type    | Default | Options | Description                                                         |
|:--------------------|:-------:|:-------:|:--------|:--------------------------------------------------------------------|
| `fates_parteh_mode` | Integer | `1`     | `1` `2` | {doc}`Specifies which plant allocation model to use <PARTEH-Modes>` |

### Photosynthesis

| Option                           | Type    | Default            | Options                                 | Description                                                                  |
|:---------------------------------|:-------:|:------------------:|:----------------------------------------|:-----------------------------------------------------------------------------|
| `use_fates_daylength_factor`     | Boolean | `.true.`           | `.true.` `.false.`                      | Switch to enable FATES to use the day length factor from the host land model |
| `fates_electron_transport_model` | String  | `'FvCB1980'`       | `.true.` `.false.`                      | Selects the type of electron transport model                                 |
| `fates_photosynth_acclimation`   | String  | `'nonacclimating'` | `'nonacclimating'` `'kumarathunge2019'` | Set the FATES photosynthesis temperature acclimation model                   |
| `fates_stomatal_assimilation`    | String  | `'net'`            | `'net'` `'gross'`                       | Set net or gross asslimiation for the FATES stomatal model                   |
| `fates_stomatal_model`           | String  | `'ballberry1987'`  | `'ballberry1987'` `'medlyn2011'`        | Set the FATES stomatal conductance model                                     |
| `fates_radiation_model`          | String  | `'norman'`         | `'norman'`  `'twostream'`               | Sets the FATES radiation model                                               |

### Respiration

| Option                 | Type   | Default      | Options                    | Description                                       |
|:-----------------------|:------:|:------------:|:---------------------------|:--------------------------------------------------|
| `fates_leafresp_model` | String | `'ryan1991'` | `'ryan1991'` `'atkin2017'` | Sets the FATES leaf maintenance respiration model |

### Seeds

| Option                     | Type    | Default w/FATES compset | Options                                 | Description                            |
|:---------------------------|:-------:|:-----------------------:|:----------------------------------------|:---------------------------------------|
| `fates_regeneration_model` | String  | `'default'`             | `'default'` `'trs'` `'trs_no_seed_dyn'` | Sets the FATES seed regeneration model |
| `fates_seeddisp_cadence`   | Integer | `1`                     | `0` `1` `2` `3`                         | Switch defining the cadence at which seeds are dispersed across gridcells, 0 = no seed dispersal, 1 = daily, 2 = monthly, 3 = yearly. |

***

## How to modify namelist options

Both E3SM and CTSM (as of Jan 2018) use the file "user_nl_clm" as the means of modifying the namelist entries from the default values generated by different compsets.  In this file, append a line for each option, with syntax "<option_name> = <option_value>".  Each line should be appended to the end of the file, usually just below the comments at the header of the file.

Example:

```
> use_fates_planthydro = .true.
```

This user control file will be interpreted when the script "./case.build" is called.  It will then use this information to generate the "lnd_in" file located in the run directory."



