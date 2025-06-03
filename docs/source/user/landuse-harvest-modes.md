# Land Use and Harvest

FATES provides a namelist option, `fates_harvest_modes`, to allow the user to engage a variety of different harvest modes, which are set by passing one of five string options:

- `'no_harvest'`
- `'event_code'`
- `'landuse_timeseries'`
- `'luhdata_area'`
- `'luhdata_mass'`

## General description

## Harvest mode descriptions

### `'no_harvest'`

This turns off the land use and harvest modes.  This is the default setting.

### `'event_code'`

This mode is uses the FATES parameter file exclusively through the use of the `fates_landuse_logging_event_code` parameter file variable to define the time at which harvesting occurs.

### `'landuse_timeseries'`

This mode makes use of the landuse timeseries harvest data provided by the host land model, which is discussed in more detail in the [HLM documentation](https://escomp.github.io/CTSM/tech_note/Transient_Landcover/CLM50_Tech_Note_Transient_Landcover.html).  While the host land model can provide a default landuse timeseries file based on the compset name option, the file can be directly set as in the namelist with the `flanduse_timeseries` option by providing it with a string formatted path to the file. **Note:** this option will likely be superseded by the `luhdata_` options noted below in the future.

### `'luhdata_area'`

This mode enables the use of a minimally processed [Land Use Harmonization (LUH)](https://luh.umd.edu/) dataset.  The file must be set via the `fluh_timeseries` namelist option.  

This option uses the area-based harvest data.  Note that this mode automatically engages the FATES landuse x pft static mapping namelist option, `use_fates_lupft` as well as fixed biogeography and no competition options, `use_fates_fixed_biogeog` and `use_fates_nocomp`, respectively.

### `'luhdata_mass'`

This modes uses the same dataset and automtically sets dependent namelist options as noted in the `'luhdata_area'` option noted above.  This option uses the mass-based harvest data.  
