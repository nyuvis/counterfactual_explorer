counterfactual_explorer
===============================

A Jupyter Widget for exploring counterfactuals

Installation
------------

To install use pip:

    $ pip install counterfactual_explorer
    $ jupyter nbextension enable --py --sys-prefix counterfactual_explorer

To install for jupyterlab

    $ jupyter labextension install counterfactual_explorer

For a development installation (requires npm),

    $ git clone https://github.com/nyuvis/counterfactual_explorer.git
    $ cd counterfactual_explorer
    $ pip install -e .
    $ jupyter nbextension install --py --symlink --sys-prefix counterfactual_explorer
    $ jupyter nbextension enable --py --sys-prefix counterfactual_explorer
    $ jupyter labextension install js

When actively developing your extension, build Jupyter Lab with the command:

    $ jupyter lab --watch

This takes a minute or so to get started, but then automatically rebuilds JupyterLab when your javascript changes.

Note on first `jupyter lab --watch`, you may need to touch a file to get Jupyter Lab to open.

