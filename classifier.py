from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import numpy as np

# Load example dataset
data = load_iris()
X = data.data
y = data.target

# Split data into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the classifier
classifier = RandomForestClassifier()
classifier.fit(X_train, y_train)

# Predict on test data
y_pred = classifier.predict(X_test)

# Print evaluation metrics
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nAccuracy Score:")
print(accuracy_score(y_test, y_pred) * 100)

# Predict on new data
new = np.array([[0.74521, 3.6357, -4.4044, -4.1414]])
y_pred_new = classifier.predict(new)
print("\nPredicted class is:", y_pred_new[0])
