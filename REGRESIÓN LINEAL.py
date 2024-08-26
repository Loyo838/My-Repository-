class LinearRegressionManual:
    def __init__(self):
        self.coef_ = None
        self.intercept_ = None

    def fit(self, X, y):
        n = len(X)
        sum_x = sum(X)
        sum_y = sum(y)
        sum_xy = sum([X[i] * y[i] for i in range(n)])
        sum_xx = sum([x ** 2 for x in X])

        self.coef_ = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x ** 2)
        self.intercept_ = (sum_y - self.coef_ * sum_x) / n

    def predict(self, X):
        return [self.coef_ * x + self.intercept_ for x in X]

if __name__ == "__main__":
    # Ejemplo de uso
    X = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    model = LinearRegressionManual()
    model.fit(X, y)
    predictions = model.predict([6, 7, 8])

    print("Predicciones:", predictions)
