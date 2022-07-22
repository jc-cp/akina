# In this file all helper functions not part of the main class should be included

# Helper function to convert NaN to 0, if there are any, and all other years to integers.
import numpy as np
import pandas as pd


class HelperFunctions:

    def __init__(self):
        self.needs = ['SUSTAINABILITY', 'STORAGE', 'TRAVEL_FRIENDLY', 'DRIVING_EXPERIENCE', 'CITY_FRIENDLY',
                      'FAMILY_FRIENDLY', 'STATUS', 'FUEL_EFFICIENCY', 'COMFORT', 'SAFETY', 'E-MOBILITY', 'RELIABILITY']

        self.list_user_needs = []

    @staticmethod
    def convert_int(x):
        try:
            return int(x)
        except:
            return 0

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

        list_user_needs = self.list_user_needs
        return list_user_needs

    def match_needs_to_scores(self, list_user_needs):
        user_input_scores = []
        avg_final_score = []
        listings_scores = pd.read_csv('test_data/listings_shorted_scores.csv', sep=',')
        listings_scores.reset_index()
        flag = 0

        for need in list_user_needs:
            if need == 'SUSTAINABILITY':
                list_scores_sus = listings_scores['CO2_EMISSION_SCORE']
                listings_scores[need + "_SCORE"] = list_scores_sus
                user_input_scores.append(list_scores_sus)
                # print('sus_scores: ', list_scores_sus)
            elif need == 'STORAGE':
                list_scores_sto = listings_scores['SEATS_SCORE']
                user_input_scores.append(list_scores_sto)
            elif need == 'DRIVING_EXPERIENCE':
                list_scores_hp = listings_scores['HORSEPOWER_SCORE']
                listings_scores[need + "_SCORE"] = list_scores_hp
                user_input_scores.append(list_scores_hp)
            elif need == 'CITY_FRIENDLY':
                pass
            elif need == 'TRAVEL_FRIENDLY':
                pass
            elif need == 'FAMILY_FRIENDLY':
                pass
            elif need == 'STATUS':
                pass
            elif need == 'FUEL_EFFICIENCY':
                if flag == 0:
                    list_scores_cm = listings_scores['CONSUMPTION_MIXED_SCORE']
                    listings_scores[need + "_SCORE"] = list_scores_cm
                    user_input_scores.append(list_scores_cm)
                elif flag == 1:
                    list_scores_ecm = listings_scores['ELECTRIC_CONSUMPTION_MIXED_SCORE']
                    user_input_scores.append(list_scores_ecm)
            elif need == 'COMFORT':
                list_scores_com = listings_scores['SEATS_SCORE']
                listings_scores[need + "_SCORE"] = list_scores_com
                user_input_scores.append(list_scores_com)
            elif need == 'SAFETY':
                pass
            elif need == 'E-MOBILITY':
                # TODO: filter all non electric cars
                flag = 1

            elif need == 'RELIABILITY':
                list_scores_rel_1 = listings_scores['MILEAGE_SCORE']
                list_scores_rel_2 = listings_scores['REGISTRATION_YEAR_SCORE']

                average_list = (list_scores_rel_1 + list_scores_rel_2) / 2
                listings_scores[need + "_SCORE"] = average_list
                user_input_scores.append(average_list)

            else:
                print("Couldn't find need.")

        for j in range(0, len(user_input_scores[0])):
            avg_scores_user = 0
            for i in range(0, len(user_input_scores)):
                avg_scores_user += user_input_scores[i][j]
            avg_final_score.append(avg_scores_user/5)

        listings_scores["SUM_USER"] = 0

        for i in range(0, len(user_input_scores[0])):
            listings_scores.iloc[i, listings_scores.columns.get_loc("SUM_USER")] = avg_final_score[i]

        listings_scores.to_csv('test_data/matched_scores.csv', encoding='utf-8')

        return listings_scores

    def filter_budget(self, listings_df, budget):
        listings = listings_df
        listings = listings[listings["PRICE_PUBLIC"] <= budget]
        listings.reset_index()
        max_val = max(list(listings["SUM_USER"]))

        index = list(listings["SUM_USER"]).index(max(listings["SUM_USER"]))
        print(max_val, index, listings.iloc[index, listings.columns.get_loc("GUID")])
        listings.to_csv('test_data/output.csv')

        return max_val, index, listings.iloc[index, listings.columns.get_loc("GUID")]

    def find_car(self, big_listings, id):

        makename = big_listings.loc[big_listings["GUID"] == id]["MAKENAME"].item()
        modelname = big_listings.loc[big_listings["GUID"] == id]["MODELNAME"].item()
        offer_link = big_listings.loc[big_listings["GUID"] == id]["DETAIL_LINK"].item()
        image_link = big_listings.loc[big_listings["GUID"] == id]["IMAGE_URL"].item()

        print(makename)
        print(modelname)
        print(image_link)
        print(offer_link)

        return makename, modelname, image_link, offer_link

    def run(self, budget):
        list_user_needs = ['COMFORT', 'RELIABILITY', 'FUEL_EFFICIENCY', 'DRIVING_EXPERIENCE', 'SUSTAINABILITY']
        listings_df = self.match_needs_to_scores(list_user_needs)
        max_val, index, id = self.filter_budget(listings_df, budget)

        big_listings = pd.read_csv('test_data/listings.de_de.csv')
        makename, modelname, image_link, offer_link = self.find_car(big_listings, id)

        out_dict = dict.fromkeys(list_user_needs, 0)
        for need in list_user_needs:
            out_dict[need] = listings_df.loc[listings_df["GUID"] == id][need + "_SCORE"].item()
        # print(out_dict)

        return max_val, index, id, out_dict, makename, modelname, image_link, offer_link


if __name__ == "__main__":
    # Generate an instance of the class
    hf = HelperFunctions()
    hf.run()