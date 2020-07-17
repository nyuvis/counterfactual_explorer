#!/bin/bash

python -m venv env
source env/bin/activate
pip install -e .

source env/bin/activate
jupyter nbextension install --py --symlink --sys-prefix counterfactual_explorer
jupyter nbextension enable --py --sys-prefix counterfactual_explorer
