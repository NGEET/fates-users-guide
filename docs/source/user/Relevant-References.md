# Relevant References

To facilitate collaboration and aid in proper attribution of work, please consult this list of references relevant to FATES and its components.  Additions, updates and corrections to this list are welcomed.  Also, please do not consider this list exhaustive and perform due diligence in attribution of work using FATES.

Users should also consult referencing guides from respective host land models (HLM).

---------------------

## Core Reference(s)

Fisher, R. A., Muszala, S., Verteinstein, M., Lawrence, P., Xu, C., McDowell, N. G., Knox, R. G., Koven, C., Holm, J., Rogers, B. M., Spessa, A., Lawrence, D., and Bonan, G.: Taking off the training wheels: the properties of a dynamic vegetation model without climate envelopes, CLM4.5(ED), Geosci. Model Dev., 8, 3593-3619, https://doi.org/10.5194/gmd-8-3593-2015, 2015.

---------------------


## Foundation References


ED Patch and Cohort approach: Moorcroft, P.R., G.C. Hurtt, and S.W. Pacala, 2001. A method for scaling vegetation dynamics: the ecosystem demography model ED. Ecological monographs 71.4, pp. 557-586.

Perfect Plasticity Approximation: Purves, D.W. et al.,  2008. Predicting and understanding forest dynamics using a simple tractable model. Proceedings of the National Academy of Sciences 105.44, pp. 17018-17022.

Calibration and Competition dynamics: Koven, C. D., Knox, R. G., Fisher, R. A., Chambers, J. Q., Christoffersen, B. O., Davies, S. J., Detto, M., Dietze, M. C., Faybishenko, B., Holm, J., Huang, M., Kovenock, M., Kueppers, L. M., Lemieux, G., Massoud, E., McDowell, N. G., Muller-Landau, H. C., Needham, J. F., Norby, R. J., Powell, T., Rogers, A., Serbin, S. P., Shuman, J. K., Swann, A. L. S., Varadharajan, C., Walker, A. P., Wright, S. J., and Xu, C.: Benchmarking and parameter sensitivity of physiological and vegetation dynamics using the Functionally Assembled Terrestrial Ecosystem Simulator (FATES) at Barro Colorado Island, Panama, Biogeosciences, 17, 3017–3044, https://doi.org/10.5194/bg-17-3017-2020, 2020.


---------------------


## Fire

_We recommend reaching out to **Rosie Fisher** and **Adrianna Foster** if planning to investigate fire modeling._

Fire Model (SPITFIRE): Thonicke, K., Spessa, A., Prentice, I. C., Harrison, S. P., Dong, L., and Carmona-Moreno, C.: The influence of vegetation, fire spread and fire behaviour on biomass burning and trace gas emissions: results from a process-based model, Biogeosciences, 7, 1991-2011, https://doi.org/10.5194/bg-7-1991-2010, 2010.


---------------------

## Recruitment

_Please reach out to **Adam Hanbury-Brown** if performing research or publishing with TRS recruitment dynamics_.

Hanbury-Brown, A.R., Powell, T.L., Muller-Landau, H.C., Wright, S.J. and Kueppers, L.M. (2022), Simulating environmentally-sensitive tree recruitment in vegetation demographic models. New Phytologist, 235: 78-93. https://doi.org/10.1111/nph.18059

---------------------

## FATES-Hydro 

_We recommend reaching out to  **Brad Christoffersen**, **Chonggang Xu**, **Yilin Fang** or **Junyan Ding** if interested in research with FATES-Hydro.  Please cite the following (when relevant)_ :

Foundational:

Xu, C., Christoffersen, B., Robbins, Z., Knox, R., Fisher, R. A., Chitra-Tarak, R., Slot, M., Solander, K., Kueppers, L., Koven, C., and McDowell, N.: Quantification of hydraulic trait control on plant hydrodynamics and risk of hydraulic failure within a demographic structured vegetation model in a tropical forest (FATES-HYDRO V1.0), EGUsphere, https://doi.org/10.5194/egusphere-2023-278, 2023.

Christoffersen, B.O., Gloor, M., Fauset, S., Fyllas, N. M., Galbraith, D. R., Baker, T. R., Kruijt, B., Rowland, L., Fisher, R. A., Binks, O. J., Sevanto, S., Xu, C., Jansen, S., Choat, B., Mencuccini, M., McDowell, N. G., Meir, P. Linking hydraulic traits to tropical forest function in a size-structured and trait-driven model (TFS~v.1-Hydro). Geoscientific Model Development, 9(11), 2016, pp: 4227-4255, https://www.geosci-model-dev.net/9/4227/2016/, DOI = 10.5194/gmd-9-4227-2016.

Matrix Solvers:

Fang Y., L. Leung, R. Knox, C.D. Koven, and B. Bond-Lamberty. 2022. "Impact of the numerical solution approach of a plant hydrodynamic model (v0.1) on vegetation dynamics." Geoscientific Model Development 15, no. 16:6385-6398. PNNL-SA-172156. doi:10.5194/gmd-15-6385-2022

Advanced Rooting Depth Controls:

Pre-print (update):  Ding, J., Buotte, P., Bales, R., Christoffersen, B., Fisher, R. A., Goulden, M., Knox, R., Kueppers, L., Shuman, J., Xu, C., and Koven, C. D.: Coordination of rooting, xylem, and stoma strategies explains the response of conifer forest stands to multi-year drought in the Southern Sierra Nevada of California, Biogeosciences Discuss. [preprint], https://doi.org/10.5194/bg-2023-16, in review, 2023.

---------------------

## Nutrient Model

_Please cite the following if using nitrogen or phosphorus limitations with FATES. We recommend reaching out to **Ryan Knox**, **Charles Koven**, **Anthony Walker**, **Rosie Fisher** and **Jennifer Holm** if interested in nutrient limitations with FATES_.

Pre-print (update): Ryan G Knox, Charles D. Koven, William J. Riley, et al. Nutrient Dynamics in a Coupled Terrestrial Biosphere and Land Model (ELM-FATES). ESS Open Archive . March 06, 2023.
DOI: 10.22541/essoar.167810418.80767445/v1

---------------------

## LAI

_If you enable variable SLA with crown depth, activated when parameters fates_leaf_slamax != fates_leaf_slatop, please cite the following reference. We recommend reaching out to **Marlies Kovenock**, **Abigail Swann**, **Charles Koven**, **Rosie Fisher** and **Ryan Knox** if interested in learning more_.

Kovenock, M., Koven, C. D., Knox, R. G., Fisher, R. A., & Swann, A. L. S. (2021). Leaf trait plasticity alters competitive ability and functioning of simulated tropical trees in response to elevated carbon dioxide. Global Biogeochemical Cycles, 35, e2020GB006807. https://doi.org/10.1029/2020GB006807

---------------------

## Allometry

> Used when fates_allom_amode = 1, fates_allom_lmode = 1, and provides parameters (if used):

Saldarriaga, J. G., West, D. C., Tharp, M. L., & Uhl, C. (1988). Long-term chronosequence of forest succession in the upper Rio Negro of Colombia and Venezuela. Journal of Ecology, 76(4), 938-958. DOI: 10.2307/2260625

> Used when fates_allom_amode = 4, fates_allom_hmode = 4, and provides parameters (if used):

Chave, J. , Réjou‐Méchain, M. , Búrquez, A. , Chidumayo, E. , Colgan, M. S., Delitti, W. B., Duque, A. , Eid, T. , Fearnside, P. M., Goodman, R. C., Henry, M. , Martínez‐Yrízar, A. , Mugasha, W. A., Muller‐Landau, H. C., Mencuccini, M. , Nelson, B. W., Ngomanda, A. , Nogueira, E. M., Ortiz‐Malavassi, E. , Pélissier, R. , Ploton, P. , Ryan, C. M., Saldarriaga, J. G. and Vieilledent, G. (2014), Improved allometric models to estimate the aboveground biomass of tropical trees. Glob Change Biol, 20: 3177-3190. doi:10.1111/gcb.12629

> Used when fates_allom_hmode = 3, and provides parameters (if used):

Poorter L, L Bongers and F Bongers.  Architecture of 54 moist-forest tree species: traits, trade-offs, and functional groups.  Ecology 87(5), 2006.

> Used when fates_allom_hmode = 5, and provides parameters (if used):

Martinez Cano, I. and Muller-Landau, H. C. and Wright, S. J. and Bohlman, S. A. and Pacala, S. W. Tropical tree height and crown allometries for the Barro Colorado Nature Monument, Panama: a comparison of alternative hierarchical models incorporating interspecific variation in relation to life history traits, Biogeosciences, 16(4), pp. 847--862, 2019.

---------------------

## Initialization

> The NGEET development team has census initialization files from Barro Colorado Island Panama, users of this data **must** cite:

Hubbell, S.P., Condit, R., and Foster, R.B. 2005. Barro Colorado Forest Census Plot Data. URL http://ctfs.si.edu/webatlas/datasets/bci. 

Condit, R. 1998. Tropical Forest Census Plots. Springer-Verlag and R. G. Landes Company, Berlin, Germany, and Georgetown, Texas. 

Hubbell, S.P., R.B. Foster, S.T. O'Brien, K.E. Harms, R. Condit, B. Wechsler, S.J. Wright, and S. Loo de Lao. 1999. Light gap disturbances, recruitment limitation, and tree diversity in a neotropical forest. Science 283: 554-557. 

Cushman, K. C., Muller‐Landau, H. C., Condit, R. S., Hubbell, S. P. and Freckleton, R. (2014), Improving estimates of biomass change in buttressed trees using tree taper models. Methods Ecol Evol, 5: 573-582. doi:10.1111/2041-210X.12187

---------------------


## Driver Data

> The NGEET development team has meteorological driver data generated for Barro Colorado Island Panama, users of this data **must** cite:

Faybishenko B; Paton S; Powell T; Knox R; Pastorello G; Varadharajan C; Christianson D; Agarwal D (2018): QA/QC-ed BCI meteorological drivers. 1.0. NGEE Tropics Data Collection. (dataset). http://dx.doi.org/10.15486/ngt/1423307
