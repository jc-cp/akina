# This file should contain all functions that are responsible for the pre-processing of the data.

from pymongo import MongoClient
import matplotlib as plt


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

    def convert_to_numerical_values(self):
        pass

    def plot_variables(self):
        pass

    def get_function_out_of_plot(self):
        pass


if __name__ == "__main__":
    # Generate an instance of the class
    pp = Preprocessing()

    pp.get_data_listings()
    # pp.get_data_adac()
