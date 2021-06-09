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
   'use_edit_page_button': True,
   'github_url': 'https://github.com/tinkertools',
   'twitter_url': 'https://twitter.com/tinkertoolsmd'
}
html_context = {
   'github_user': 'tinkertools',
   'github_repo': 'tinkerdoc',
   'github_version': 'master'
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

def setup(app):
   app.add_js_file('citation.js') # under the "_static" directory

# -- Options for LaTex output ------------------------------------------------

latex_logo = 'mechanic.png'
latex_elements = {
   'papersize': 'letterpaper', # 'letterpaper' or 'a4paper'
   'pointsize': '10pt',        # '10pt', '11pt' or '12pt'

   'preamble': r'''
\usepackage[notextcomp]{kpfonts}
% \usepackage{fouriernc}
\usepackage[defaultsans]{lato} % sans serif
\usepackage{inconsolata}       % monospace
\usepackage[none]{hyphenat}    % turn off hyphenation
\usepackage{enumitem}
\setlist[description]{style=unboxed} % long description list

\usepackage[normalem]{ulem} % strikethrough text: \sout{text}

% \usepackage{geometry} % already used
\geometry{paperheight=9in,paperwidth=6in,top=1.0in,bottom=1.0in,left=0.5in,right=0.5in,heightrounded}
''',

   'maketitle': r'''
\newcommand\sphinxbackoftitlepage{
\vspace*{\fill}
\begingroup
Copyright © 1990--\the\year{}\\
by Jay William Ponder\\
All Rights Reserved\\
\\
\\
Cover Illustration by Jay Nelson\\
Courtesy of Prof. R. T. Paine, University of New Mexico\\
\\
\\
TINKER IS PROVIDED "AS IS" AND WITHOUT ANY WARRANTY EXPRESS OR IMPLIED. THE USER ASSUMES ALL RISKS OF USING THIS SOFTWARE. THERE IS NO CLAIM OF THE MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE.\\
\\
YOU MAY MAKE COPIES OF TINKER FOR YOUR OWN USE, AND MODIFY THOSE COPIES. YOU MAY NOT DISTRIBUTE ANY ORIGINAL OR MODIFIED SOURCE CODE, EXECUTABLES OR DOCUMENTATION TO USERS AT ANY SITE OTHER THAN YOUR OWN.\\
\\
PLEASE READ, SIGN AND RETURN THE TINKER LICENSE AGREEMENT IF YOU MAKE USE OF THIS SOFTWARE.
\endgroup
\vspace*{\fill}
}
\sphinxmaketitle
''',

   'sphinxsetup': r'''
      TitleColor={rgb}{0,0,0},
      InnerLinkColor={rgb}{0,0,0},
      OuterLinkColor={rgb}{0,0,0},
      VerbatimColor={rgb}{0.9,0.9,0.9},
      VerbatimBorderColor={rgb}{1,1,1}
'''
}


# -- Options for bibliography output -----------------------------------------

extensions.append('sphinxcontrib.bibtex')
bibtex_bibfiles = ['text/refs.bib']
latex_elements['preamble'] = latex_elements['preamble'] + r'''
\addto{\captionsenglish}{\renewcommand{\bibname}{References}}
'''
