import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()


# Create a Dash app
app = dash.Dash(__name__)

# TASK 1: Create the layout
app.layout = html.Div(children=[
    # Dashboard Title
    html.H1('SpaceX Launch Records Dashboard', style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
    
    # Dropdown for Launch Sites
    dcc.Dropdown(
        id='site-dropdown',
        options=[
            {'label': 'All Sites', 'value': 'ALL'},
            {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
            {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
            {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
            {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'}
        ],
        value='ALL',
        placeholder="Select a Launch Site here",
        searchable=True,
    ),
    
    # Range Slider for Payload Selection
    dcc.RangeSlider(
        id='payload-slider',
        min=0,
        max=10000,
        step=1000,
        marks={i: f'{i}' for i in range(0, 10001, 1000)},
        value=[0, 10000],
    ),
    
    # Pie Chart for Launch Success Rates
    dcc.Graph(id='success-pie-chart'),

    # Scatter Plot for Payload vs Success
    dcc.Graph(id='success-payload-scatter-chart')
])

# TASK 2: Add callback for the pie chart
@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
)
def get_pie_chart(entered_site):
    filtered_df = spacex_df
    if entered_site == 'ALL':
        fig = px.pie(filtered_df, values='class', 
                     names='Launch Site', 
                     title='Total Success Launches for All Sites')
    else:
        # Filter data for the selected site
        filtered_df = filtered_df[filtered_df['Launch Site'] == entered_site]
        success_fail = filtered_df['class'].value_counts().reset_index()
        success_fail.columns = ['class', 'count']
        fig = px.pie(success_fail, values='count', 
                     names='class', 
                     title=f'Total Success vs Failed Launches for {entered_site}')
    return fig

# TASK 4: Add callback for the scatter plot
@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [Input(component_id='site-dropdown', component_property='value'),
     Input(component_id='payload-slider', component_property='value')]
)
def update_scatter_chart(entered_site, payload_range):
    filtered_df = spacex_df[(spacex_df['Payload Mass (kg)'] >= payload_range[0]) &
                            (spacex_df['Payload Mass (kg)'] <= payload_range[1])]

    if entered_site == 'ALL':
        fig = px.scatter(
            filtered_df,
            x='Payload Mass (kg)',
            y='class',
            color='Booster Version Category',
            title='Correlation between Payload and Success for all Sites',
            hover_data=['Launch Site']
        )
    else:
        # Filter the DataFrame by the selected launch site
        filtered_df = filtered_df[filtered_df['Launch Site'] == entered_site]
        fig = px.scatter(
            filtered_df,
            x='Payload Mass (kg)',
            y='class',
            color='Booster Version Category',
            title=f'Correlation between Payload and Success for site {entered_site}',
            hover_data=['Launch Site']
        )
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
