from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
import numpy as np
class ML:
    def __init__(self,model,X,y):
        self.model=model
        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)
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

