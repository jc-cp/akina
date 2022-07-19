# In this file all helper functions not part of the main class should be included

# Helper function to convert NaN to 0, if there are any, and all other years to integers.
import numpy as np


class HelperFunctions:

    def __init__(self):
        self.needs = ['SUSTAINABILTY', 'STORAGE', 'SPACE', 'TRAVEL_FRIENDLY', 'DRIVING_EXPERIENCE', 'CITY_FRIENDLY',
                      'FAMILY_FRIENDLY', 'STATUS', 'FUEL_EFFICIENCY']

    def convert_int(self, x):
        try:
            return int(x)
        except:
            return 0

    def fit_least_squares(self, X, y):
        """Fit ordinary least squares model to the data.

        Parameters
        ----------
        X : array, shape [N, D]
            (Augmented) feature matrix.
        y : array, shape [N]
            Regression targets.

        Returns
        -------
        w : array, shape [D]
            Optimal regression coefficients (w[0] is the bias term).

        """
        return np.linalg.pinv(X) @ y

    def fit_ridge(self, X, y, reg_strength):
        """Fit ridge regression model to the data.

        Parameters
        ----------
        X : array, shape [N, D]
            (Augmented) feature matrix.
        y : array, shape [N]
            Regression targets.
        reg_strength : float
            L2 regularization strength (denoted by lambda in the lecture)

        Returns
        -------
        w : array, shape [D]
            Optimal regression coefficients (w[0] is the bias term).

        """
        return np.linalg.inv(X.T @ X + reg_strength * np.eye(X.shape[1])) @ X.T @ y

    def mean_squared_error(self, y_true, y_pred):
        """Compute mean squared error between true and predicted regression targets.

        Reference: `https://en.wikipedia.org/wiki/Mean_squared_error`

        Parameters
        ----------
        y_true : array
            True regression targets.
        y_pred : array
            Predicted regression targets.

        Returns
        -------
        mse : float
            Mean squared error.

        """
        return np.mean((y_true - y_pred) ** 2)

    def user_input(self):
        # TODO: ask for the needs and return the five selected ones
        pass

    def run(self):
        pass
