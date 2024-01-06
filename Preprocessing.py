from sklearn import preprocessing
class Preprocessing:
    def __init__(self,X):
        self.X=X
    def standardization(self):
        scaler = preprocessing.StandardScaler().fit(self.X)
        return scaler.transform(self.X)
    def normalization(self):
        return preprocessing.normalize(self.X, norm='l2')
