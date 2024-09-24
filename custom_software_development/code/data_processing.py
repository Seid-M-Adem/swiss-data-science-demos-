import pandas as pd
import os

class DataProcessor:
    def __init__(self):
        self.data = None
        self.raw_data_dir = '/workspaces/swiss-data-science-demos-/custom_software_development/data/raw_data'
        self.processed_data_dir = '/workspaces/swiss-data-science-demos-/custom_software_development/data/processed_data'
        
        # Ensure the processed data directory exists
        os.makedirs(self.processed_data_dir, exist_ok=True)

    def load_data(self, file_name):
        file_path = os.path.join(self.raw_data_dir, file_name)
        if os.path.exists(file_path):
            self.data = pd.read_csv(file_path)
            print(f"Data loaded successfully from {file_path}.")
        else:
            raise FileNotFoundError(f"No such file: {file_path}")

    def process_data(self):
        if self.data is not None:
            # Example processing: drop duplicates
            self.data.drop_duplicates(inplace=True)
            # Add additional processing steps as needed
            print("Data processed successfully.")
        else:
            raise ValueError("No data to process.")

    def save_data(self, file_name):
        if self.data is not None:
            output_path = os.path.join(self.processed_data_dir, file_name)
            self.data.to_csv(output_path, index=False)
            print(f"Processed data exported successfully to: {output_path}")
        else:
            raise ValueError("No data to save.")
