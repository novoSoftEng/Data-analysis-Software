class ML:
    def __init__(self,algo,X,y):
        self.algo=algo
        self.model=self.algo.fit(X,y)
        self.X=X
        self.y=y
    def predict(self,X):
        self.prediction = self.model.predict(X)
        return self.prediction


