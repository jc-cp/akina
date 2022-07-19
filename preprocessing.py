# This file should contain all functions that are responsible for the pre-processing of the data.

from pymongo import MongoClient
import matplotlib as plt
import numpy as np
from scipy.optimize import curve_fit
import seaborn as sns


class Preprocessing:

    def __init__(self):
        self.cluster = MongoClient(
            "mongodb+srv://jayqwalin:sBizum7HyN2Isvmi@cluster0.hvkyyid.mongodb.net/?retryWrites=true&w=majority")

        self.db = self.cluster["akina"]

        self.sigVars_listings = ['GUID', 'MAKENAME', 'MODELNAME', 'REGISTRATION_YEAR', 'MILEAGE', 'FUEL_TYPE',
                                 'HORSEPOWER', 'GEARING_TYPE', 'BODY_TYPE', 'PREV_OWNERS', 'WARRANTY', 'FULL_SERVICE',
                                 'EQUIPMENTS', 'EMISSION_CLASS', 'CONSUMPTION_MIXED', 'ELECTRIC_CONSUMPTION_MIXED',
                                 'EFFICIENCY_CLASS', 'CO2_EMISSION', 'SEATS', 'DOORS', 'EMISSION_STICKER']

        self.sigVars_listings_num = ['REGISTRATION_YEAR', 'MILEAGE', 'HORSEPOWER', 'PREV_OWNERS', 'CONSUMPTION_MIXED',
                                     'ELECTRIC_CONSUMPTION_MIXED', 'CO2_EMISSION', 'SEATS', 'DOORS']

        self.sigVars_listings_cat = ['GUID', 'MAKENAME', 'MODELNAME', 'FUEL_TYPE', 'GEARING_TYPE', 'BODY_TYPE',
                                     'WARRANTY', 'FULL_SERVICE', 'EQUIPMENTS', 'EMISSION_CLASS', 'EFFICIENCY_CLASS',
                                     'EMISSION_STICKER']

        self.sigVars_adac = []

        self.scoring_scale = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def get_data_listings(self):
        collection = self.db["listings_AutoScout"]
        # print(collection.find({"MAKENAME": "BMW"}))
        # results = self.db.inventory.find({"MAKENAME": "BMW"})
        # results = collection.find({"MAKENAME": "BMW"})

        results = collection.find({})

        for result in results:
            # print(result)
            pass

        # TODO: Change the Cursor object retrieved from MONGODB to a "pandas"-style dataframe
        # TODO: Filtering of sigVars to numerical and categorical and add them as return values

        self.cluster.close()
        return results

    def get_data_adac(self):
        collection = self.db["adac_scores"]
        # results = collection.find({"MAKENAME": "BMW"})
        self.cluster.close()

    def cat_to_num(self):
        # TODO: Think about individual or generic cases
        pass

    def filter_numerical(self, listings_numerical):
        """ Filters outliers according to mean and standard deviation of the infividual categories
        """
        n_std = 2
        for col in listings_numerical.columns:
            mean = listings_numerical[col].mean()
            sd = listings_numerical[col].std()
            listings_numerical = listings_numerical[listings_numerical[col] <= mean + (n_std * sd)]

        listings_numerical_filtered = listings_numerical

        return listings_numerical_filtered

    def plot_distribution(self, variable, listings_numeric):
        """ Plots the histogram with the density provided by the input variable.
        """
        string = str(variable)
        sns.displot(listings_numeric[string], kde=True, stat='count')

    def get_density_data(self, variable, listings_numeric):
        """ Returns the ``x`` and ``y`` values from the density function provided by the input variable.
        """
        string = str(variable)
        x, y = sns.kdeplot(listings_numeric[string], cut=0).get_lines()[0].get_data()
        return x, y

    def polynomial_fit(self, x, y, degree):
        """ Does a polynomial fit with the data and degree provided. Returns the coefficients fot the polynomial.
        """
        function = np.polyfit(x, y, degree)
        return function

    def poly_coefficients(self, x, coeffs):
        """ Returns a polynomial for ``x`` values for the ``coeffs`` provided.

        The coefficients must be in ascending order (``x**0`` to ``x**o``).
        """
        o = len(coeffs)
        rev_coeffs = coeffs[::-1]
        # print(f'# This is a polynomial of order {o}.')
        y = 0
        for i in range(o):
            y += rev_coeffs[i] * x ** i
        return y

    def exponential(self, x, a, b):
        """ Returns an exponential with constants a and b.
        """
        return a * np.exp(b * x)

    def linear(self, x, m, c):
        """ Returns a linear with constants m and c.
        """
        return m * x + c

    def plot_values(self, x, y):
        fx = np.linspace(0, np.max(x), len(x))
        plt.plot(fx, y)
        plt.xlim(0, np.max(x))
        plt.ylim(0, np.max(y))
        plt.show()

    def plot_comparison(self, apprx_function, density_x, density_y):
        """ Takes in the approximated functionand plots it against the extracted density.
        """
        fx = np.linspace(0, np.max(density_x), len(density_x))

        fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(15, 10), sharey='all', sharex='all')
        fig.suptitle('Comparison of density and approximation.')
        ax = fig.add_subplot(1, 1, 1)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')

        # plot the function
        plt.subplot(1, 2, 1)
        plt.xlim(0, np.max(density_x))
        plt.ylim(0, np.max(density_y))
        plt.plot(fx, density_y, 'r.-')
        plt.ylabel('Density')

        plt.subplot(1, 2, 2)
        plt.plot(fx, apprx_function, 'ko-')
        plt.ylabel('Approximation')

        plt.tight_layout()
        plt.show()

    def scoring_mileage(self, density_x):
        mapping = map(lambda perc: np.percentile(density_x, perc * 10), self.scoring_scale)
        scoring = list(mapping)[::-1]
        return scoring


    def run(self):
        listings = self.get_data_listings()
        # TODO: how to change from Cursor object to "pandas"-style dataframe
        listings_num_filtered = self.filter_numerical(self, listings)

        while True:
            user_input = input("Do you want to see the data distributions for all features (y/n)? ")

            if user_input == 'y':
                # TODO: define "feature" as the name that had to be entered before
                for feature in listings_num_filtered:
                    x, y = self.get_density_data(self, feature, listings_num_filtered)
                    function_coefficients = self.polynomial_fit(x, y, 15)
                    fx = np.linspace(0, np.max(x), len(x))
                    apprx_function_values = self.poly_coefficients(fx, function_coefficients)
                    self.plot_comparison(self, apprx_function_values, x, y)
                break
            elif user_input == 'n':
                break
            else:
                print("Please answer simply with \'y\' for yes and \'n\' for no.")
                # TODO: add back loop to the if/ else clauses ? CHECK THE WHILE LOOP LOGIC

        print("Calculating all scores, please wait.")

        # TODO: define "feature" as the name that had to be entered before
        for feature in listings_num_filtered:
            pass

    # TODO: Think about returning all scores as end-result of this class, can be fed into NN ?
    # return scores


if __name__ == "__main__":
    # Generate an instance of the class
    pp = Preprocessing()
    pp.run()
