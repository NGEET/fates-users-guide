# How to add a new FATES history variable

## TLDR:
To add a new variable you basically have to add four pieces of code to `FatesHistoryInterfaceMod.F90`:
1. Add a variable to serve as an index (like this:  https://github.com/NGEET/fates/blob/7c065e2/main/FatesHistoryInterfaceMod.F90#L335)
2. Associate a pointer to the chunk of memory indexed by the prior variable (like this:  https://github.com/NGEET/fates/blob/7c065e2/main/FatesHistoryInterfaceMod.F90#L1857)
3. Do whatever logic needs to be done to get the information you want into the variable you are adding (like this:  https://github.com/NGEET/fates/blob/7c065e2/main/FatesHistoryInterfaceMod.F90#L2359)
4. Add the variable name and metadata to the list of history variables, and link those to the index variable you've added above (like this: https://github.com/NGEET/fates/blob/7c065e2/main/FatesHistoryInterfaceMod.F90#L4935-L4938)

## Long Answer:

Because FATES variables exist outside the normal host land model (HLM) variable hierarchy, they need to be passed through an interface layer in order to be output to standard HLM history variables. This requires them to be transferred from the linked-list structure that they are natively on to a vector structure that can be used by the history infrastructure.  Furthermore, because the ED-derived structure of cohorts and patches in FATES are ephemeral over the intervals used for history averaging, the history variables need to be tracked in a more persistent structure that can be transferred to the history, and because of the complex structure within FATES, there may be multiple ways of slicing across this structure to look at quantities of interest.

Many of the FATES variables are transferred over to the host model already, but a user may want to add a new one.  This guide is meant to show how to do so. 

1. Determine the time frequency of the history variable you would like to create.  Most FATES variables are either half-hourly (physiological variables such as GPP or transpiration), or daily (structural variables such as biomass, or vegetation-dynamical variables such as growth or mortality rates).

2. Determine the dimensionality of the history variable.  Options include:
    * Site-level (i.e. scalar from the perspective of FATES)
    * Plant Functional Type
    * Patch age bin. Note that the bin spacing can be set at runtime through the `fates_history_ageclass_bin_edges ` variable in the FATES parameter file.
    * Cohort size bin. Also can be set at runtime via the `fates_history_sizeclass_bin_edges` variable in the FATES parameter file.
    * Canopy Layer
    * Leaf Layer
    * CWD size class and Fuel class (which is CWD size class + indices for leaves and grass)
    * Multiplexed dimensions that combine the above in various ways: Patch-Age x PFT, Patch-Age x Cohort-Size, Cohort-Size x PFT, Cohort-Size x Patch-Age x PFT, Canopy x Leaf, Canopy x Leaf x PFT. The way these work is by rolling up two or more dimensions into a single combined dimension, which you can then unroll when you process the history output (see [here](https://github.com/NCAR/ctsm_python_gallery/blob/master/ctsm_py/fates_xarray_funcs.py) for a library with some xarray functions to do so, and [here](https://github.com/NCAR/ctsm_python_gallery/blob/master/notebooks/fates_notebook.ipynb) for a jupyter notebook with some examples). The indices for unrolling these dimensions are output to the history variable as well to aid in interpreting them properly. Some of these can end up making quite large variables in the history file, so only use those if you really need them. 

3. Create an index variable to keep track of the new history variable.  FATES needs an overall index variable to keep track of the information.  Create a new integer variable to do this, in the `FatesHistoryInterfaceMod.F90` file.  By convention, this variable starts with the prefix `ih_`, then a description of what the variable holds, then a suffix that descrtibes the dimensionality of the variable, like `_si` for site-level variables, `_si_scpf` for size-class x PFT variables, etc.  As an example, here is where we identify the variable for keeping track of the number of plants in each size bin:
https://github.com/NGEET/fates/blob/7c065e2/main/FatesHistoryInterfaceMod.F90#L335

4. Associate a local pointer to the region of memory that gets passed through the interface to the history file.  Basically, FATES passes a massive chunk of memory back and forth to the HLM, but for purposes of tractability, you want to give a small piece of that large chunk of memory a local name.  By convention, this local pointer starts with the prefix `hio_`, and then the rest of it is like the index variable you made in step 3.  An example of this, again for keeping track of the number of plants in each size bin, is here:
https://github.com/NGEET/fates/blob/7c065e2/main/FatesHistoryInterfaceMod.F90#L1857 
Basically you want to cut and paste so that your code looks like the above, varying only the variable name and dimensionality suffix.  Note that the index variable from step 3 is on the right had side, and the new pointer variable you are hereby making is on the left hand side of the statement.
Also, this is where you need to keep track of what timestep you output the history variable on.  For daily timestep variables, you add the local pointer in the part of the code where the above is pointing to (procedure `update_history_dyn`).  For half-hourly timestep variables, you need to add the local pointer in a different part of the code (in the `update_history_prod` procedure), near here:
https://github.com/NGEET/fates/blob/7c065e2/main/FatesHistoryInterfaceMod.F90#L3032

5. Pass the information from the FATES variable to the history buffer via the local pointer you made in step 4.  In the same procedure where you added the local memory pointer with the associate statement, now you want to to take the information from the FATES variable that you are tracking, and send it to the pointer. You first want to figure out which variable is holding the information that you want to the history file to keep track of.  Most likely, this FATES variable is on one of the FATES linked-list types (cohort, patch, or site), which are defined in [EDTypesMod](https://github.com/NGEET/fates/blob/7c065e2/main/EDTypesMod.F90).  Depending on which of these types your variable of interest is, you want to pass the information within either the site loop, the patch loop, or the cohort loop of the procedure. As an example of this step, again following the variable tracking the number of plants in each size bin, see here:
https://github.com/NGEET/fates/blob/7c065e2/main/FatesHistoryInterfaceMod.F90#L2359
Note a couple things here.  (1) is that, for many of the structured variables, you'll be working within a patch of cohort loop, and the key thing is to index the history variable correctly so that it corresponds to the right point in the FATES linked-list structure.  There are likely already in place a bunch of variables for indexing: `scls` for indexing by size class, `iscag` for size-class by age-class, `scpf` for size x pft, `ft` for pft; there are also several helper functions in [FatesSizeAgeTypeIndicesMod](https://github.com/NGEET/fates/blob/7c065e2/main/FatesSizeAgeTypeIndicesMod.F90) that keep track of that indexing, which you can call as needed. (2) is that the pointer variables get initialized every timestep so you don't have to zero them before entering the loop.

6. Now pass the attributes of the new variable to the history interface.  You'll need to tell it what dimension it's on, what frequency it's to be updated, whether it's a default variable or not, what it's name, long name, and units are, etc.  An example for the same variable we've been looking at is here:
https://github.com/NGEET/fates/blob/7c065e2/main/FatesHistoryInterfaceMod.F90#L4935-L4938
You set the dimensionality with the vtype argument (`site_r8` = site-level, `site_size_r8` = size-class dimensioned, etc), the update frequency with the upfreq argument (`1` = daily, `2` = half-hourly, etc). Crucially, you put the index variable that you made in step 3 as the index argument (not the pointer variable). Double-check that you've set the dimensionality correctly, because this is something that is not always caught by the compiler if you get it wrong and can lead to buffer overflows.

7. If the variable that you've made is not default-on, then make sure to add it to your namelist via the `hist_fincl1` argument when you launch your run.

That's it! 

## Adding new multiplexed dimensions

Variables to be defined:
- `site_<newdim>`:
- `nlev<newdim>`:
- `lev<newdim>`:
- `fates_lev<newdim>`
- `lev<newdim>_index`:
- `lev<newdim>_index_`:
- `<newdim>_begin` and `<newdim>_end`:
- `fates_...map_lev<newdim>`:
- `fates_hdim_...map_lev<newdim>`:


### New dimension checklist


- [ ] Add new parameter `site_<newdim>` in [clmfates_interfacemod (hlm)](https://github.com/NGEET/fates/wiki/How-to-add-a-new-FATES-history-variable#clmfates_interfacemod-hlm)
- [ ] Set bounds `<newdim>_begin` and `<newdim>_end` index in clmfates_interfacemod (see below)

This checklist is ordered by fates module file and then by procedure.  It starts with FatesHistoryInterfaceMod assuming that the impetus for the new dimension comes from a new history output variable definition.  The checklist contains internal links to other modules to try and note the code's own connection to other modules.  The cross referencing is not thorough, however, and assumes the reader with proceed through the checklist from top to bottom in order.

#### FatesHistoryInterfaceMod:
- [ ] Define the new multiplexed abbreviation `<newdim>` in the [header comments](https://github.com/NGEET/fates/blob/86e8f11cbe9f7b98b30ea70171b5e885a330a84b/main/FatesHistoryInterfaceMod.F90#L127)

- `fates_history_interface_type` definition
    - [ ] [Initialize `lev<newdim>_index_` integer](https://github.com/NGEET/fates/blob/86e8f11cbe9f7b98b30ea70171b5e885a330a84b/main/FatesHistoryInterfaceMod.F90#L671)
    - [ ] [Initialize `lev<newdim>_index` procedure](https://github.com/NGEET/fates/blob/86e8f11cbe9f7b98b30ea70171b5e885a330a84b/main/FatesHistoryInterfaceMod.F90#L713)
    - [ ] [Initialize `set_lev<newdim>_index` procedure](https://github.com/NGEET/fates/blob/86e8f11cbe9f7b98b30ea70171b5e885a330a84b/main/FatesHistoryInterfaceMod.F90#L740)

- `set_lev<newdim>_index_` and `lev<newdim>_index_` procedures
    - [ ] [Create `set_lev<newdim>_index_` procedure](https://github.com/NGEET/fates/blob/86e8f11cbe9f7b98b30ea70171b5e885a330a84b/main/FatesHistoryInterfaceMod.F90#L1464-L1469)
    - [ ] [Create `lev<newdim>_index_` procedure](https://github.com/NGEET/fates/blob/86e8f11cbe9f7b98b30ea70171b5e885a330a84b/main/FatesHistoryInterfaceMod.F90#L1471-L1475)

- `Init` procudure
    - [ ] [Add `use FatesIODimensionsMod, only lev<newdim>`](https://github.com/NGEET/fates/blob/86e8f11cbe9f7b98b30ea70171b5e885a330a84b/main/FatesHistoryInterfaceMod.F90#L766)
        - [ ] Define `lev<newdim>` in [FatesIODimensionsMod](https://github.com/NGEET/fates/wiki/How-to-add-a-new-FATES-history-variable#FatesIODimensionsMod)
    - [ ] [Add call to `set_lev<newdim>_index`](https://github.com/NGEET/fates/blob/86e8f11cbe9f7b98b30ea70171b5e885a330a84b/main/FatesHistoryInterfaceMod.F90#L888-L889)
    - [ ] [Add call to `dim_bounds(dim_count)%Init(lev<newdims>...)`](https://github.com/NGEET/fates/blob/86e8f11cbe9f7b98b30ea70171b5e885a330a84b/main/FatesHistoryInterfaceMod.F90#L890-L891)
        - [ ] Define fates bounds `<newdim>_begin` and `<newdim>_end` in `fates_bounds_type` in [FatesIODimensionsMod](https://github.com/NGEET/fates/wiki/How-to-add-a-new-FATES-history-variable#FatesIODimensionsMod)

- `SetThreadBoundsEach` procedure
    - [ ] [Set `index` using `lev<newdim>_index()` procedure](https://github.com/NGEET/fates/blob/86e8f11cbe9f7b98b30ea70171b5e885a330a84b/main/FatesHistoryInterfaceMod.F90#L1003)
    - [ ] [Add call to `this%dim_bounds(index)%SetThreadBounds` with `<newdim>_begin` and `<newdim>_end`](https://github.com/NGEET/fates/blob/86e8f11cbe9f7b98b30ea70171b5e885a330a84b/main/FatesHistoryInterfaceMod.F90#L1004-L1005)

- `assemble_history_output_types` procedure
    - [ ] [Add `use FatesIOVariableKindMod, only site_<newdim>`](https://github.com/NGEET/fates/blob/86e8f11cbe9f7b98b30ea70171b5e885a330a84b/main/FatesHistoryInterfaceMod.F90#L1023)
        - [ ] Define `site_<newdim>` in [FatesIOVariableKindMod](https://github.com/NGEET/fates/wiki/How-to-add-a-new-FATES-history-variable#FatesIOVariableKindMod)
    - [ ] [Call `this%set_dim_indices(site_<newdim>` procedure using `lev<newdim>_index()` procedure](https://github.com/NGEET/fates/blob/86e8f11cbe9f7b98b30ea70171b5e885a330a84b/main/FatesHistoryInterfaceMod.F90#L1103-L1104)

- `flush_hvars` procedure
    - [ ] Add `site_<newdim>` to [FatesHistoryVariableType](https://github.com/NGEET/fates/wiki/How-to-add-a-new-FATES-history-variable#FatesHistoryVariableType) for call to `his%hvars(ivar)%flush` call

- `set_history_var` procedure
    - [ ] Add `site_<newdim>` to [FatesHistoryVariableType](https://github.com/NGEET/fates/wiki/How-to-add-a-new-FATES-history-variable#FatesHistoryVariableType) for call to `this%hvars(ivar)%Init` call

- `init_dim_kinds_maps` procedure
    - [ ] [Add `use FatesIOVariableKindMod, only site_<newdim>`](https://github.com/NGEET/fates/blob/86e8f11cbe9f7b98b30ea70171b5e885a330a84b/main/FatesHistoryInterfaceMod.F90#L1572)
    - [ ] [Call `this%dim_kinds(index)%Init(site_<newdim>`](https://github.com/NGEET/fates/blob/86e8f11cbe9f7b98b30ea70171b5e885a330a84b/main/FatesHistoryInterfaceMod.F90#L1680-L1682)

- `define_history_vars` procedure 
    - [ ] [Add `use FatesIOVariableKindMod, only site_<newdim>`](https://github.com/NGEET/fates/blob/86e8f11cbe9f7b98b30ea70171b5e885a330a84b/main/FatesHistoryInterfaceMod.F90#L4162)
    - [ ] [Set `vtype=site_<newdim>` for the new history output variable](https://github.com/NGEET/fates/blob/86e8f11cbe9f7b98b30ea70171b5e885a330a84b/main/FatesHistoryInterfaceMod.F90#L4503)

#### FatesIODimensionsMod:
- [ ] [Define `lev<newdim>` parameter and associated HLM string `fates_lev<newdim>`](https://github.com/NGEET/fates/blob/86e8f11cbe9f7b98b30ea70171b5e885a330a84b/main/FatesIODimensionsMod.F90#L30)
    - [ ] Add `fates_lev<newdim>` parameter in [histFileMod (HLM)](https://github.com/NGEET/fates/wiki/How-to-add-a-new-FATES-history-variable#histFileMod-hlm)
    - [ ] [Add `lev<newdim>` definition in the comment section](https://github.com/NGEET/fates/blob/86e8f11cbe9f7b98b30ea70171b5e885a330a84b/main/FatesIODimensionsMod.F90#L90-L91)

- `fates_bounds_type` definition
    - [ ] [Add bounds `<newdim>_begin` and `<newdim>_end`](https://github.com/NGEET/fates/blob/86e8f11cbe9f7b98b30ea70171b5e885a330a84b/main/FatesIODimensionsMod.F90#L149-L150)

#### histFileMod (HLM):
- `htape_create` procedure
    - [ ] [Call `ncd_defdim(lnfid, 'fates_lev<newdim>`](https://github.com/ESCOMP/CTSM/blob/0392347e51747abf16039b2d4771cc97785be987/src/main/histFileMod.F90#L2095)

- `htape_timeconst` procedure
    - [ ] [Add `use FatesInterfaceTypesMod, only : fates_hdim_...map_lev<newdimi>` map variables as necessary](https://github.com/ESCOMP/CTSM/blob/0392347e51747abf16039b2d4771cc97785be987/src/main/histFileMod.F90#L2540-L2541)
        - [ ] Define `fates_hdim_...map_lev<newdim>` variables in [FatesInterfaceTypesMod](https://github.com/NGEET/fates/wiki/How-to-add-a-new-FATES-history-variable#FatesInterfaceTypesMod)
    - [ ] [Call `ncd_defvar(<newdim>, dim1name='fates_lev<newdim>`](https://github.com/ESCOMP/CTSM/blob/0392347e51747abf16039b2d4771cc97785be987/src/main/histFileMod.F90#L2646-L2649)
    - [ ] [Call `ncd_io(varname='fates_...map_lev<newdim>, data=fates_hdim_...map_lev<newdim>` to set the appropriate mappings as necessary](https://github.com/ESCOMP/CTSM/blob/0392347e51747abf16039b2d4771cc97785be987/src/main/histFileMod.F90#L2644-L2647)

- `hist_addfld2d` procedure
    - [ ] [Create `case ('fates_lev<newdim>')`](https://github.com/ESCOMP/CTSM/blob/0392347e51747abf16039b2d4771cc97785be987/src/main/histFileMod.F90#L4958)
        - [ ] [Define `num2d` using the existing dimensions for this case](https://github.com/ESCOMP/CTSM/blob/0392347e51747abf16039b2d4771cc97785be987/src/main/histFileMod.F90#L4959)

#### FatesIOVariableKindMod:
- [ ] [Add new parameter `site_<newdim>`](https://github.com/NGEET/fates/blob/86e8f11cbe9f7b98b30ea70171b5e885a330a84b/main/FatesIOVariableKindMod.F90#L37)

#### FatesHistoryVariableType:
- [ ] [Add `use FatesIOVariableKindMod, only site_<newdim>`](https://github.com/NGEET/fates/blob/86e8f11cbe9f7b98b30ea70171b5e885a330a84b/main/FatesHistoryVariableType.F90#L17)
- [ ] [Add `case(site_<newdim>)` to `Init` procedure](https://github.com/NGEET/fates/blob/86e8f11cbe9f7b98b30ea70171b5e885a330a84b/main/FatesHistoryVariableType.F90#L204-L206)
- [ ] [Add `case(site_<newdim>)` to `Flush` procedure](https://github.com/NGEET/fates/blob/86e8f11cbe9f7b98b30ea70171b5e885a330a84b/main/FatesHistoryVariableType.F90#L335-L336)

#### FatesInterfaceTypesMod:
- [ ] [Define `fates_hdim_...map_lev<newdim>`](https://github.com/NGEET/fates/blob/86e8f11cbe9f7b98b30ea70171b5e885a330a84b/main/FatesInterfaceTypesMod.F90#L245-L246)
    - [ ] Allocate `fates_hdim_...map_lev<newdim>` in [FatesInterfaceMod](https://github.com/NGEET/fates/wiki/How-to-add-a-new-FATES-history-variable#FatesInterfaceMod)

#### FatesInterfaceMod:
- `fates_history_maps` procedure
    - [ ] [Call `allocate ( fates_hdim_...map_lev<newdim> )`](https://github.com/NGEET/fates/blob/86e8f11cbe9f7b98b30ea70171b5e885a330a84b/main/FatesInterfaceMod.F90#L918-L919)
    - [ ] [Set `fates_hdim_...map_lev<newdim>(i)`](https://github.com/NGEET/fates/blob/86e8f11cbe9f7b98b30ea70171b5e885a330a84b/main/FatesInterfaceMod.F90#L1058-L1065)

#### clmfates_interfacemod (HLM):
- `init_history_io` procedure
    - [ ] [Add `use FatesIOVariableKindMod, only site_<newdim>`](https://github.com/ESCOMP/CTSM/blob/0392347e51747abf16039b2d4771cc97785be987/src/utils/clmfates_interfaceMod.F90#L2366)
    - [ ] [Add new parameter `site_<newdim>` to `case` call](https://github.com/ESCOMP/CTSM/blob/0392347e51747abf16039b2d4771cc97785be987/src/utils/clmfates_interfaceMod.F90#L2500-L2505)

- `hlm_bounds_to_fates_bounds` procedure
    - [ ] [Set bounds `<newdim>_begin` and `<newdim>_end` index](https://github.com/ESCOMP/CTSM/blob/0392347e51747abf16039b2d4771cc97785be987/src/utils/clmfates_interfaceMod.F90#L2879-L2880)