project = 'Tdproto docs'
locale_dirs = ['locale/']
gettext_uuid = True

try:
    import sphinx_rtd_theme
    global extensions
    extensions = [
        "sphinx_rtd_theme",
    ]
    del sphinx_rtd_theme
except ImportError:
    ...


html_theme = "sphinx_rtd_theme"
