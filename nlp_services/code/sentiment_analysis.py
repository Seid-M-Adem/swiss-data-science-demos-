import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
from nltk.corpus import stopwords
import nltk

# Download the stopwords if you don't have them already
nltk.download('stopwords')

# Load dataset
df = pd.read_csv('/workspaces/swiss-data-science-demos-/nlp_services/data/reader_feedback.csv')

# Text preprocessing
def preprocess_text(text):
    # Lowercase
    text = text.lower()
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in text.split() if word not in stop_words]
    return ' '.join(words)

df['cleaned_feedback_text'] = df['feedback_text'].apply(preprocess_text)

# Feature extraction
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['cleaned_feedback_text'])

# Labels
y = df['sentiment_label']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')
print('Classification Report:')
print(classification_report(y_test, y_pred))

# Save the model
import joblib
joblib.dump(model, 'sentiment_model.pkl')

