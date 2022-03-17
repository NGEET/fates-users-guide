Frequently Asked Questions
--------------------------

What is FATES?
^^^^^^^^^^^^^^
FATES is a module, designed to operate insides a 'host' land surface model, that simulates vegetation physiology, growth, competition, ecosystem assembly and vegetation distribution. FATES is a 'vegetation demographics model' that uses a cohortized representation of plant populations to approximate ecosystem behaviour. 

Where does FATES live? 
^^^^^^^^^^^^^^^^^^^^^^
FATES is currently a component to the Energy Exascale Earth System Model (`E3SM`_), and the Community Terrestrial System Model (`CTSM`_) (which itself is part of both the Community Earth System Model (`CESM`_) and the Norwegian Earth System Model (`NorESM`_). More interfaces are envisaged as time goes on. 

.. _E3SM: https://github.com/E3SM-Project/E3SM
.. _CTSM: https://github.com/escomp/ctsm
.. _CESM: https://github.com/ESCOMP/CESM
.. _NorESM: https://github.com/NorESMhub/NorESM


How is FATES different to the Ecosystem Demography model?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FATES uses the core concept of size and age-structured representation of vegetation as proposed by Moorcroft et al. (2001) and started life as the EDv1.0 code. Almost every aspects of the model has since diverged from that codebase, either moderately or fundamentally. The different parallel developments of the ED concept are described in `Fisher et al. 2018`_.

.. _Fisher et al. 2018: https://www.bnl.gov/isd/documents/95213.pdf

Does FATES work globally?
^^^^^^^^^^^^^^^^^^^^^^^^^
Yes, and, No. FATES can be and is run globally. We are working on a scientifically supportable plant functional type characterisation for 'standard' global runs at present.  

What plant functional types does FATES have?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FATES is designed specifically to do experiments with alternative representations of plant functional types and to investigate the mechanistic causes of plant distribution in space and time (e.g. `Koven et al. 2020`_) Each PFT is specified by a vector of traits in the input file.  You can have as many as your computing architecture will allow... We currently have a _default_ PFT parameterization based off the ELM/CLM configurations but this is to be taken with a pinch of salt.   

.. _Koven et al. 2020: https://www.biogeosciences.net/17/3017/2020/bg-17-3017-2020-discussion.html

I don't have a supercomputer that runs a climate model at my disposal. Can I still use FATES?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Yes, we are actively working on accesible user platforms. e.g. https://github.com/NGEET/docker-fates-tutorial

Does FATES do nutrients, land use, fire, plant hydraulics? 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
We are actively working on `land use`_ and `nutrient cycling`_.  FATES already has the `SPITFIRE`_ model embedded, and a plant `hydrodynamics`_ scheme. 

.. _land use: https://github.com/NGEET/fates/projects/2
.. _nutrient cycling: https://github.com/NGEET/fates/tree/master/parteh
.. _spitfire: https://github.com/NGEET/fates/tree/master/fire
.. _hydrodynamics: https://pearl.plymouth.ac.uk/bitstream/handle/10026.1/12918/christoffersen%20GMD%20typeset_manuscript-version4.pdf?sequence=1&isAllowed=y

Isn't this all really complicated? I don't want to have to think about plant demography whenever I run my favourite land surface model...
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
We have implemented numerous '`reduced complexity modes`_' in FATES and will implement more. Slides on this idea are here: https://docs.google.com/presentation/d/1_z2PIroU0AzLgwHuDf-ast-OrLPpSiSzW-liLvH5vyo/edit.

.. _reduced complexity modes: https://github.com/NGEET/fates/projects/5

I want to develop a process or parameterization in FATES, what should I do? 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1. Either add an issue to the github repo here, to figure out if it's already happening, whether other people have tried, if anyone could offer useful collaboration or resources.
or. 
email the FATES co-leads (Rosie Fisher or Charlie Koven) 
and
check out the :doc:`/developer/developer-guide`.

I want to run the code, how do I learn how to do that? 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
See the :doc:`../running-fates-walkthrough` tutorial.  It includes a basic script for generating a 100 year global model run here: https://drive.google.com/file/d/0B_5e7rc3QoQqc3lXWlp5SkN3ajQ/view

What version of FATES should I be running?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
*Add a cross-reference here to the hlm-fates compatability table*


I ran FATES successfully!  How do I view the multiplexed dimensions?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
*Add a cross-reference here to the tutorial and to page discussing different tools (e.g. Acre, ctsm_python_gallery,etc)*

How can I find out more about how FATES works?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Either in the `technical documentation`_ or in this slide deck from the `2019 FATES tutorial`_. 

.. _technical documentation: https://fates-docs.readthedocs.io/en/latest/index.html
.. _2019 FATES tutorial: https://docs.google.com/presentation/d/1kztSENcOOw54XpjDCebcOLWciC8kqJegkMJGnuQKisI/edit

How do I keep up with everything that is going on in FATES?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Sign up for our `google group mailing list`_, which we primarily use to advertise bi-weekly meetings (Thursday, 11am Pacific/12am Mountain/8pm CEST) and to publicize new releases and features. Also look through the 'issues', 'pull requests', and 'project' tabs on this github site to see what is in the works. 

.. _google group mailing list: https://groups.google.com/forum/#!forum/fates_model

What is in the 'host land model' and what is in FATES? 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Everything pertaining to **vegetation** is housed inside FATES. This includes radiation transfer, gas exchange, growth, allocation, allometry, turnover, mortality, litter/fuels, fire, seed pools and secondary forests. The 'host land model' retains soil hydrology and physics, surface gas exchange, canopy hydrology, snow physics, river routing, urban processes, soil evaporation.


### References

> Fisher, R.A., Koven, C.D., Anderegg, W.R., Christoffersen, B.O., Dietze, M.C., Farrior, C.E., Holm, J.A., Hurtt, G.C., Knox, R.G., Lawrence, P.J. and Lichstein, J.W., 2018. Vegetation demographics in Earth System Models: A review of progress and priorities. Global change biology, 24(1), pp.35-54.

> Koven, C.D., Knox, R.G., Fisher, R.A., Chambers, J.Q., Christoffersen, B.O., Davies, S.J., Detto, M., Dietze, M.C., Faybishenko, B., Holm, J. and Huang, M., 2020. Benchmarking and parameter sensitivity of physiological and vegetation dynamics using the Functionally Assembled Terrestrial Ecosystem Simulator (FATES) at Barro Colorado Island, Panama. Biogeosciences, 17(11), pp.3017-3044.

> Moorcroft, P.R., Hurtt, G.C. and Pacala, S.W., 2001. A method for scaling vegetation dynamics: the ecosystem demography model (ED). Ecological monographs, 71(4), pp.557-586.

