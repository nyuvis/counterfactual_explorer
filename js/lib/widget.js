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
        //checked : false,
        slidervalue: 0
    })
});

// Custom View. Renders the widget model.
var SettingsView = widgets.DOMWidgetView.extend({
    // Defines how the widget gets rendered into the DOM
    render: function() {
        //this.checkbox = document.createElement('input');
        this.slider=document.createElement('input');
        //this.checkbox.type = 'checkbox';
        this.slider.type='range';
        this.slider.min=-5;
        this.slider.max=5;
        //console.log(SettingsModel);
        this.slider.value=0;


      //  this.el.appendChild(this.checkbox);
        this.el.appendChild(this.slider);

        // JavaScript -> Python update
        //this.checkbox.onchange = this.checkbox_changed.bind(this);
        this.slider.onchange = this.slider_changed.bind(this);

    },
    checkbox_changed: function() {
      this.model.set('checked', this.checkbox.checked);
      this.model.save_changes();
    },

    slider_changed: function() {
      console.log("yay");
      this.model.set('slidervalue', +this.slider.value);
      this.model.save_changes();
      //this.touch();
      console.log("slider changed",this.slider.value);
      console.log(this.model.get("slidervalue"))
    },
});


module.exports = {
    SettingsModel: SettingsModel,
    SettingsView: SettingsView
};
