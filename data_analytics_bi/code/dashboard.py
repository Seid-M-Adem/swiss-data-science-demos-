import pandas as pd
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.io as pio

# Ensure you have the kaleido package installed
# Install it using: pip install -U kaleido

# Load the dataset
df = pd.read_csv('/workspaces/swiss-data-science-demos-/data_analytics_bi/data/customer_transactions.csv')

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
    ]),

    html.Div([
        dcc.Graph(id='transactions-over-time-graph')
    ]),

    html.Div([
        dcc.Graph(id='average-transaction-amount-graph')
    ]),

    html.Div([
        dcc.Graph(id='scatter-transaction-age-graph')
    ])
])

# Define callback to update graphs based on dropdown selection
@app.callback(
    [Output('transaction-amount-graph', 'figure'),
     Output('churn-risk-distribution-graph', 'figure'),
     Output('transactions-over-time-graph', 'figure'),
     Output('average-transaction-amount-graph', 'figure'),
     Output('scatter-transaction-age-graph', 'figure')],
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

    # Create a line graph for transactions over time
    transactions_over_time_fig = px.line(
        df,
        x='transaction_date',  # Ensure this column is properly formatted as datetime
        y='transaction_amount',
        title='Transactions Over Time',
        labels={'transaction_date': 'Date', 'transaction_amount': 'Transaction Amount'}
    )

    # Create a bar chart comparing average transaction amount by churn risk
    avg_transaction_amount_fig = px.bar(
        df.groupby('churn_risk')['transaction_amount'].mean().reset_index(),
        x='churn_risk',
        y='transaction_amount',
        title='Average Transaction Amount by Churn Risk',
        labels={'churn_risk': 'Churn Risk', 'transaction_amount': 'Avg Transaction Amount'}
    )

    # Create a scatter plot for transaction amount vs. customer age
    scatter_transaction_age_fig = px.scatter(
        df,
        x='customer_age',  # Ensure this column exists in your dataset
        y='transaction_amount',
        color='churn_risk',
        title='Transaction Amount vs. Customer Age',
        labels={'customer_age': 'Customer Age', 'transaction_amount': 'Transaction Amount'}
    )
    
    # Export all figures as images and HTML files
    visualizations_dir = '/workspaces/swiss-data-science-demos-/data_analytics_bi/visualizations/'
    
    pio.write_image(transaction_amount_fig, f'{visualizations_dir}transaction_amount_histogram.png')
    pio.write_html(transaction_amount_fig, f'{visualizations_dir}transaction_amount_histogram.html')

    pio.write_image(churn_risk_distribution_fig, f'{visualizations_dir}churn_risk_distribution.png')
    pio.write_html(churn_risk_distribution_fig, f'{visualizations_dir}churn_risk_distribution.html')

    pio.write_image(transactions_over_time_fig, f'{visualizations_dir}transactions_over_time.png')
    pio.write_html(transactions_over_time_fig, f'{visualizations_dir}transactions_over_time.html')

    pio.write_image(avg_transaction_amount_fig, f'{visualizations_dir}average_transaction_amount.png')
    pio.write_html(avg_transaction_amount_fig, f'{visualizations_dir}average_transaction_amount.html')

    pio.write_image(scatter_transaction_age_fig, f'{visualizations_dir}scatter_transaction_age.png')
    pio.write_html(scatter_transaction_age_fig, f'{visualizations_dir}scatter_transaction_age.html')
    
    # Return all figures
    return (transaction_amount_fig, churn_risk_distribution_fig, 
            transactions_over_time_fig, avg_transaction_amount_fig, scatter_transaction_age_fig)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

