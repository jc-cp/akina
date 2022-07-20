import pymongo
from pymongo import MongoClient
import numpy as np
import random
import pandas as pd
from data_handler import DataHandler
from user import User

writer = pd.ExcelWriter("test_data/output.xlsx")

# These are all the cost variables across all ownership models that we will use to evaluate the total cost of ownership
tco_vars = ["INSURANCE_BUYING", "INSURANCE_LEASING", "REGISTRATION", "REPAIRS", "MAINTENANCE", "TAXES", "SUBSIDIES_BUYING", "SUBSIDIES_LEASING",
           "DEPRECIATION", "FUEL_MONTHLY", "LEASING_RATE", "SUBSCRIPTION_RATE", "RESALE_VALUE"]

calc_vars = ["ARTICLE_OFFER_TYPE", "CO2_EMISSION", "DISPLACEMENT", "REGISTRATION_YEAR", "PRICE_PUBLIC", "FUEL_TYPE", "MILEAGE", "CONSUMPTION_MIXED", "ELECTRIC_CONSUMPTION_MIXED"]

# MongoDB Handling
# cluster = MongoClient("mongodb+srv://jayqwalin:sBizum7HyN2Isvmi@cluster0.hvkyyid.mongodb.net/?retryWrites=true&w=majority")
# listings_mongo = cluster["akina"]
# collection = listings_mongo["listings_AutoScout"]
# adac_mongo = listings_mongo["adac_scores"]

# ONLY NEEDS TO BE RUN ONCE - COMMENT AFTER
# for var in tcoVars:
#     collection.update_many({}, {"$set": {var: None}})

# Local Test Data CSV Handling
listings_csv = pd.read_csv("test_data/Test Data.csv", sep=";")

for var in tco_vars:
    listings_csv.insert(loc=len(listings_csv.columns), column=var, value=None)

listings_csv.set_index("GUID", inplace=True)


class TCO:
    def __init__(self):
        pass

    def insurance_buying(self, age, experience, location, body_type, offer_type, car_brand, km_per_month):
        # This is going to be painful af, need tons of user data to scrape web calculators
        return

    def insurance_leasing(self, age, experience, location, body_type, offer_type, car_brand, km_per_month):
        # This is going to be painful af, need tons of user data to scrape web calculators
        return

    @staticmethod
    def registration(location):
        return random.randint(100, 140)

    @staticmethod
    def repairs(km_per_month, car_age):
        inspection_yearly = 100
        oil_change_yearly = 100
        tires_yearly = None
        misc_yearly = None
        return

    @staticmethod
    def inspection():
        return random.randint(57, 134)

    @staticmethod
    def taxes(emission, displacement, fuel_type):
        # SOURCE: https://www.leasingmarkt.de/magazin/recht/auto-unterhaltskosten
        # TODO: Check for exceptions such as "Sonstige" or "Erdgas"
        # TODO: Potentially scrape, check differences due to registry year

        taxes = 0

        if fuel_type == "Elektro": # EVs don't pay taxes for the first 10 years
            return 0
        elif fuel_type == "Benzine" or fuel_type == "Elektro/Benzin":
            taxes += np.ceil(displacement/100)*2
        elif fuel_type == "Diesel" or fuel_type == "Elektro/Diesel":
            taxes += np.ceil(displacement/100)*9.5

        if emission > 95:
            taxes += (emission - 95)*2

        return taxes

    @staticmethod
    def subsidies_buying_new(fuel_type, registry_date, list_price, emission):
        # SOURCE: https://www.adac.de/rund-ums-fahrzeug/elektromobilitaet/kaufen/foerderung-elektroautos/
        if registry_date < 2020 or list_price > 65000:
            return 0

        if fuel_type == "Elektro" and list_price <= 40000:
            return 9000
        elif fuel_type == "Elektro" and list_price > 40000:
            return 7500

        elif (fuel_type == "Elektro/Benzin" or fuel_type == "Elektro/Benzin") and emission < 50:
            if list_price <= 40000:
                return 6750
            else:
                return 5625

    @staticmethod
    def subsidies_buying_used(fuel_type, registry_date, list_price_new, used_price, mileage, emission):
        # SOURCE: https://www.adac.de/rund-ums-fahrzeug/elektromobilitaet/kaufen/foerderung-elektroautos/
        # TODO: Parse registry date string input
        # TODO: Get new list price function
        if registry_date < 2019 or list_price_new > 65000:
            return 0

        if fuel_type == "Elektro":
            if mileage <= 15000 and used_price <= 0.8 * list_price_new: # Conditions to receive government support
                return 5000
            else:
                return 0
        elif (fuel_type == "Elektro/Benzin" or fuel_type == "Elektro/Diesel") and emission < 50:
            if mileage <= 15000 and used_price <= 0.8 * list_price_new:  # Conditions to receive government support
                return 3750
            else:
                return 0
        else:
            return 0

    @staticmethod
    def subsidies_leasing(fuel_type, registry_date, list_price_new, emission, duration):
        # SOURCE: https://www.adac.de/rund-ums-fahrzeug/elektromobilitaet/kaufen/foerderung-elektroautos/
        if registry_date < 2019 or list_price_new > 65000:
            return 0

        if fuel_type == "Elektro":
            if list_price_new <= 40000:
                if duration >= 24:
                    return 3000
                elif duration >= 12:
                    return 1500
                else:
                    return 750
            else:
                if duration >= 24:
                    return 2500
                elif duration >= 12:
                    return 1250
                else:
                    return 625
        elif (fuel_type == "Electron/Benzin" or fuel_type == "Elektro/Benzin") and emission < 50:
            if list_price_new <= 40000:
                if duration >= 24:
                    return 2250
                elif duration >= 12:
                    return 1125
                else:
                    return 562.5
            else:
                if duration >= 24:
                    return 1875
                elif duration >= 12:
                    return 937.5
                else:
                    return 468.75
        else:
            return 0

    def avg_depreciation(self, original_price, car_age, holding_time):  # Holding time in years
        resell_value = self.resell_value(original_price, car_age, holding_time)
        depreciation = original_price - resell_value
        return depreciation/(holding_time)

    @staticmethod
    def fuel_costs(km_per_month, consumption, e_consumption, fuel_type):
        diesel = 1.98
        benzin = 1.8
        kWh = 0.3714
        consumption = consumption/10    # Normalize units to l/100km and kWh/100km
        e_consumption = e_consumption/10

        if fuel_type == "Elektro":
            return e_consumption*km_per_month*kWh/100
        elif fuel_type == "Benzin" or fuel_type == "Elektro/Benzin":
            if not np.isnan(e_consumption):
                return consumption*km_per_month*benzin/100 + e_consumption*km_per_month*kWh/100
            else:
                return consumption*km_per_month*benzin/100
        elif fuel_type == "Diesel" or fuel_type == "Elektro/Diesel":
            if not np.isnan(e_consumption):
                return consumption*km_per_month*diesel/100 + e_consumption*km_per_month*kWh/100
            else:
                return consumption*km_per_month*diesel/100
        else:
            return None

    @staticmethod
    def leasing_rate(holding_time, original_price, residual_value):
        interest_rate = 0.03
        return (original_price - residual_value)/holding_time + (original_price + residual_value)/2 * interest_rate/12

    @staticmethod
    def subscription_rate(km_per_month):
        return

    @staticmethod
    def resell_value(list_price, car_age, holding_time, mileage=None, previous_owners=None):
        holding_time = holding_time/12
        return list_price*pow(0.85, holding_time)


tco = TCO()
dh = DataHandler(listings_csv)
test_user = User("Hans Zimmer", 43, 1200, holding_time=36)


i = 0
for listing in listings_csv.index:
    emission = dh.get_emission(listing)
    displacement = dh.get_displacement(listing)
    fuel = dh.get_fuel_type(listing)
    registration = dh.get_registry_date(listing)
    list_price = dh.get_listing_price(listing)
    mileage = dh.get_mileage(listing)
    consumption = dh.get_consumption(listing)
    e_consumption = dh.get_e_consumption(listing)
    car_age = dh.get_car_age(listing)
    resell_value = tco.resell_value(list_price, car_age, test_user.holding_time)

    listings_csv.loc[listing, "REGISTRATION"] = tco.registration(None)
    listings_csv.loc[listing, "INSPECTION"] = tco.inspection()
    listings_csv.loc[listing, "TAXES"] = tco.taxes(emission, displacement, fuel)

    if listings_csv.loc[listing, "ARTICLE_OFFER_TYPE"] == "Gebraucht" or listings_csv.loc[listing, "ARTICLE_OFFER_TYPE"] == "Jahreswagen":
        listings_csv.loc[listing, "SUBSIDIES_BUYING"] = tco.subsidies_buying_used(fuel, registration, list_price*1.25, list_price, mileage, emission)
    elif listings_csv.loc[listing, "ARTICLE_OFFER_TYPE"] == "Neu":
        listings_csv.loc[listing, "SUBSIDIES_BUYING"] = tco.subsidies_buying_new(fuel, registration, list_price, emission)
    listings_csv.loc[listing, "SUBSIDIES_LEASING"] = tco.subsidies_leasing(fuel, registration, list_price, emission, test_user.holding_time)
    listings_csv.loc[listing, "DEPRECIATION"] = tco.avg_depreciation(list_price, car_age, test_user.holding_time)
    listings_csv.loc[listing, "FUEL_MONTHLY"] = tco.fuel_costs(test_user.km_per_month, consumption, e_consumption, fuel)
    listings_csv.loc[listing, "LEASING_RATE"] = tco.leasing_rate(test_user.holding_time, list_price, resell_value)
    listings_csv.loc[listing, "RESALE_VALUE"] = resell_value

listings_csv[calc_vars + tco_vars].to_excel(writer)
writer.save()
