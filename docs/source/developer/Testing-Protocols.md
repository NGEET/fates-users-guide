# Testing Protocols

## Testing Protocols for Developers and Scientists

*To be discussed:*

- Testing through `newcase`
- Funtional unit tests

## Functional Unit Tests

Functional unit tests help research programmers evaluate validity of scientific code they are developing.  A unit test is intended to be well-bounded so as to only test the correctness of the code being developed.  As such, the extent of the code is typically much smaller in size, and includes as few dependencies as possible.  Ideally the unit test will directory validate the outputs of the code (i.e. not test indirectly through other variables as emmergent phenomenon).

### Unit Test Components

- FATES wrapped code: Fortran module files that wrap the source FATES code to be called by the python driver.  
- Python driver: The python driver makes use of the `ctypes` [library](https://docs.python.org/3.8/library/ctypes.html) to enable calling of C compatible data types.
- Build script: The script is used to manipulate the fortran wrapped code to convert to ctypes and compile for use by the python driver.

### Example description

*This is a placeholder*

## Testing protocol for FATES integrators

FATES integrators, i.e. members of the FATES dev team with administrative privledges and responsible for review and integration of pull request to the ngeet FATES github repo, must run the `fates` regression tests suite provided through CIME's testing functionality prior to integrating a pull request into the main branch.  These tests provide reproducible evidence that the code is working as expected.  See [below](#CIME-test-suites) for more information.  Developers and scientists are not expected to run these tests, but may if so inclined.  These tests must take place on an HPC assets that the FATES dev team has access to and on which a FATES supported host land model is maintained.  This list currently consists of the following:

- [Cheyenne](https://www2.cisl.ucar.edu/resources/computational-systems/cheyenne)
  - NCAR asset.  CESM and other models (e.g. CTSM) officially maintained.
- [Cori](https://docs.nersc.gov/systems/cori/)
  - DOE asset.  E3SM officially maintained.
- [Lawrencium](https://sites.google.com/a/lbl.gov/high-performance-computing-services-group/lbnl-supercluster/lawrencium)  
  - LBL asset.  E3SM and CTSM maintained by FATES dev team. 

### CIME test suites

[CIME documentation](http://esmci.github.io/cime/versions/master/html/users_guide/testing.html)


***The following is out-of-date and under rework - GML***

### Running Tests
Running the test suite:
```SH
    cd cime/scripts
    ./create_test --xml-category fates \
        --machine ${MACHINE} --compiler ${COMPILER} \
        --xml-machine ed --xml-compiler ed \
        --compare ${BASELINE_ED} \
        --test-root ${TEST-ROOT} \
        --test-id ${TEST-ID}e

    ./create_test --xml-category clm_short_45 \
        --machine ${MACHINE} --compiler ${COMPILER} \
        --xml-machine yellowstone --xml-compiler intel \
        --compare ${BASELINE_CLM} \
        --test-root ${TEST-ROOT} \
        --test-id ${TEST-ID}4

    ./create_test --xml-category clm_short_50 \
        --machine ${MACHINE} --compiler ${COMPILER} \
        --xml-machine yellowstone --xml-compiler intel \
        --compare ${BASELINE_CLM} \
        --test-root ${TEST-ROOT} \
        --test-id ${TEST-ID}5
```
where `${ALLCAPSWORD}` should be replaced with the appropriate values for the machine and user. These can either be set on the command line or in a script using 'set', e.g.

set TEST-ROOT=testrootexample
* MACHINE is the computer on which you are working (cheyenne, yellowstone, lawrencium etc.) 
* COMPILER is, well, the compiler you want to use.  gnu, intel, nag or pgi.

* TEST-ROOT is the path to a directory where all of the test cases will be created. (user defined) 

* TEST-ID is a specific name for this set of tests (user defined - there is no wrong answer. example: MMDDfire or 0515fire). But **NOTE**:
  * If you are putting all the tests into the same test root directory, then the testid's must be unique to ensure proper results. The simplest way to do this is add an 'e', '4', or '5' the the end of the id, indicating ed, clm45, or clm50.
  * The test suite occasionally has file name length problems. To avoid these issues, keep the testid to about 10-12 characters.

* BASELINE_X is a path to a set of baseline simulations which are defined for each answer-changing commit to the main repository master. Numerous tests determine whether the code modifications have changed the answers relative to the most-recent baseline. ED and CLM will generally have different baselines. See *Determining your baseline below*.

**NOTE**: the clm_short_N test suites are not setup the same way as the ed test suite. You *must* specify `xml_mach=yellowstone` and `xml_mach=intel` regardless of what machine and compiler you are using.

### Test Results
from tests output directory ${TEST_ROOT}:
```SH
 /${PATH_TO_GIT_FATES-clm}/git/fates-clm/parse_cime.cs.status -s cs.status*
```

## Single tests

The full test suite takes several hours to run and isn't usable for incremental, day to day development where quick, i.e. minutes, turn around is needed. For quick testing, you can run or two single tests that cover the code you are working in or a general case to ensure you aren't breaking things.

```SH
    cd cime/scripts
    ./create_test -testname SMS_D_Ld5.f45_f45.ICLM45ED.${MACHINE}_${COMPILER}.clm-edTest -testid junk-dev -compare ${BASELINE_X}
    cd SMS_D_Ld5.f45_f45.ICLM45ED.${MACHINE}_${COMPILER}.clm-edTest.C.junk-dev
    ./case.test_build
    ./case.submit
    cat TestStatus
    # did everything pass?

```

You can run other tests manually, for example to test the fire code, change the above test name to: `ERS_D_Ld5.f10_f10.ICLM45ED.yellowstone_intel.clm-edFire`.

## Determining your baselines

The version of master your branch is up-to-date with determines your baselines for ed and clm. You need to analyze your branch history to determine which version of master you are based on. To see the history of your clone:

```
git log --graph
```

Look through the history for merge commits. One of the first two commit comment lines will generally contain a description of the merge, something like:
* `Merge branch 'rgknox-CLMLink2' into master` the commit id of this commit is your ed baseline.
* `update ed master to clm4_5_12_r195` the clm trunk is your clm baseline.

NOTE: You do provide good commit messages when you commit code, right? The ability to provide good commit messages is why you should *not* use the '-m' option to commit.

### Machine specific baselines
* On yellowstone:
    * baselines are stored in `/glade/p/cesm/cseg/ccsm_baselines/`
    * ed baselines are in directories following the convention `ed-clm-HASHID` where the hash id corresponds to the master commit in question.
    * clm baselines are stored according to the clm trunk tag naming convention, e.g. `clm4_5_12_r196`. 

## Modifications to the host

The **ed** test suite is the most comprehensive set of tests for ed/fates. The **clm** tests are to ensure that we are not changing the answers of the upstream host model. They must be bit for bit with a baseline generated from the host trunk. If you have changes that need to change the behavior of the host, they must be:

1. submitted independently to the host development team for review

1. included in an `if (use_ed)` block until accepted into the host



### Testing Protocols for SE's

Same as for scientists. While scientists only need to run tests on their production machine with one compiler, SE's should run the test suite with all supported compilers, currently gnu, intel, nag and pgi. The tests should be run on the final commit to master to ensure that there are no semantic conflicts in the final merge. Semantic conflicts are changes in meaning between the master and branch that did not result in a text conflict but change behavior. The final merge to master should be include the detailed commit message that is self contained explaining the changes. The required information includes: the test status, answer changes, user interface changes. The simplest, most efficient, and least error prone way to do this testing is use leverage git.

* Create a small script to process a pull request, `ed-pr.sh`:
```SHELL
#!/usr/bin/env bash

PR_NUM=$1
PR_REPO=$2
PR_BRANCH=$3

REF_REPO=git@github.com:NGEET/ed-clm.git

PR_DIR=pr${PR_NUM}
mkdir -p ${PR_DIR}

cd ${PR_DIR}
git clone ${REF_REPO}

cd ed-clm
git remote add pr ${PR_REPO}
git fetch pr
git checkout ${PR_BRANCH}
git checkout master
git merge --no-ff ${PR_BRANCH}
```

* Initiate the merge:

```SHELL
ed-pr.sh XYZ git@github.com:SOME_USER/ed-clm.git some_branch
# The PR should merge cleanly. Enter a minimal commit message.
```

* Clone the merge repo to hobart:

```SHELL
ssh hobart
git clone ssh://MYNAME@yellowstone.ucar.edu/PATH/TO/SOMEWHERE/prXYZ/ed-clm prXYZ
```

* Kick off testing on hobart using the 'ed' suite and 'nag' compiler. Generate new baselines in the system default location as ed-clm-prXYZ

* Once nag tests have been verified to compile, kick off testing on yellowstone:

  * ed test suite with gnu, intel and pgi compilers. Generate new baselines in the system default location as ed-clm-prXYZ

  * clm_short45 and clm_short50 test suites with gnu, intel, pgi. If changes have been made to the host outside the fates interface, run the full clm test suite, aux_clm45, for gnu, intel, pgi. Compare to baselines generated by the clm SE team. FATES is generally not allowed to change answers for CLM unless the changes have been pre-approved by the CLM scientists.

* Verify that results are as expected:

  * All functionality tests must pass.

  * Are fates baselines expected to be bit for bit? Expect changes limited to a limited subset of fields? All fields?

  * Are all CLM baselines bit for bit?

  * If there are any unexpected results:

    * Update the pull request on git hub with failure information.

    * Delete or rename the merge clone

    * Remove the baselines generated for the PR.

* If all tests are ok, verify there are no source changes in the PR directory. Amend the commit message by copying the info from the pull request message into the message. Add final testing status.

* Push to central repo master.

* Determine the changeset id of the new master. Rename the baselines on yellowstone and hobart: `mv ed-clm-prXYZ ed-clm-CHANGESET_ID`.


