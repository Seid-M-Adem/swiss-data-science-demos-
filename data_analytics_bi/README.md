## Data Analytics and Business Intelligence (BI)

### Overview

In this demo, we analyze customer transaction patterns and create interactive dashboards.

### Static Visualization

![Dashboard Overview](visualizations/dashboard_overview.png)

*Figure 1: Distribution of Average Transaction Amount per Customer*

### Interactive Visualization

[Churn Risk Group Distribution](visualizations/dashboard_interactive.html)

*Interactive visualization showing the distribution of churn risk groups.*

# Instructions
Save the Script: Copy the above code into a file named dashboard.py inside the data_analytics_bi/code/ directory of your GitHub repository.
Install Dependencies: Make sure you have the necessary Python packages installed. You can install them using pip:
bash
Copy code
   pip install pandas dash plotly
Run the Script: Execute the script from your terminal or command line:
bash
Copy code
   python data_analytics_bi/code/dashboard.py
View the Dashboard: Open your web browser and go to http://127.0.0.1:8050/ to view the interactive dashboard.
This script leverages Dash and Plotly to create an interactive dashboard that allows users to filter data based on the churn risk and view visualizations accordingly. It’s a powerful tool for exploring and presenting data insights directly from your GitHub Codespace.

# Modified dashboard.py Script
Install Additional Libraries: Ensure you have plotly and dash installed in your environment. You also need selenium and Pillow for saving HTML and PNG files.
bash
Copy code
   pip install dash plotly selenium pillow
Modify the Script: Update dashboard.py to include code that generates and saves the 
