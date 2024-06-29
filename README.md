zipCodeHeatMap.py
Class plots the zip codes provided in the "zip_codes.csv" file on a global heat-map, saved into project directory as "zip_copes_heatmap.html"

MLPractice.py
Using sample Dataset to predict bird species.

UrbanOrRuralZip.py
Predict whether Zip Codes or urban or rural.

Machine learning example where we predict whether a ZIP code is more susceptible to fraud based on some features. We'll generate a synthetic dataset with ZIP codes and features such as average income, population density, average age, and number of reported fraud cases. Then, we'll train a classifier to predict fraud susceptibility.

Apriori Data:
Number of fraud cases per zip code.

Explanation
Generate Synthetic Data:
zip_codes: Sequential ZIP codes from 10000.
average_income: Random values between 20000 and 100000.
population_density: Random values between 50 and 5000.
average_age: Random values between 20 and 70.
reported_fraud_cases: Random integer values between 0 and 50.
labels: Based on the number of reported fraud cases, ZIP codes with more than 25 cases are labeled as Fraud, others as No Fraud.
Create DataFrame: A pandas DataFrame is created to hold the generated data.
Features and Labels: The features are selected (average_income, population_density, average_age, reported_fraud_cases), and the label is label.
Split Dataset: The data is split into training and test sets using train_test_split().
Standardize Features: The features are standardized using StandardScaler().
Initialize Classifier: A RandomForestClassifier is used for classification.
Train Classifier: The classifier is trained using the training data.
Make Predictions: Predictions are made on the test set.
Evaluate Classifier: The classifier's performance is evaluated using accuracy, a classification report, and a confusion matrix.

trendLine.py
takes input from .txt fileand creates a line graph to show the trend


