import os
from data_processing import DataProcessor

class RealEstateCLI:
    def __init__(self):
        self.processor = DataProcessor()

    def run(self):
        while True:
            print("\nWelcome to the Switzerland Real Estate Management Software!")
            print("1. Import Property Listings")
            print("2. Process Data")
            print("3. Export Processed Data")
            print("4. Exit")
            choice = input("Select an option (1-4): ")

            if choice == '1':
                self.import_data()
            elif choice == '2':
                self.process_data()
            elif choice == '3':
                self.export_data()
            elif choice == '4':
                break
            else:
                print("Invalid option. Please try again.")

    def import_data(self):
        file_name = input("Enter the filename of the property listings (e.g., real_estate_listings.csv): ")
        try:
            self.processor.load_data(file_name)
        except Exception as e:
            print(f"Failed to import data: {e}")

    def process_data(self):
        try:
            self.processor.process_data()
        except Exception as e:
            print(f"Failed to process data: {e}")

    def export_data(self):
        default_filename = 'processed_real_estate_listings.csv'
        file_name = input(f"Enter the filename to save processed data (default: {default_filename}): ") or default_filename
        try:
            self.processor.save_data(file_name)
        except Exception as e:
            print(f"Failed to export data: {e}")

if __name__ == "__main__":
    cli = RealEstateCLI()
    cli.run()
