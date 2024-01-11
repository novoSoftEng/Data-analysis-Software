import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

class DataManager:
    def __init__(self):
        self.data = None
        self.prev_data={}
    def getColumns(self):
        return self.data.columns
    def getData(self):
        return self.data

    def create_dummy_variables(self, columns=None):
        """
        Convert categorical variables into dummy/indicator variables.

        Parameters:
        - columns: list, optional (default=None)
            List of column names to encode. If None, all object or category columns are encoded.

        """
        if columns is None:
            # Select all object or category columns if 'columns' is not specified
            categorical_columns = self.data.select_dtypes(include=['object', 'category']).columns
        else:
            categorical_columns = columns

        # Use pandas get_dummies to create dummy variables
        self.data = pd.get_dummies(self.data, columns=categorical_columns)

        # Alternatively, you can use OneHotEncoder from scikit-learn
        # encoder = OneHotEncoder(drop='first', sparse=False)
        # dummy_variables = encoder.fit_transform(self.data[categorical_columns])
        # self.data = pd.concat([self.data, pd.DataFrame(dummy_variables, columns=encoder.get_feature_names_out(categorical_columns))], axis=1)
    def load_data(self, file_path):
        # Load data from CSV file into a Pandas DataFrame
        self.data = pd.read_csv(file_path)

    def handle_missing_values(self, strategy='mean', fill_value=None):
        """
        Handle missing values in the DataFrame.

        Parameters:
        - strategy: str, optional (default='mean')
            Strategy to use for imputation. Possible values: 'mean', 'median', 'most_frequent', or 'constant'.
        - fill_value: optional, default=None
            The constant value to fill missing values when strategy is 'constant'.

        """
        if strategy == 'constant' and fill_value is None:
            raise ValueError("If strategy is 'constant', a fill_value must be provided.")

        imputer = SimpleImputer(strategy=strategy, fill_value=fill_value)
        self.data = pd.DataFrame(imputer.fit_transform(self.data), columns=self.data.columns)
        return self.data

    def drop_columns(self, column_to_drop):
        self.prev_data[column_to_drop] = self.data.copy()
        # Drop specified columns from the DataFrame
        self.data.drop(columns=[column_to_drop], inplace=True)

    def rollBackDelete(self, col):
        if col in self.prev_data:
            self.data = self.prev_data[col].copy()
            self.prev_data.pop(col)
            print("current columns", self.getColumns())
            return self.data
        else:
            print(f"No previous data found for column {col}")
            return None

    def one_hot_encode(self, columns_to_encode):
        # Perform one-hot encoding on specified categorical columns
        encoder = OneHotEncoder(drop='first', sparse=False)
        encoded_data = pd.DataFrame(encoder.fit_transform(self.data[columns_to_encode]))
        encoded_data.columns = encoder.get_feature_names_out(columns=columns_to_encode)

        # Concatenate the encoded data with the original DataFrame
        self.data = pd.concat([self.data, encoded_data], axis=1)

        # Drop the original categorical columns
        self.data.drop(columns=columns_to_encode, inplace=True)

    def get_features_labels(self, target_column):
        # Extract features (X) and labels (y) from the DataFrame
        features = self.data.drop(columns=[target_column])
        labels = self.data[target_column]
        return features, labels


