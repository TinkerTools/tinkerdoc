# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

import datetime
project = 'Tinker Manual'
author_html = 'Jay W. Ponder & Zhi Wang'
author_latex = 'Jay W. Ponder \& Zhi Wang'
copyright = '%s, %s' % (datetime.datetime.now().year, author_html)
latex_documents = [('index', 'tinkermanual.tex', project, author_latex, 'manual')]

numfig = True # number the figures

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme'
html_theme_options = {
   'navbar_center': [],
   'github_url': 'https://github.com/tinkertools',
   'twitter_url': 'https://twitter.com/tinkertoolsmd'
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Options for LaTex output ------------------------------------------------

latex_elements = {
   'papersize': 'letterpaper', # 'letterpaper' or 'a4paper'
   'pointsize': '10pt',        # '10pt', '11pt' or '12pt'

   'preamble': r'''
% \usepackage[notextcomp]{kpfonts}
\usepackage{fouriernc}
\usepackage[defaultsans]{lato} % sans serif
\usepackage{inconsolata}       % monospace

% \usepackage{geometry} % already used
\geometry{paperheight=9in,paperwidth=6in,top=1.0in,bottom=1.0in,left=0.5in,right=0.5in,heightrounded}
''',

   'sphinxsetup': r'''
      TitleColor={rgb}{0,0,0},
      InnerLinkColor={rgb}{0,0,0},
      OuterLinkColor={rgb}{0,0,0},
      VerbatimColor={rgb}{0.9,0.9,0.9},
      VerbatimBorderColor={rgb}{1,1,1}
'''
}
