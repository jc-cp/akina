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
        self.sigVars_listings = ['MAKENAME', 'MODELNAME', 'REGISTRATION_YEAR', 'MILEAGE', 'FUEL_TYPE', 'HORSEPOWER',
                                 'GEARING_TYPE', 'BODY_TYPE', 'PREV_OWNERS', 'WARRANTY', 'FULL_SERVICE', 'EQUIPMENTS',
                                 'EMISSION_CLASS', 'CONSUMPTION_MIXED', 'ELECTRIC_CONSUMPTION_MIXED', 'EFFICIENCY_CLASS',
                                 'CO2_EMISSION', 'SEATS', 'DOORS', 'EMISSION_STICKER']
        self.sigVars_adac = []

    def get_data_listings(self):
        collection = self.db["listings_AutoScout"]
        # print(collection.find({"MAKENAME": "BMW"}))
        # results = self.db.inventory.find({"MAKENAME": "BMW"})
        # results = collection.find({"MAKENAME": "BMW"})

        results = collection.find({})

        for result in results:
            print(result)

        self.cluster.close()
        return results

    def get_data_adac(self):
        collection = self.db["adac_scores"]
        # results = collection.find({"MAKENAME": "BMW"})
        self.cluster.close()

    def cat_to_num(self):
        pass

    def plot_variables(self):
        # This function shows how the density functions of different variables look like.
        # sns.distplot(listings_numeric['CO2_EMISSION'], hist=False, kde=True,
        #              bins=int(20), color = 'darkblue', hist_kws={'edgecolor':'black'},
        #              kde_kws={'linewidth': 4},)
        # sns.kdeplot(listings_numeric['CO2_EMISSION'])
        pass

    def plot_density(self):#
        fx = np.linspace(-5, 5, 100)
        # f = -1.88143044e-13 * pow(fx,5) + 1.97031937e-10 * pow(fx,4) + -6.78677633e-08 * pow(fx,3) + 8.93899760e-06 * pow(fx,2) + -3.54868029e-04 * fx + 4.00692692e-03
        f = 5.64926944e-12 * pow(fx, 5) + -2.46999496e-09 * pow(fx, 4) + 3.38290013e-07 * pow(fx,
                                                                                              3) + -1.40586450e-05 * pow(
            fx, 2) + 2.24944543e-05 * fx + 2.83365680e-03
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')

        # plot the function
        plt.plot(fx, f, 'r')

        # show the plot
        plt.show()

    def get_function_out_of_plot(self):
        # x, y = sns.kdeplot(listings_numeric['HORSEPOWER']).get_lines()[0].get_data()
        # function = np.polyfit(x,y, 5)
        # f_von_x = function[0] * pow(fx,5) + function[1] * pow(fx,4) + function[2] * pow(fx,3) + function[3] *
        # pow(fx,2) + function[4] * pow(fx,1) + function[5]
        pass




if __name__ == "__main__":
    # Generate an instance of the class
    pp = Preprocessing()

    pp.get_data_listings()
    # pp.get_data_adac()
