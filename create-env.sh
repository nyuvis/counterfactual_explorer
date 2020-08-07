#!/bin/bash

# create virtual environment
python -m venv counterfactual_explorer

# activate virtual environment
source counterfactual_explorer/bin/activate

# install dependencies
pip install -r requirements.txt

# use virtual environment in jupyter
pip install ipykernel==5.3.2
python -m ipykernel install --user --name=counterfactual_explorer
