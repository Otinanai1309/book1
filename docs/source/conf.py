import os
import sys
sys.path.insert(0, os.path.abspath('../BOOK1'))


# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Book'
copyright = '2024, Καραμιχαηλίδης Χρήστος'
author = 'Καραμιχαηλίδης Χρήστος'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
  'sphinx.ext.viewcode',
  'sphinx.ext.duration',
  'sphinx.ext.doctest',
  'sphinx.ext.autodoc',
  'sphinx.ext.autosummary',
  'sphinx.ext.napoleon',
  'sphinxcontrib.httpdomain',
  'sphinx_copybutton',
  'sphinx_toolbox.collapse', 
  ]

autosummary_generate = True

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
