import pymongo
from pymongo import MongoClient
import numpy as np

cluster = MongoClient("mongodb+srv://jayqwalin:sBizum7HyN2Isvmi@cluster0.hvkyyid.mongodb.net/?retryWrites=true&w=majority")
db = cluster["akina"]
collection = db["listings_AutoScout"]
adac = db["adac_scores"]

# These are the variables that the user can define which will affect the calculation, defaults are below, periods are in years
userInput = {"KM_PER_MONTH": 1000, "HOLDING_TIME": 5, "Birthday": "15.10.1990", "PREVIOUS_EXPERIENCE": 3, "NUMBER_OF_DRIVERS": 1,
             "LOCATION": None, "INSURANCE_TYPE": None, "OWNS_CAR_ATM": None}

# These are all the cost variables across all ownership models that we will use to evaluate the total cost of ownership
tcoVars = ["INSURANCE_BUYING", "INSURANCE_LEASING", "REGISTRATION", "REPAIRS", "MAINTENANCE", "TAXES", "SUBSIDIES",
           "DEPRECIATION", "FUELCOST_PER_KM", "LEASING_RATE", "SUBSCRIPTION_RATE"]

outputVars = {"BUYING": None, "LEASING": None, "SUBSCRIPTION": None}

# ONLY NEEDS TO BE RUN ONCE - COMMENT AFTER
# for var in tcoVars:
#     collection.update_many({}, {"$set": {var: None}})

def insurance_buying(age, experience, location, body_type, offer_type, car_brand, km_per_month):
# This is going to be painful af, need tons of user data to scrape web calculators

def insurance_leasing(age, experience, location, body_type, offer_type, car_brand, km_per_month):
# This is going to be painful af, need tons of user data to scrape web calculators

def registration(location):

def repairs(km_per_month, car_age):
    inspection_yearly = 100
    oil_change_yearly = 100
    tires_yearly = None
    misc_yearly = None

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

def subsidies_buying_new(fuel_type, registry_date, list_price, consumption):
# SOURCE: https://www.adac.de/rund-ums-fahrzeug/elektromobilitaet/kaufen/foerderung-elektroautos/
    if registry_date < 2020 or list_price > 65000:
        return 0

    if fuel_type == "Elektro" and list_price <= 40000:
        return 9000
    elif fuel_type == "Elektro" and list_price > 40000:
        return 7500

    elif (fuel_type == "Elektro/Benzin" or fuel_type == "Elektro/Benzin") and consumption < 50:
        if list_price <= 40000:
            return 6750
        else:
            return 5625


def subsidies_buying_used(fuel_type, registry_date, list_price_new, used_price, mileage, consumption):
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
    elif (fuel_type == "Elektro/Benzin" or fuel_type == "Elektro/Benzin") and consumption < 50:
        if mileage <= 15000 and used_price <= 0.8 * list_price_new:  # Conditions to receive government support
            return 3750
        else:
            return 0

def subsidies_leasing(fuel_type, registry_date, list_price_new, consumption, duration):
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
    elif (fuel_type == "Electron/Benzin" or fuel_type == "Elektro/Benzin") and consumption < 50:
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


def depreciation(car_age, original_price):

def fuel_costs(km_per_month, consumption ):

def leasing_rate(holding_time, original_price, residual_value):
# TODO: Define residual value function

    interest_rate = 0.03

    return (original_price - residual_value)/holding_time + (original_price + residual_value)/2 * interest_rate/12


def subscription_rate(km_per_month):


def resell_value(holding_time, mileage, previous_owners):