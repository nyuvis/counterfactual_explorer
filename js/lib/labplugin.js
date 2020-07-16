var plugin = require('./index');
var base = require('@jupyter-widgets/base');

module.exports = {
  id: 'counterfactual_explorer',
  requires: [base.IJupyterWidgetRegistry],
  activate: function(app, widgets) {
      widgets.registerWidget({
          name: 'counterfactual_explorer',
          version: plugin.version,
          exports: plugin
      });
  },
  autoStart: true
};

