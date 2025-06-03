# Land Use and harvest

The land use settings in FATES can be controlled via a namelist setting: 

> fates_harvest_mode

The setting for this variable should be one of the following: 

``` 
 no_harvest   : no fates harvesting of any kind                                                                                                         
 event_code   : fates logging via fates logging event codes only (via fates parameter file)                                                             
 landuse_timeseries: fates harvest driven by HLM landuse timeseries data (dynHarvestMod)                                                                
 luhdata_area : fates harvest driven by LUH2 raw harvest data, area-based (dynFATESLandUseChangeMod)                                                    
 luhdata_mass : fates harvest driven by LUH2 raw harvest data, mass-based (dynFATESLandUseChangeMod)  
```
                                                  
Note that the landuse_timeseries option is not the same as the FATES fluh_timeseries data file.                                                         
This option is older than the luhdata options and may be depricated at some point in the future.  
