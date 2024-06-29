import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
from collections import Counter
import pandas as pd
from jupyter_dash import JupyterDash
import base64
from io import BytesIO


# Step 1: Load the data
def load_data(file_path):
    with open(file_path, 'r') as file:
        applications = [line.strip().split(',') for line in file]
    return applications


# Step 2: Count occurrences
def count_codes(applications):
    codes = [application[1] for application in applications]
    return Counter(codes)


# Step 3: Get samples by code
def get_samples_by_code(applications):
    samples_by_code = {}
    for application in applications:
        code = application[1]
        if code not in samples_by_code:
            samples_by_code[code] = []
        samples_by_code[code].append(application[0])
    return samples_by_code


# Function to generate Excel data
def generate_excel(samples):
    df = pd.DataFrame(samples, columns=['Application ID'])
    excel_data = BytesIO()
    with pd.ExcelWriter(excel_data, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Applications')
    excel_data.seek(0)
    return excel_data


# File paths
input_file_path = 'data/applications.txt'
average_count_file_path = 'data/annualAverageApplicants.txt'

# Load data
applications = load_data(input_file_path)

# Count codes
code_counts = count_codes(applications)

# Get samples by code
samples_by_code = get_samples_by_code(applications)

# Prepare data for the pie chart
labels, values = zip(*code_counts.items())

# Create the Dash app
app = JupyterDash(__name__)

app.layout = html.Div([
    html.H1("Distribution of Application Codes"),
    html.Div([
        dcc.Graph(id='pie-chart',
                  figure={
                      'data': [
                          go.Pie(labels=labels, values=values, hoverinfo='label+percent', textinfo='label+percent')
                      ],
                      'layout': go.Layout(
                          title='Pie Chart of Application Codes',
                          annotations=[dict(text='Application Codes', x=0.5, y=0.5, font_size=20, showarrow=False)]
                      )
                  })
    ], style={'width': '48%', 'display': 'inline-block'}),
    html.Div([
        html.H2("Application Details"),
        html.Div(
            html.Table(id='details-table'),
            style={'height': '400px', 'overflowY': 'auto', 'border': '1px solid #ddd', 'padding': '10px'}
        ),
        html.A(html.Button("Download Excel"), id='download-excel-btn', download="applications.xlsx", href="",
               target="_blank")
    ], style={'width': '48%', 'display': 'inline-block', 'verticalAlign': 'top'})
])


# Callback to update the details table
@app.callback(
    Output('details-table', 'children'),
    [Input('pie-chart', 'hoverData')]
)
def update_table(hoverData):
    if hoverData is None:
        return []

    label = hoverData['points'][0]['label']
    sample_ids = samples_by_code[label]

    table_header = [
        html.Thead(html.Tr([html.Th("Application ID")]))
    ]

    table_body = [
        html.Tbody([html.Tr([html.Td(app_id)]) for app_id in sample_ids])
    ]

    return table_header + table_body


# Callback to generate and download Excel
@app.callback(
    Output('download-excel-btn', 'href'),
    [Input('pie-chart', 'hoverData')]
)
def download_excel(hoverData):
    if hoverData is None:
        return ""

    label = hoverData['points'][0]['label']
    sample_ids = samples_by_code[label]

    excel_data = generate_excel(sample_ids)
    b64_data = base64.b64encode(excel_data.read()).decode('utf-8')
    href_data = f'data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64_data}'

    return href_data


# Run the app
if __name__ == '__main__':
    app.run_server(mode='inline')
