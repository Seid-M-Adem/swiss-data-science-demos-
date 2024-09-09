import pandas as pd
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Load the dataset
df = pd.read_csv('data/customer_transactions.csv')

# Initialize the Dash app
app = Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1("Customer Transactions Dashboard"),
    
    html.Div([
        dcc.Dropdown(
            id='churn-risk-dropdown',
            options=[
                {'label': 'Low', 'value': 'Low'},
                {'label': 'Medium', 'value': 'Medium'},
                {'label': 'High', 'value': 'High'}
            ],
            value='Low'
        )
    ]),
    
    html.Div([
        dcc.Graph(id='transaction-amount-graph')
    ]),
    
    html.Div([
        dcc.Graph(id='churn-risk-distribution-graph')
    ])
])

# Define callback to update graphs based on dropdown selection
@app.callback(
    Output('transaction-amount-graph', 'figure'),
    Output('churn-risk-distribution-graph', 'figure'),
    [Input('churn-risk-dropdown', 'value')]
)
def update_graphs(selected_risk):
    # Filter data based on selected churn risk
    filtered_df = df[df['churn_risk'] == selected_risk]
    
    # Create transaction amount histogram
    transaction_amount_fig = px.histogram(
        filtered_df,
        x='transaction_amount',
        title=f'Distribution of Transaction Amounts (Churn Risk: {selected_risk})',
        labels={'transaction_amount': 'Transaction Amount'}
    )
    
    # Create churn risk distribution pie chart
    churn_risk_distribution_fig = px.pie(
        df,
        names='churn_risk',
        title='Churn Risk Distribution',
        labels={'churn_risk': 'Churn Risk'},
        hole=0.3
    )
    
    return transaction_amount_fig, churn_risk_distribution_fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
