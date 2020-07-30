from traitlets import Unicode, Bool, Int
from ipywidgets import DOMWidget

# See js/lib/widget.js for the frontend counterpart to this file.

class Settings(DOMWidget):
    # Name of the widget view class in front-end
    _view_name = Unicode('SettingsView').tag(sync=True)

    # Name of the widget model class in front-end
    _model_name = Unicode('SettingsModel').tag(sync=True)

    # Name of the front-end module containing widget view
    _view_module = Unicode('counterfactual_explorer').tag(sync=True)

    # Name of the front-end module containing widget model
    _model_module = Unicode('counterfactual_explorer').tag(sync=True)

    # Version of the front-end module containing widget view
    _view_module_version = Unicode('^0.1.0').tag(sync=True)
    # Version of the front-end module containing widget model
    _model_module_version = Unicode('^0.1.0').tag(sync=True)

    # Widget specific property.
    # Widget properties are defined as traitlets. Any property tagged with `sync=True`
    # is automatically synced to the frontend *any* time it changes in Python.
    # It is synced back to Python from the frontend *any* time the model is touched.

    checked = Bool(False).tag(sync=True)
    slidervalue=Int(0).tag(sync=True)
