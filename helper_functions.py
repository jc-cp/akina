# In this file all helper functions not part of the main class should be included

# Helper function to convert NaN to 0, if there are any, and all other years to integers.
import numpy as np


class Helper:

    def convert_int(x):
        try:
            return int(x)
        except:
            return 0

    def fit_least_squares(X, y):
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

    def fit_ridge(X, y, reg_strength):
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

    def mean_squared_error(y_true, y_pred):
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

    def PolyCoefficients(x, coeffs):
        """ Returns a polynomial for ``x`` values for the ``coeffs`` provided.

        The coefficients must be in ascending order (``x**0`` to ``x**o``).
        """
        o = len(coeffs)
        print(f'# This is a polynomial of order {o}.')
        y = 0
        for i in range(o):
            y += coeffs[i] * x ** i
        return y