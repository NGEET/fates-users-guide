# Running Fates with selective logging

== Overview ==

The selective logging module in FATES mimics the ecological, biophysical, and biogeochemical processes following a logging event:  (1) A logging event code to turn on/off and specify the timing of logging; (2) a routine to specify fractions of trees that are damaged by direct felling, collateral damage, and infrastructure damage as additional mortality types that are size-specific; (3) splitting the logged patch into disturbed and intact new patches; (4) applying survivorship to cohorts in disturbed patch;  and (5) transporting logs of harvest trees off-site and adding the remaining biomass from damaged trees into coarse woody debris and litter pools. 

== Guide for Modifying Parameters Relevant to Selective Logging ==

The following parameters can be modified for different logging practices and intensities. Assuming a reduced impact logging event occurred on 01 September 2001 that was designed for minimizing collateral and mechanical damage for infrastructural construction, and only harvested trees larger than 50 cm in DBH, one can modify the parameters as follows:

* Use a the FATES parameter modification python script (ideal of batch processes)

```
$ ./modify_fates_paramfile.py --var fates_logging_dbhmin --fates_scalar 1 --val 50.0 --fin fates_params_2troppftclones.c171018.nc --fout fates_params__2troppftclones.c171018.RILlow.nc
$ ./modify_fates_paramfile.py --var fates_logging_direct_frac fates_scalar 1 --val 0.09 --fin fates_params_2troppftclones.c171018.RILlow.nc --fout fates_params__2troppftclones.c171018.RILlow.nc
$ ./modify_fates_paramfile.py --var fates_logging_collateral_frac fates_scalar 1 --val 0.009 --fin fates_params_2troppftclones.c171018.RILlow.nc --fout fates_params__2troppftclones.c171018.RILlow.nc
$ ./modify_fates_paramfile.py --var fates_logging_coll_under_frac fates_scalar 1 --val 0.65 --fin fates_params_2troppftclones.c171018.RILlow.nc --fout fates_params__2troppftclones.c171018.RILlow.nc
$ ./modify_fates_paramfile.py --var fates_logging_mechanical_frac fates_scalar 1 --val 0.02 --fin fates_params_2troppftclones.c171018.RILlow.nc --fout fates_params__2troppftclones.c171018.RILlow.nc
$ ./modify_fates_paramfile.py --var fates_logging_event_code fates_scalar 1 --val 20010901.0 --fin fates_params_2troppftclones.c171018.RILlow.nc --fout fates_params__2troppftclones.c171018.RILlow.nc
```

=== Namelist Entries ===

One namelist entry is required: a flag that turns on the logging module, the entries can be specified in the main parameter group (clm_inparm) of user_nl_clm.

```
use_fates_logging = .true.

```

