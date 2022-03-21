# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'FATES Users Guide'
copyright = '2022, Lawrence Berkeley National Laboratory'
author = 'FATES Development Team'

release = '0.0'
version = '0.0.0'

# -- General configuration

extensions = [
    'myst_parser',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.intersphinx',
    'sphinxfortran.fortran_domain',
    'sphinxfortran.fortran_autodoc',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
    'rtd': ('https://docs.readthedocs.io/en/stable/', None),
    'fates-doc': ('https://fates-users-guide.readthedocs.io/projects/tech-doc/en/stable/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

# html_theme = 'bizstyle'
html_theme = 'sphinx_rtd_theme'

# html sidebar
# html_sidebars = {
#     "**": ["sbt-sidebar-nav.html", "sbt-sidebar-footer.html"]
# }

# These folders are copied to the documentation's HTML output
html_static_path = ['_static']

# These paths are either relative to html_static_path or fully qualified paths (eg. https://...)
html_css_files = [
    'css/theme_override.css',
]

html_logo = 'images/FATES_logo.png'

html_theme_options = {
    'logo_only': True,
}

# -- Options for EPUB output
epub_show_urls = 'footnote'

## -- Options for myst-parser

# Tell myst to auto-generate heading anchors to a specific heading depth: 
# https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#syntax-header-anchors
myst_heading_anchors = 2

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
