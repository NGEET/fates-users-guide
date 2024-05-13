# FATES Harvest Modes

FATES provides a namelist option, `fates_harvest_modes`, to allow the user to engage a variety of different harvest modes.  The settings for this option should be an integer with a value from 0 to 4.  The options result in the following settings:

0. No harvesting (default mode)
1. Time based harvest only
2. Mass or area-based harvesting driven by CLM landuse timeseries data
3. Area-based harvesting driven by the LUH2 timeseries data
4. Mass-based harvesting driven by the LUH2 timeseries data
