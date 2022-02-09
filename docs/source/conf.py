# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'FATES Users Guide'
copyright = '2022, Lawrence Berkeley National Laboratory'
author = 'FATES Development Team'

release = '0.0'
version = '0.0.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinxfortran.fortran_domain',
    'sphinxfortran.fortran_autodoc',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

## -- Options for Sphinx-Fortran ---------------------------------------------
# List of possible extensions in the case of a directory listing
fortran_ext = ['f90', 'F90', 'f95', 'F95']

# This variable must be set with file pattern, like "*.f90", or a list of them. 
# It is also possible to specify a directory name; in this case, all files than 
# have an extension matching those define by the config variable `fortran_ext` 
# are used.
# fortran_src = [ os.path.abspath('../src/'),  ]

# Indentation string or length (default 4). If it is an integer, 
# indicates the number of spaces.
fortran_indent = 4
