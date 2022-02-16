# Notes on the Parameter File

NGEET/fates tracks the default fates parameter files in their CDL form via git!

These files can be found here:

https://github.com/NGEET/fates/tree/master/parameter_files

---
### Notes on the file

A short history of the changes to parameter files before they were added to version control is as follows:


Time description format is `c<YYMMDD>.cdl`

There are two ways to get the netcdf version of these files.
* Download or copy/paste these files, and save with the cdl extension. Then run the ncgen command: ncgen -o `<file>.nc` `file.cdl`
* Find the file in the NCAR SVN server and download (requires authentication): https://svn-ccsm-inputdata.cgd.ucar.edu/trunk/inputdata/lnd/clm2/paramdata/

---

### Old versions of the fates parameter files
(Stopped tracking post API 3)


[fates_params_2troppftclones.c171018.cdl (sci.1.4.0_api.3.0.0,current)](content/fates_params_2troppftclones.c171018.cdl) : Wed Oct 18 16:07:18 PDT 2017 Added some default parameters for prescribed physiology, also updated descriptions of allometry options.

[fates_params_2troppftclones.c171010.cdl (sci.1.4.0_api.3.0.0)](content/fates_params_2troppftclones.c171010.cdl) : Tue Oct 10 11:32:10 PDT 2017 (Charlie Koven/Ryan Knox), Added: fates_history_sizeclass_bin_edges, fates_history_ageclass_bin_edges, fates_dbh_repro_threshold,fates_allom_dbh_maxheight,fates_allom_d2ca_coefficient_max,fates_allom_d2ca_coefficient_max,fates_logging_coll_under_frac.  Removed: fates_max_dbh, fates_allom_d2bl_slascaler. Changed values: fates_allom_d2bl1, fates_fdi_a, fates_fdi_b, fates_logging_event_code. Updated metadata: fates_logging_collateral_frac

[fates_params_2troppftclones.c170810.cdl (sci.1.3.0_api.2.0.0) ](content/fates_params_2troppftclones.c170810.cdl)