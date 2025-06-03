# SPITFIRE

The fire model in FATES (SPITFIRE), can be controlled via a namelist setting:

> fates_spitfire_mode

The setting for this variable should be an integer, with a value from 0 to 4 with the following meanings:

```
 0 : Simulations of fire are off
 1 : use a global constant lightning rate found in fates_params.
 2 : use an external lightning dataset. 
 3 : use an external confirmed ignitions dataset (not available through standard CSEM dataset collection).
 4 : use external lightning and population datasets to simulate both natural and anthropogenic
ignitions.
```

Most users of the FATES model will start by either turning this feature off (if perhaps fire is not a critical ecosystem process in their location of interest), or using the a global constant lightning rate.  The default generated when nothing is specified is:

> fates_spitfire_mode = 0
