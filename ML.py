from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
import numpy as np
class ML:
    def __init__(self,model,X,y):
        self.model=model
        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)
        self.model=self.model.fit(X_train,y_train)
        self.X_train=X_train
        self.y_train=y_train
        self.X_test = X_test
        self.y_test = y_test
    def predict(self,X):
        self.prediction = self.model.predict(X)
        return self.prediction
    def evaluate(self):
        # Evaluate the model on test data and return metrics
        predictions = self.predict(self.X_test)
        accuracy = accuracy_score(self.y_test, predictions)
        confusion_mat = confusion_matrix(self.y_test, predictions)
        return accuracy, confusion_mat

# Example usage:
# Assuming you have a machine learning model (e.g., from scikit-learn)
from sklearn.ensemble import RandomForestClassifier

# Create a random forest classifier (replace this with your chosen model)
model = RandomForestClassifier(n_estimators=100)

# Generate some dummy data for demonstration purposes
X, y = np.random.rand(100, 5), np.random.choice([0, 1], size=100)

ml = ML(model,X,y)

# Evaluate the model
accuracy, confusion_matrix = ml.evaluate()

# Print the results
print(f"Accuracy: {accuracy}")
print("Confusion Matrix:")
print(confusion_matrix)

