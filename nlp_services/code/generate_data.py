import pandas as pd
import random
from datetime import datetime, timedelta

# Constants
NUM_RECORDS = 3500
sources = ['web', 'mobile', 'email']
sentiment_labels = ['positive', 'negative', 'neutral']

# Sample feedback for each sentiment
positive_feedback = [
    "The service was outstanding!", 
    "Great experience, highly recommend.", 
    "Everything was perfect, will use again.", 
    "Very satisfied with the product quality.",
    "Fast and reliable, well done!"
]

negative_feedback = [
    "Terrible experience, very disappointed.", 
    "The product was defective upon arrival.", 
    "Customer service was rude.", 
    "I wouldn't recommend this to anyone.",
    "Extremely poor quality, not worth the price."
]

neutral_feedback = [
    "It was okay, nothing special.", 
    "Average experience overall.", 
    "Not too bad, but could be better.", 
    "The product works as expected.", 
    "Service was fine, but not impressive."
]

# Generate random feedback text
def generate_feedback(sentiment):
    if sentiment == 'positive':
        return random.choice(positive_feedback)
    elif sentiment == 'negative':
        return random.choice(negative_feedback)
    else:
        return random.choice(neutral_feedback)

# Generate random timestamps
def random_date(start, end):
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds()))
    )

# Start and end dates for timestamp generation
start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 9, 24)

# Generate dataset
data = []

for i in range(1, NUM_RECORDS + 1):
    feedback_id = i
    customer_id = random.randint(1000, 9999)
    sentiment = random.choice(sentiment_labels)
    feedback_text = generate_feedback(sentiment)
    timestamp = random_date(start_date, end_date).strftime('%Y-%m-%d %H:%M:%S')
    source = random.choice(sources)
    
    data.append([feedback_id, customer_id, feedback_text, timestamp, source, sentiment])

# Create a DataFrame
df = pd.DataFrame(data, columns=['feedback_id', 'customer_id', 'feedback_text', 'timestamp', 'source', 'sentiment_label'])

# Save to CSV
df.to_csv('/workspaces/swiss-data-science-demos-/nlp_services/data/reader_feedback.csv', index=False)

print("reader_feedback.csv generated successfully!")
