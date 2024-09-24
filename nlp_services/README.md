# NLP Services - Sentiment Analysis

This project performs sentiment analysis on a dataset of reader feedback. The dataset includes customer feedback from various sources and is used to classify the sentiment into categories (e.g., positive, negative, neutral).

## Project Structure

- `data/`: Contains the dataset for the sentiment analysis (`reader_feedback.csv`).
- `code/`: Python code for performing sentiment analysis using NLP libraries.
- `notebooks/`: Jupyter notebook demonstrating the NLP workflow and results.
- `README.md`: Overview of the project, structure, and dependencies.

## Dataset

The dataset is located in `data/reader_feedback.csv`. It contains the following columns:
- `feedback_id`: Unique ID for the feedback.
- `customer_id`: Unique ID for the customer.
- `feedback_text`: The textual feedback provided by the customer.
- `timestamp`: When the feedback was submitted.
- `source`: Source of the feedback (e.g., web, mobile).
- `sentiment_label`: The actual sentiment (positive, negative, neutral) for supervised learning.

## Requirements

- Python 3.x
- Pandas
- Scikit-learn
- NLTK (Natural Language Toolkit)
- Jupyter Notebook (for running the notebook)

