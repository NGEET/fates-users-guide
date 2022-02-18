# Testing FATES with answer changing updates

All developers should be aware of and able to use the set of PASS/FAIL and regression tests that are bundled with CIME/E3SM/CESM/FATES.  These tests should be run for any submission of code to the master branch.   However, in the event that a developer changes the code such that answers are changed, and expectedly so... those tests will only tell the developer that their simulations were able to complete (or not) or perform features like restarting correctly.

There is a tool that can help developers evaluate their changes by evaluating model output from a more subjective perspective.  This tool is called the Answer Changing Regression Evaluator (ACRE), see here:

https://github.com/NGEET/acre