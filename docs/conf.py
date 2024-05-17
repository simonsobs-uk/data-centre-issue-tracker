# https://www.sphinx-doc.org/en/master/usage/configuration.html
project = "SO:UK Data Centre"
author = "Kolen Cheung"
year = "2023–2024"
copyright = f"{year}, {author}"
del year
release = "0.4.1"
version = ".".join(release.split(".")[:-1])
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.extlinks",
    "sphinx.ext.ifconfig",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinxcontrib.apidoc",
    "myst_parser",
    "sphinx_last_updated_by_git",
]
source_suffix = [".md", ".rst"]
# https://github.com/mgeier/sphinx-last-updated-by-git/issues/40
needs_sphinx = "5.2"
pygments_style = "solarized-light"
html_theme = "furo"
html_last_updated_fmt = "%Y-%m-%dT%H:%M:%S%z"
latex_engine = "lualatex"

# https://myst-parser.readthedocs.io/en/stable/syntax/optional.html
myst_enable_extensions = [
    "dollarmath",
    "amsmath",
    "deflist",
    "fieldlist",
    "html_admonition",
    "html_image",
    "colon_fence",
    "smartquotes",
    "replacements",
    "linkify",
    "strikethrough",
    "substitution",
    "tasklist",
    "attrs_inline",
    "attrs_block",
]

# https://github.com/sphinx-contrib/apidoc
apidoc_module_dir = "../src/souk"
apidoc_separate_modules = True
apidoc_module_first = True

# https://github.com/mgeier/sphinx-last-updated-by-git/
git_last_updated_timezone = "Europe/London"
