# Parameter File

The FATES parameter file is a text file, and uses the JSON format convention.  JSON is similar to XML in that it relies on key and object pairs, and allows nesting of key and object pairs.  Instead of describing the format here, we recommend reading the standard itself: https://www.json.org/json-en.html .

Or, users may find it is somewhat self explanatory by taking a look at it.  A default version of this file is maintained in the FATES version control. This default version has values that are reasonable for testing purposes. For scientifically valid parameters, please consult publications for their parameter sets.

The default can be found here:
https://github.com/NGEET/fates/blob/main/parameter_files/fates_params_default.cdl


---

## Notes on the file

**Prior to 12/2025**, the software team maintained old versions of the netcdf files in the folder: parameter_files/archive.

Following a review of this practice, the team decided to stop updating the archive and move it to parameter_files/deprecated_archive, as using simple git commands such as "diff" is a suitable way of tracking differences in the default parameter file through its history.

**After 12/2025: No more text/binary conversion**: Unlike previous versions of the FATES parameter file, the JSON format is read directly by the FATES model. In the past, the text version of the file (i.e. the "cdl") needed to be converted to a binary format (i.e. the "nc") prior to use. FATES also relied on external code to perform the reading, which resulted in a complicated API and made testing more difficult.

---

## Accessing the parameter file

Users direct the host model to find the FATES parameter file via the namelist. The namelist variable is `fates_paramfile` and accepts a string with the filepath. Two types of paths are acceptable, a path relative to the land-model's source folder or the absolute file path.

`fates_paramfile = "<path to file relative to the land-model root directory>"`

`fates_paramfile = "<absolute path to file>"`


Example using relative paths: The user creates a set of parameters at their site in Barro Colorado Island, they put it in the FATES parameter folder and call it "fates_params_bci.json".

1. For CTSM: `fates_paramfile = "src/fates/parameter_files/fates_params_bci.json"`

2. For E3SM (Post API 43): `fates_paramfile = "src/external_models/fates/parameter_files/fates_params_bci.json"`

---

## Modifying the parameter file

Users may choose to modify the FATES parameter file through different methods, which include:

1. Via a text editor
2. Using python scripting tools provided in https://github.com/NGEET/fates/blob/main/tools/
3. Using their own scripts

It is recommended that users perform "linting" on a modified file to make sure it is compliant. There are utilities that will read in a JSON parameter file and advise the user on what in it's contents is part of the JSON standard.  Simply reading a JSON with the core library is a form of linting, it will fail if it is not compliant:


```
import json
with open(path_to_json_file, 'r') as file:
        data = json.load(file)
```

In the future the "create_case" process may perform a test of the input file to check for compatability.  Alternatively, the user can either run the standard suite of functional unit tests on their parameter file, or run the test found in parameter_files/TestParsing/.


Here is a brief description of the tools that are provided in the FATES repository:

1. [modify_fates_paramfile.py](https://github.com/NGEET/fates/tools/modify_fates_paramfile.py): Command-line style modification of specific parameters, file querying and linting. Examples:

&nbsp;&nbsp;&nbsp;&nbsp;
Example of linting (simply list parameters):
> ./modify_fates_paramfile.py --listparams --fin ../parameter_files/fates_params_default.json


&nbsp;&nbsp;&nbsp;&nbsp;Example of changing Vcmax for the the broadleaf evergreen tropical tree from the default.  Step 1, let's take a look at the parameter in question:

> ./modify_fates_paramfile.py --queryparam --param fates_leaf_vcmax25top --fin ../parameter_files/fates_params_default.json

```
Reporting: Parameter: fates_leaf_vcmax25top:
           dimension names: ['fates_leafage_class', 'fates_pft']
           dimension sizes: [1, 14]
           Current Values:
           [50.0, 62.0, 39.0, 61.0, 58.0, 58.0, 62.0, 54.0, 54.0, 38.0, 54.0, 86.0, 78.0, 78.0]
           Index Pattern:
           [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

```
&nbsp;&nbsp;&nbsp;&nbsp;Step 2. Lets modify the parameters for the first pft, and the 5th pft to 100 and 45. Lets save this into a new file, called fates_params_modified.json
> ./modify_fates_paramfile.py --param fates_leaf_vcmax25top --indices 1,5 --values 100.,45.  --fin ../parameter_files/fates_params_default.json --fout ../parameter_files/fates_params_modified.json

```
Changing fates_leaf_vcmax25top[0,0] from 50.0 to 100.0
Changing fates_leaf_vcmax25top[0,4] from 58.0 to 45.0
Writing to: ../parameter_files/fates_params_modified.json
Writing complete

```

---

2. [batch_patch_params.py](https://github.com/NGEET/fates/tools/batch_patch_params.py): Used with another JSON file that contains any number of changes to apply to a base file.  There is an example of a patch file that filters the PFTs to only use the broadleaf tropical evergreen, and reproduces the parameters that were the basif of Knox et al. 2024. See here: [patch_default_bciopt224.json](https://github.com/NGEET/fates/parameter_files/patch_default_bciopt224.json)

---

3. [cdl_to_xml.py](https://github.com/NGEET/fates/tools/cdl_to_xml.py): Converts a CDL (deprecated) to the new JSON format.

---

4. [pft_index_swapper.py](https://github.com/NGEET/fates/tools/pft_index_swapper.py): Command-line style utility that filters out PFTs.

---

5. [sort_parameters.py](https://github.com/NGEET/fates/tools/sort_parameters.py): Tool used by developers to order parameters and reduce verbosity of "diffs" in version control.
