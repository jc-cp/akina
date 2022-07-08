import pymongo
from pymongo import MongoClient
import numpy as np

cluster = MongoClient("mongodb+srv://jayqwalin:sBizum7HyN2Isvmi@cluster0.hvkyyid.mongodb.net/?retryWrites=true&w=majority")
db = cluster["akina"]
collection = db["listings_AutoScout"]
adac = db["adac_scores"]

# These are the variables that the user can define which will affect the calculation, defaults are below, periods are in years
userInput = {"KM_PER_MONTH": 1000, "HOLDING_TIME": 5, "AGE": 30, "PREVIOUS_EXPERIENCE": 3, "NUMBER_OF_DRIVERS": 1, "LOCATION": None, "INSURANCE_TYPE": None}

# These are all the cost variables across all ownership models that we will use to evaluate the total cost of ownership
tcoVars = ["INSURANCE_BUYING", "INSURANCE_LEASING", "REGISTRATION", "REPAIRS", "MAINTENANCE", "TAXES", "SUBSIDIES",
           "DEPRECIATION", "FUELCOST_PER_KM", "LEASING_RATE", "SUBSCRIPTION_RATE"]

outputVars = {"BUYING": None, "LEASING": None, "SUBSCRIPTION": None}

# ONLY NEEDS TO BE RUN ONCE - COMMENT AFTER
# for var in tcoVars:
#     collection.update_many({}, {"$set": {var: None}})

def insurance_buying(age, experience, location, body_type, offer_type, car_brand, km_per_month):
    base_price = 0

def insurance_leasing(age, experience, location, body_type, offer_type, car_brand, km_per_month):

def registration(location):

def repairs(km_per_month, car_age):
    inspection_yearly = 100
    oil_change_yearly = 100
    tires_yearly = None
    misc_yearly = None

def taxes(emission, displacement, fuel_type):
# SOURCE: https://www.leasingmarkt.de/magazin/recht/auto-unterhaltskosten
# TODO: Check for exceptions such as "Sonstige" or "Erdgas"

    taxes = 0

    if (fuel_type == "Elektro"): # EVs don't pay taxes for the first 10 years
        return 0
    elif (fuel_type == "Benzin" or fuel_type == "Elektro/Benzin"):
        taxes += np.ceil(displacement/100)*2
    elif (fuel_type == "Diesel" or fuel_type == "Elektro/Diesel"):
        taxes += np.ceil(displacement/100)*9.5

    if (emission > 95):
        taxes += (emission - 95)*2

    return taxes


def subsidies(fuel_type):

def depreciation(car_age, original_price):

def fuel_costs(km_per_month, consumption ):

def leasing_rate(holding_time, original_price):

def subscription_rate(km_per_month):

def resell_value(holding_time):







