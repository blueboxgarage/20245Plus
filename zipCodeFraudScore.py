import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Generate synthetic data
np.random.seed(42)
num_samples = 1000
zip_codes = np.arange(10000, 10000 + num_samples)
average_income = np.random.uniform(20000, 100000, num_samples)
population_density = np.random.uniform(50, 5000, num_samples)
average_age = np.random.uniform(20, 70, num_samples)
reported_fraud_cases = np.random.randint(0, 50, num_samples)
labels = np.where(reported_fraud_cases > 25, 'Fraud', 'No Fraud')

# Create a DataFrame
data = pd.DataFrame({
    'zip_code': zip_codes,
    'average_income': average_income,
    'population_density': population_density,
    'average_age': average_age,
    'reported_fraud_cases': reported_fraud_cases,
    'label': labels
})

# Features and labels
X = data[['average_income', 'population_density', 'average_age', 'reported_fraud_cases']]
y = data['label']

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Initialize the classifier
classifier = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the classifier
classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = classifier.predict(X_test)

# Evaluate the classifier
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

print('\nClassification Report:')
print(classification_report(y_test, y_pred, target_names=['No Fraud', 'Fraud']))

print('Confusion Matrix:')
print(confusion_matrix(y_test, y_pred))