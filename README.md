# Counterfactual Explorer

## Overview

The Counterfactual Explorer produces and visualizes counterfactual explanations for a given dataset, model, and query_instance. The interface relies on three main libraries: DiCE, ipywidgets, and Plotly. Diverse Counterfactual Explanations (DiCE) generates counterfactual explanations for any Machine Learning model and provides the main functionality for the Counterfactual Explorer tool. Jupyter widgets (ipywidgets) and Plotly provide the front-end interactive interfaces of collapsible checkboxes, sliders, dropdown menus, input boxes, and graphs.
The interactive selection elements run with interactive_output, which allows features to automatically appear, disappear, and be disabled.
To learn more about this project, visit https://sites.google.com/nyu.edu/counterfactual-explorer/home.

## How to Use

Access and download the Counterfactual Explorer. Within terminal, navigate to the counterfactual_explorer folder. To set up the project environment and dependencies for the first time, run  `./create-env.sh.`  After the intial setup, run `source counterfactual_explorer/bin/activate` to activate the envionment and deactivate to deactivate it.

Within the counterfactual_explorer folder and virtual enviroment, create a jupyter notebook. After loading the dataset and defining the machine learning model, run `import counterfactual_explorer` as cfe.

The Counterfactual Explorer has five functions, described in more details below: 
1. **cfe.explore(dataname, modelname,cont_feat,outcome_name)**
2. **cfe.visualize_as_list(show_changes)**
3. **cfe.visualize_as_df(show_changes)**
4. **cfe.visualize_as_pcp()**
5. **cfe.visualize_as_radar()**

## Description

### Explore

The first function produces the counterfactual explanations and takes as an input the dataset name (dataname), model name (modelname), list of continuous features (cont_feat), and the name of the output column (outcome_name). It produces an interactive interface which allows the user to input their preferences for the explanations. Each aspect of this function is described in more detail below.

#### 1. Features to Use

The first input portion of the interface asks the user to choose which features to vary in the explanations. It automatically creates a new checkbox for every input feature, meaning that this section will change size depending on the dataset. Since counterfactual models change inputs to produce new outputs, a user may choose leave unvaried some features that cannot physically be changed (such as gender or race). If they choose to do so, they can uncheck the box related to that feature. 

#### 2. Feature Weights

Some feature weights may be more physically difficult to change than others depending on the dataset. For example, it is easier to change the number of hours worked per week than it is to change one's occupation or level of education. In solving for explanations, DiCE automatically calculates default weights for each feature based on feature variance, using Median Absolute Deviation (MAD).  DiCE also allows the user to input their own custom weights for features.
In the Counterfactual Explorer interface, a user may choose from a dropdown menu to either use the default weight values or input their own. If they choose to input their own, a float text area appears for each of the features. For continuous features, the default text box value is the value automatically calculated by MAD. For categorical features, the default input is 1 as they are automatically one-hot encoded through the DiCE data setup and have little variance. In the example of age in the Adult Dataset, the default weight of 7.3 conveys that age is about 7 times as difficult to change as a categorical feature, but about 3 times easier than changing the hours per week (24.5). These comparative weights can be changed in the interface.
Note: If the user deselected features in step 1 (Features to Use), the text boxes correlating to the deselected inputs are disabled as DiCE will not take that input into account when generating instances.

#### 3. Query

In this portion of the display, the user is asked to input a query instance (the original instance to be explained). There are two ways to input a query: by selecting an instance from the dataset or by manually inputting values for each feature. If the user chooses from the dataset, they input the row number of the query. If they manually enter the query, continuous inputs appear as text boxes and categorical inputs appear as dropdown menus with all the possible options in the dataset. 
Note: even if the user unchecked a feature to use in the first section, they are still required to input a value for that feature. Even though the feature will not be changed, it is still used to influence the prediction.

#### 4. Proximity and Diversity Weights

A good counterfactual explanation is similar to the original instance and models the desired outcome. By adjusting the proximity weight, the interface allows the user to search for instances that are closer to their query. Adjusting the diversity weight lets the model search for more varied counterfactual results. The default DiCE values for these weights are 0.5 and 1 respectively, which are the starting values on the sliders.

#### 5. Number of Explanations
This slider sets the number of counterfactual explanations that the model produces. The choices are between 1 and 5, with 1 as the default value.

#### Generating Counterfactuals

Once the user clicks the "Generating Counterfactuals" button, the Counterfactual Explorer extracts the values from the above inputs and converts them into a form that DiCE can accept. After a few minutes, the Explorer will output the message: "Counterfactuals Found!" along with the time taken to generate the explanations. To display these outputs, use the functions described below.

### Visualizations

#### Visualizing as a List and a Dataframe

The Counterfactual Explorer has two ways to visualize and compare the explanations to the initial input as raw data: **cfe.visualize_as_list(show_changes)** and **cfe.visualize_as_df(show_changes)**. Both accept a boolean (True/False) as the show_changes input. If it is set to True, the list or dataframe will display a dash ( - ) where the explanation feature value is the same as the original instance's value for that feature.

To display only original instance:
1. As Dataframe: `cfe.explore.dice_exp.org_instance`
2. As List: `cfe.explore.dice_exp.org_instance.values.tolist()[0]`

To display only explanations:
1. As Dataframe: `cfe.explore.dice_exp.final_cfs_df_sparse`
2. As List: `cfe.explore.dice_exp.final_cfs_df.values.tolist()`

#### Visualizing as a Graphs

The **cfe.visualize_as_pcp()** function allows the user to visualize the results of the Counterfactual Explorer as a parallel coordinates plot. It visualizes the original instance and explanations in contrasting colors on the same plot to help the user understand the changes in input that caused the new output. This model is powered by Plotly Python Parallel Coordinates Plot, which allows for interactive filtering of data. The user can drag lines across the axes to highlight certain data points and move around the order of the axes to see different relationships. 
 
The **cfe.visualize_as_radar()** function allows the user to visualize the results of the Counterfactual Explorer as a radar/spider/polar plot. It visualizes the original instance and explanations as multiple polar charts with the axes as the different inputs. It is equivalent to the parallel coordinates plot in terms of the data, but here the features are displayed as rays of the circle rather than vertical axes. This model is powered by Plotly Categorical Polar Charts, which also allows for interactive filtering of data. The user can hover over specific data points, zoom into the chart, and spin each graph to display each visualization differently. 
Note: Categorical Polar Charts do not support multiple labels for axes, so the input data is label encoded and normalized (so that each value is between 0 and 1). To understand each of the data points, load either visualize_as_list, visualize_as_df, or the normalized data with `cfe.visualize_as_radar.normalized_data`.





