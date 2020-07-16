setup:
	python -m venv env
	source env/bin/activate
	pip install -e .
	deactivate
	source env/bin/activate
	jupyter nbextension install --py --symlink --sys-prefix counterfactual_explorer
	jupyter nbextension enable --py --sys-prefix counterfactual_explorer

active:
	source env/bin/activate

deactive:
	deactivate
