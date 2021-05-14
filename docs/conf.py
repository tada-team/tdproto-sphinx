project = 'Tdproto docs'
locale_dirs = ['locale/']
gettext_uuid = True
extensions = ['sphinxcontrib.httpdomain']

try:
    import sphinx_rtd_theme
    extensions.append("sphinx_rtd_theme")
    html_theme = "sphinx_rtd_theme"
    del sphinx_rtd_theme
except ImportError:
    ...

templates_path = ['templates']
