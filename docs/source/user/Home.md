# The Functionally Assembled Terrestrial Ecosystem Simulator (FATES)

[FATES techical documentation](https://fates-docs.readthedocs.io/en/latest/index.html)


This repository houses the development of the Functionally Assembled Terrestrial Ecosystem Simulator (FATES). 
 FATES is a numerical terrestrial ecosystem model.  The funding for this project is supported by Department of Energy’s Next Generation Ecosystem Experiment - Tropics (NGEE-T) project.  The conceptual design is based off of the original Ecosystem Demography model (ED, Moorcroft et al. 2001, Hurtt et al. 2002, Fisher et al. 2015).  This model is designed so that it works as a library that can be called from a selection of driver models including Earth System Models (ESM) such as ACME and CESM.  

Core model code is primarily written using modern Fortran (90+)

Scripting involved in testing, automation and generation of run-time environments may include Perl, Bash, Csh, Python, and perhaps others


***

References:


[Moorcroft et al. 2001. Ecological Monographs, 74:557-586](http://dx.doi.org/10.1890/0012-9615(2001)071[0557:AMFSVD]2.0.CO;2).

[Hurtt et al. 2002. PNAS, 99:1389-1394](http://dx.doi.org/10.1073/pnas.012249999).

[Fisher et al. 2015. GMD, Geosci. Model Dev., 8:3593-3619](https://www.geosci-model-dev.net/8/3593/2015/gmd-8-3593-2015.pdf).

[CLM(ED) tech note](https://drive.google.com/file/d/1waflKlIGKj127hDAiN7b-X0N-HBZdMEE/view?usp=sharing)