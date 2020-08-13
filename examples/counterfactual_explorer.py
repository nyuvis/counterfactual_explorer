import dice_ml
from dice_ml.utils import helpers

import tensorflow as tf
from tensorflow import keras

import ipywidgets as widgets
from IPython.display import display
from ipywidgets import Checkbox, VBox, HBox, Label, interact, Box, FloatSlider, interact_manual, Layout


import pandas as pd
from sklearn.preprocessing import LabelEncoder
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def explore(dataname, modelname,cont_feat,outcome_name):
    columns=dataname.columns
    feature_names=[]
    for i in columns:
        if i!=outcome_name:
            feature_names.append(i)
    explore.cont_feat=cont_feat
    explore.outcome_name=outcome_name

    #LABELS:
    labels=[]
    for i in feature_names:
        labels.append(widgets.Label(i))
    justlabels=VBox(children=labels)

    #FEATURES TO USE
    displayselectchildren=[Label('1. Select Features to Use')]
    feature_children=[]
    for i in feature_names:
        new_check1=Checkbox(description=i, value=True, indent=False,layout=dict(max_width='200px'))
        feature_children.append(new_check1)
        displayselectchildren.append(new_check1)

    feature_vb = VBox(children = feature_children)
    displayselect=VBox(children=displayselectchildren)


    def f(**kwargs):
        use = list(kwargs.values())

        using=[]
        for i in feature_names:
            using.append(i)

        for i in range(len(use)):
            if use[i] is False:
                using.remove(feature_names[i])

        f.useusing=using
        


        #FEATURE WEIGHTS

        b=widgets.Dropdown(options=['Use Default Weights','Choose Your Own Weights'],value='Use Default Weights',
                           description='2. Feature Weights:',style = {'description_width': 'initial'})

        f.weightdropdown=b
        def g(i):
            if i=='Choose Your Own Weights':
                d = dice_ml.Data(dataframe=dataname, continuous_features=cont_feat, outcome_name=outcome_name)
                mads = d.get_mads(normalized=True)

                feature_weights = {}
                for feature in mads:
                    feature_weights[feature] = round(1/mads[feature], 2)

                feat_child=[]
                floattexts=[]
                for i in feature_names:
                    if i in using:
                        if i in cont_feat:
                            new_floattext=widgets.BoundedFloatText(value=feature_weights.get(i),description=i,layout= dict(max_width='500px'),min=0.01)
                            floattexts.append(new_floattext)
                        if i not in cont_feat:
                            new_floattext=widgets.BoundedFloatText(value=1,description=i,layout= dict(max_width='500px'),min=0.01)
                            floattexts.append(new_floattext)
                    elif i not in using:
                        new_floattext=widgets.FloatText(disabled=True,description=i,layout= dict(max_width='500px'))
                        floattexts.append(new_floattext)

                weights=VBox(children=floattexts)
                display(weights)

                def weightvalues(**kwargs):
                    list1=list(kwargs.values())
                    print(list1)
                    f.weightvaluestouse=list1
                args1 = {
                    f'arg{i}': child
                    for i, child in enumerate(floattexts) }

                outtest=widgets.interactive_output(weightvalues, args1)

            elif i=='Use Default Weights':
                print('Using Default Weights!')


        out1 = widgets.interactive_output(g, {'i': b})
        feat=VBox(children=[b,out1])
        display(HBox([displayselect,feat]))

    args = {
        f'arg{i}': child
        for i, child in enumerate(feature_children)}

    out=widgets.interactive_output(f, args)




    #QUERY
    a=widgets.Dropdown(options=['From Dataset', 'Manually Enter'],
                       value='From Dataset',description='3. Query Input:',style = {'description_width': 'initial'})

    def h(b):
        if b=='From Dataset':
            automatic_entry=widgets.IntText(value=1,description='Enter row number of query:',
                                            style = {'description_width': 'initial'},layout= dict(max_width='250px'))
            listautomatic_entry=[automatic_entry]

            display(automatic_entry)

            def queryvalues1(**kwargs):
                list3=list(kwargs.values())
                outcome_index=dataname.columns.get_loc(outcome_name)
                rowdata=[]
                for i in dataname.loc[list3[0] , : ]:
                    rowdata.append(i)
                rowdata.pop(outcome_index)
                explore.queryvaluestouse=rowdata

            args3 = {
                f'arg{i}': child
                for i, child in enumerate(listautomatic_entry) }

            outtest3=widgets.interactive_output(queryvalues1, args3)

        elif b=='Manually Enter':
            inputq=[]

            inputs=[]
            index=-1
            for i in feature_names:
                index+=1
                if i in cont_feat:
                    cont_text=widgets.FloatText(value=0,layout=dict(max_width='250px'))
                    inputs.append(cont_text)

                else:
                    noncont_dropdown=widgets.Dropdown(options=dataname[i].unique(),layout= dict(max_width='250px'))
                    inputs.append(noncont_dropdown)

            justinputs=VBox(children=inputs)
            inputsandlabels=HBox(children=[justlabels,justinputs])

            inputq.append(inputsandlabels)
            query=VBox(children=inputq)
            display(query)

            def queryvalues(**kwargs):
                list2=list(kwargs.values())
                explore.queryvaluestouse=list2

            args2 = {
                f'arg{i}': child
                for i, child in enumerate(inputs) }

            outtest2=widgets.interactive_output(queryvalues, args2)


    out2 = widgets.interactive_output(h, {'b': a})
    query1=VBox(children=[a,out2])

    #DISPLAY FIRST 3
    display(HBox([out,query1]))

    # PROX/DIV WEIGHTS
    tune_proxdiv1 = Checkbox(description='4. Tune proximity/diversity?', indent=False)
    prox = widgets.FloatSlider(description='Proximity Weight', max=10, value=0.5,style = {'description_width': 'initial'})
    #default for prox in DiCE is 0.5
    div = widgets.FloatSlider(description='Diversity Weight', max=10, value=1,style = {'description_width': 'initial'})
    #default for div in DiCE is 1

    vb_proxdiv = VBox([prox, div])

    def show(d):
        if d==True:
            display(vb_proxdiv)
        elif d==False:
            print('')

    outtester = widgets.interactive_output(show, {'d': tune_proxdiv1})
    #tune_proxdiv=VBox([tune_proxdiv1,outtester])

    #NUMBER OF EXPLANATIONS
    num_exp = widgets.IntSlider(description='5. Num of Explanations', min=1, max=5,
                                style = {'description_width': 'initial'}, indent=False)



    #BUTTON
    button = widgets.Button(description="Generate Explanations!",layout=Layout(height='auto', width='auto'))
    button_output = widgets.Output()


    def on_button_clicked(b):
        with button_output:
            print("Generating explanations may take a few minutes...")
            print()

            #SETTING UP
            d = dice_ml.Data(dataframe=dataname, continuous_features=cont_feat, outcome_name=outcome_name)

            backend = 'TF'+tf.__version__[0] # TF2
            m = dice_ml.Model(model=modelname, backend=backend)

            exp = dice_ml.Dice(d, m)

            #Generating CFs
            query_instance = dict(zip(feature_names, explore.queryvaluestouse))

            if f.weightdropdown.value=='Use Default Weights':
                dice_exp = exp.generate_counterfactuals(query_instance,total_CFs=num_exp.value, desired_class="opposite",
                                                        features_to_vary=f.useusing,
                                                        proximity_weight=prox.value, diversity_weight=div.value)
            elif f.weightdropdown.value=='Choose Your Own Weights':
                #putting weights into dict
                weightstouse=dict(zip(f.useusing, f.weightvaluestouse))
                dice_exp = exp.generate_counterfactuals(query_instance, total_CFs=num_exp.value, desired_class="opposite",
                                                        features_to_vary=f.useusing, feature_weights=weightstouse,
                                                        proximity_weight=prox.value, diversity_weight=div.value)

            explore.dice_exp=dice_exp

    button.on_click(on_button_clicked)

    #DISPLAYING LAST 3 WIDGETS
    display(HBox([tune_proxdiv1, num_exp,button]))
    display(outtester)
    display(button_output)







#VISUALIZING OUTPUT


def visualize_as_pcp():
    data_org=explore.dice_exp.org_instance
    data_cf=explore.dice_exp.final_cfs_df_sparse
    outcome_name=explore.outcome_name
    cont_feat=explore.cont_feat
    vertical_stack = pd.concat([data_org, data_cf], axis=0)

    #have output be 0/1
    new_output=[]
    for i in vertical_stack[outcome_name].values:
        new_output.append(round(i))
    vertical_stack[outcome_name]=new_output

    def parallel_coordinates(df1,cont_feat):
        columns=list(df1.columns)
        labelencoder = LabelEncoder()

        df = df1.copy()

        for i in columns:
            if i not in cont_feat:
                df[i]=labelencoder.fit_transform(df[i])

        new_list=[]
        for i in columns:
            if i in cont_feat:
                x=dict(range = [min(df[i].values.tolist()),max(df[i].values.tolist())],
                         label = i, values = df[i].values.tolist())
                new_list.append(x)
            else:
                x=dict(range = [min(df[i].values.tolist()),max(df[i].values.tolist())],
                         tickvals = list(df[i].unique()),
                         label = i, values = df[i].values.tolist(),
                        ticktext = list(df1[i].unique()))
                new_list.append(x)

        fig = go.Figure(
            data=go.Parcoords(
                line=dict(
                    color = df[explore.outcome_name],
                    colorscale = [[0, 'red'], [0.5, 'red'], [0.5, 'blue'], [1, 'blue']],
                    showscale = True,
                    colorbar=dict(
                        lenmode='pixels',
                        len=75,
                        tickmode='array',
                        tickvals=[0.25, 0.75],
                        ticktext=['0', '1']
                    )
                ),
                dimensions = list(new_list)
            )
        )
        

        fig.show()

    parallel_coordinates(vertical_stack,cont_feat)
    



def visualize_as_list(show_changes):
    if show_changes==True:
        explore.dice_exp.visualize_as_list(show_only_changes=True)
    elif show_changes==False:
        explore.dice_exp.visualize_as_list()





def visualize_as_df(show_changes):
    if show_changes==True:
        explore.dice_exp.visualize_as_dataframe(show_only_changes=True)
    elif show_changes==False:
        explore.dice_exp.visualize_as_dataframe()

        
        
        

def visualize_as_radar():
    data_org=explore.dice_exp.org_instance
    data_cf=explore.dice_exp.final_cfs_df_sparse
    outcome_name=explore.outcome_name
    vertical_stack = pd.concat([data_org, data_cf], axis=0)

    #have output be 0/1
    new_output=[]
    for i in vertical_stack[outcome_name].values:
        new_output.append(round(i))
    vertical_stack[outcome_name]=new_output


    labelencoder = LabelEncoder()

    vertical_stack1 = vertical_stack.copy()
    columns=list(vertical_stack1.columns)

    for i in columns:
        if i not in explore.cont_feat:
            vertical_stack1[i]=labelencoder.fit_transform(vertical_stack1[i])

    normalized_vertical_stack1=(vertical_stack1-vertical_stack1.min())/(vertical_stack1.max()-vertical_stack1.min())

    visualize_as_radar.normalized_data=normalized_vertical_stack1
    columns_touse=[]
    for i in columns:
        columns_touse.append(i)
    columns_touse.append(columns[0])
    #print(columns_touse)


    fig = make_subplots(rows=2, cols=3, specs=[[{'type': 'polar'}]*3]*2)
    col=[2,3,1,2,3]
    row=[1,1,2,2,2]

    fig.add_trace(go.Scatterpolar(
          name = "original instance",
          r = list(normalized_vertical_stack1.iloc[0]),
          theta = columns_touse,
        ), 1, 1)

    for i in range(normalized_vertical_stack1.shape[0]-1):
        fig.add_trace(go.Scatterpolar(
          name = "counterfactual",
          r = list(normalized_vertical_stack1.iloc[i+1]),
          theta = columns_touse,
        ), row[i], col[i])

    fig.update_traces(fill='toself')


    fig.show()