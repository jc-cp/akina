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
        print("Hi, and welcome to AKINA v0.1! \n")
        print("Let's find your dream car in under 5 minutes! \n")
        print("First, we want to know what you are actually looking for in a car. \n")
        print("Therefore, a list containing 10 needs will be shown in the next step and we want you to select the five "
              "most relevant ones. \n")

        print("Please press [ENTER].")

        # TODO: add waitforkeyresponse()
        # TODO: check for how to put tabs in print comments
        print("1: " + self.needs[0] + "\t" + "2: " + self.needs[1] + "\n" +
              "3: " + self.needs[2] + "\t" + "4: " + self.needs[3] + "\n" +
              "5: " + self.needs[4] + "\t" + "6: " + self.needs[5] + "\n" +
              "7: " + self.needs[6] + "\t" + "8: " + self.needs[7] + "\n" +
              "9: " + self.needs[2] + "\t" + "10: " + self.needs[9] + "\n")

        # TODO: ask for the needs and return the five selected ones

        # return list_user_needs
        pass

    def run(self):
        self.user_input()
        pass
