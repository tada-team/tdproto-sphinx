from sys import path
from os.path import abspath

path.append(abspath('.'))
project = 'Tdproto docs'
locale_dirs = ['locale/']
gettext_uuid = True
extensions = [
    'sphinxcontrib.httpdomain',
    'sphinx.ext.autosectionlabel',
    'tdproto_ext',
]
html_theme = "sphinx_rtd_theme"

templates_path = ['templates']
html_favicon = './favicon.svg'
html_logo = './logo.svg'
