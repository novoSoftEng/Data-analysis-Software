import os

import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

class DataManager:
    def __init__(self):
        self.csv_files=None
        self.data = None
        self.file_path=None
        self.prev_data={}
        self.find_data_files()

    def update_file(self,data):
        if self.file_path:
            try:
                # Overwrite the existing file with the updated data
                data.to_csv(self.file_path, index=False)
                self.data = data
                print(f"File '{self.file_path}' updated successfully.")
            except Exception as e:
                print(f"Error updating the file: {str(e)}")
        else:
            print("No file path specified. Use set_file_path method to set a file path.")

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
            # Assuming self.data is your DataFrame
            columns_to_convert = self.data.select_dtypes(include='object').columns

            # Convert object columns to numeric (if they contain numbers)
            self.data[columns_to_convert] = self.data[columns_to_convert].apply(pd.to_numeric, errors='ignore')
            print("data types",self.data.dtypes)
            # Select all object or category columns if 'columns' is not specified
            categorical_columns = self.data.select_dtypes(include=['object'],exclude=['float64','int64']).columns
        else:
            categorical_columns = columns

        # Use pandas get_dummies to create dummy variables with binary values (0/1)
        print("categorical_columns",categorical_columns)
        dummy_variables = pd.get_dummies(
            self.data[categorical_columns],
            columns=categorical_columns,
            prefix=None,  # Use column names as prefixes
            prefix_sep='_',
            dummy_na=False,
        )

        # Concatenate dummy variables with the original DataFrame
        self.data = pd.concat([self.data, dummy_variables], axis=1)

        # Drop the original categorical columns
        self.data.drop(columns=categorical_columns, inplace=True)
    def load_data(self, file_path):
        # Load data from CSV file into a Pandas DataFrame
        self.file_path=file_path
        self.data = pd.read_csv(file_path)
    def find_data_files(self):
        current_folder = os.path.dirname(os.path.abspath(__file__))
        self.csv_files = [file for file in os.listdir(current_folder) if file.endswith('.csv')]
        return self.csv_files

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






