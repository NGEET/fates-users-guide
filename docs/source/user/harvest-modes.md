# FATES Harvest Modes

FATES provides a namelist option, `fates_harvest_modes`, to allow the user to engage a variety of different harvest modes, which are set by passing one of five string options:

- `no_harvest`: No harvesting (default mode)
- `event_code`: Time based harvest only
- `surfdata_file`: Mass or area-based harvesting driven by HLM landuse timeseries data
- `luhdata_area`: Area-based harvesting driven by the LUH2 timeseries data
- `luhdata_mass`: Mass-based harvesting driven by the LUH2 timeseries data

## General description

## Harvest mode descriptions

### `event_code`

This mode is uses the FATES parameter file exclusively through the use of the `fates_landuse_logging_event_code` to define the time at which harvesting occurs.

### `surfdata_file`

### `luhdata_area`

### `luhdata_mass`
