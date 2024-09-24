import pandas as pd
import random
import os

# Sample data generation function
def generate_real_estate_data(num_records):
    # Locations with average price per square meter (CHF)
    locations = {
        "Zurich": 13000,
        "Geneva": 12000,
        "Bern": 9000,
        "Lausanne": 10000,
        "Basel": 9500,
        "Lucerne": 11000,
        "St. Gallen": 8000,
        "Lugano": 11000,
        "La Chaux-de-Fonds": 7500,
        "Biel": 7000
    }
    
    property_types = ["Apartment", "House", "Villa", "Penthouse"]

    data = {
        "Property ID": [],
        "Location": [],
        "Price (CHF)": [],
        "Size (m²)": [],
        "Bedrooms": [],
        "Bathrooms": [],
        "Property Type": [],
        "Description": []
    }

    for i in range(num_records):
        location = random.choice(list(locations.keys()))
        size = random.randint(30, 300)  # Random size between 30 m² and 300 m²
        price_per_sqm = locations[location]
        price = size * price_per_sqm  # Calculate price based on size and location
        
        data["Property ID"].append(f"PR{i+1:04d}")
        data["Location"].append(location)
        data["Price (CHF)"].append(price)
        data["Size (m²)"].append(size)
        data["Bedrooms"].append(random.randint(1, 6))  # Random bedrooms between 1 and 6
        data["Bathrooms"].append(random.randint(1, 4))  # Random bathrooms between 1 and 4
        data["Property Type"].append(random.choice(property_types))
        data["Description"].append(f"Beautiful {random.choice(property_types)} located in {location} with {random.randint(1, 4)} bathrooms and {random.randint(1, 6)} bedrooms.")

    return pd.DataFrame(data)

# Generate 100 sample records
num_records = 100
real_estate_data = generate_real_estate_data(num_records)

# Save to CSV
output_file = '/workspaces/swiss-data-science-demos-/custom_software_development/data/raw_data/real_estate_listings.csv'  # Adjust the path as necessary
os.makedirs(os.path.dirname(output_file), exist_ok=True)
real_estate_data.to_csv(output_file, index=False)

print(f"Generated {num_records} records and saved to {output_file}")
