# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#

import os
import sys

# -- Path setup --------------------------------------------------------------

# If you have custom modules, uncomment and adjust the path
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'FreeTaxUSA 2025 Help & Filing Guide'
copyright = '2025, FreeTaxUSA'
author = 'FreeTaxUSA Support Team'

# Full version (useful for trust & documentation clarity)
release = '2025.1'

# -- General configuration ---------------------------------------------------

# Sphinx extensions (keep minimal for speed & SEO cleanliness)
extensions = []

# Allow raw HTML in .rst files (for CTA buttons, banners, etc.)
raw_enabled = True

# Templates path
templates_path = ['_templates']

# Files and folders to ignore
exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store'
]

# Source file encoding
source_encoding = 'utf-8'

# -- HTML output options -----------------------------------------------------

# Theme (Read the Docs theme is recommended for help sites)
# Uncomment if installed
# html_theme = 'sphinx_rtd_theme'

# SEO-friendly page titles
html_title = "FreeTaxUSA 2025 – Complete Tax Filing Help & Guide"
html_short_title = "FreeTaxUSA 2025 Guide"

# Favicon (place inside _static or root directory)
html_favicon = 'freetaxusa_favicon.ico'

# Hide "View page source" for cleaner UI
html_show_sourcelink = False

# Allow raw HTML safely (needed for buttons & custom CTAs)
html_allow_unsafe = True

# Disable Sphinx branding
html_theme_options = {
    'show_powered_by': False,
}

# Static files (CSS, JS, images)
# Uncomment if you add custom styles
# html_static_path = ['_static']

# -- SEO & usability enhancements -------------------------------------------

# Language for search engines
language = 'en'

# Prevent duplicated URLs
html_use_index = True
html_copy_source = False

# Better anchor behavior
html_permalinks = True
html_permalinks_icon = '¶'
