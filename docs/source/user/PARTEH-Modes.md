# Parteh Mode

The Plant Allocation and Reactive Transport Extensible Hypotheses (PARTEH) module, like the name implies, handles all things related to growth, allocation and transport.  Here is a link to the
[PARTEH Technical Documentation](https://fates-docs.readthedocs.io/en/latest/fates_tech_note.html#allocation-and-reactive-transport-parteh).

Only 1 alternative is currently active in PARTEH at the moment.

## The carbon-only (non nutrient enabled), allometric growth hypothesis.

This mode is set by default in the namelist.  The namelist entry generated will look like this:

> fates_parteh_mode = 1

List of key parameters in the parameter file (see [default](https://github.com/NGEET/fates/blob/master/parameter_files/fates_params_default.cdl)): 

All allometry coefficients are critical to growth, these parameters are mostly dimensioned by "pft", and should all start with prefix `fates_allom_*`.

All parameters prefixed by `fates_prt_*`, short for Plant Reactive Transport parameters, are salient to PARTEH as well.

`fates_leaf_stor_priority`, which governs the replacement priority between leaves, fine-roots and storage, is dimensioned by `pft`.

`fates_prt_nitr_stoich_p1`, which is the nitrogen content in grams per gram carbon for each plant organ, is dimensioned `plant organ x pft`.

`fates_turnover_carb_retrans`, which is the carbon retranslocation fraction from organs lost during turnover, is dimensioned `plant organ x pft`.

There are several placeholder parameters that are only used in the CNP hypothesis, currently under development:
 > fates_prt_nitr_stoich_p2, fates_prt_phos_stoich_p1, fates_prt_phos_stoich_p2, fates_prt_alloc_priority