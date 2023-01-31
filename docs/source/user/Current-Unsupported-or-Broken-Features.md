# Current Unsupported or Broken Features 

This is a listing of features that users and developers should be wary of when running FATES.

Last updated:  11/3/2020 (RGK)


-----------------------------

## Key:

**Broken** features have been identified as having a critical flaw or bug associated with them.  It is not recommended that anyone use the model in these configurations, unless they are an expert user who is actively mitigating or addressing the relevant problem.


**Unsupported** features may or may not produce scientifically valid and bug-free results.  These features may be currently in active development, or may be untested, or maybe just poorly understood.  It is not recommended that new users, or users unfamiliar with the code itself use these features.


**Experimental** features that may be of importance to FATES team goals, but are still in the midst of development, or do no have a long proven track record.

----------------------------
##  Broken Features:

Snow occlusion of understory plants is not activated.  Regardless of how much snow has fallen, all leaf areas and stem areas are 100% exposed.

Long-term FATES-HYDRO runs with dynamics turned on (non-ST3) contains an important simplification. When FATES-HYDRO is active, all water in dying plants is banked into a storage pool that has no return flux to the ecosystem. 

-----------------------------

## Unsupported Features:


"HYBRID" simulations a la CLM/ELM.  This may very well work, but we just haven't tested it.

Plants with no sapwood or structural biomass, users may want try specifying grasses with very small quantities of each.  

Coupled simulations with atmospheric components.  As of 1/31/23, some people have run these simulations, but very little evaluation has been performed. Further, burn fluxes are not passed to the atmosphere from FATES fire emissions.

-----------------------------

## Experimental Features:

FATES Hydro, generally, is currently undergoing testing, tweaking and refining.

FATES Hydro combined with fire and logging modes has not had significant evaluation either.

FATES with nutrient dynamics (i.e. parteh_mode = 2) is relatively new and has undergone very limited testing, consider experimental.


-------------------------------------

Updated 01/31/2023 (RGK)
