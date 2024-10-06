import os
import re
import numpy as np
import pandas as pd
from bertopic import BERTopic
from openai import OpenAI

# Initialize the OpenAI client with your API key
api_key = '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'
client = OpenAI(api_key=api_key)

# Load the data
df = pd.read_excel('acl_only_4-5_rated_papers_final.xlsx')

# Function to preprocess text
def preprocess_text(text):
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return text.lower().strip()  # Convert to lowercase and strip trailing spaces

# Apply text preprocessing
df['Evidence'] = df['Evidence'].apply(preprocess_text)

# Function to get embeddings using OpenAI
def get_embeddings(text):
    try:
        response = client.Completion.create(
            model="text-similarity-babbage-001",
            inputs=text,
            max_tokens=2048  # Adjust as necessary for your model's limits
        )
        return np.array(response['choices'][0]['embeddings'])
    except Exception as e:
        print(f"Error obtaining embeddings: {e}")
        return np.zeros(1024)  # Return a zero-filled array if an error occurs, adjust size based on your model

# Generate embeddings for all evidence
embeddings = np.array([get_embeddings(text) for text in df['Evidence']])

# Initialize BERTopic without specifying an embedding model since we use custom embeddings
topic_model = BERTopic()

# Fit BERTopic using the embeddings
topics, _ = topic_model.fit_transform(df['Evidence'], embeddings)

# Get and display topic information
topic_info = topic_model.get_topic_info()
print(topic_info)

# Save the clustered data to a CSV file
df['Topic'] = topics
df.to_csv('clustered_evidence_with_bertopic.csv', index=False)

print("Clustering complete and saved.")
