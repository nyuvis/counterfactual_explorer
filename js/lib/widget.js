var widgets = require('@jupyter-widgets/base');
var _ = require('lodash');

// See widget.py for the kernel counterpart to this file.

var SettingsModel = widgets.DOMWidgetModel.extend({
    defaults: _.extend(widgets.DOMWidgetModel.prototype.defaults(), {
        _model_name : 'SettingsModel',
        _view_name : 'SettingsView',
        _model_module : 'counterfactual_explorer',
        _view_module : 'counterfactual_explorer',
        _model_module_version : '0.1.0',
        _view_module_version : '0.1.0',
        checked : false
    })
});

// Custom View. Renders the widget model.
var SettingsView = widgets.DOMWidgetView.extend({
    // Defines how the widget gets rendered into the DOM
    render: function() {
        this.checkbox = document.createElement('input');
        this.checkbox.type = 'checkbox';

        this.el.appendChild(this.checkbox);

        // JavaScript -> Python update
        this.checkbox.onchange = this.input_changed.bind(this);
    },
    input_changed: function() {
      this.model.set('checked', this.checkbox.checked);
      this.model.save_changes();
    },
});


module.exports = {
    SettingsModel: SettingsModel,
    SettingsView: SettingsView
};
