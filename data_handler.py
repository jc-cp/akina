import datetime

class DataHandler:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def get_car_age(self, id):
        current_date_time = datetime.datetime.now()
        date = current_date_time.date()
        year = float(date.strftime("%Y"))
        registry_year = self.dataframe.loc[id, "REGISTRATION_YEAR"]
        return year - registry_year

    def get_emission(self, id):
        return self.dataframe.loc[id, "CO2_EMISSION"]

    def get_displacement(self, id):
        return self.dataframe.loc[id, "DISPLACEMENT"]

    def get_fuel_type(self, id):
        return self.dataframe.loc[id, "FUEL_TYPE"]

    def get_registry_date(self, id):
        return self.dataframe.loc[id, "REGISTRATION_YEAR"]

    def get_listing_price(self, id):
        return self.dataframe.loc[id, "PRICE_PUBLIC"]

    def get_mileage(self, id):
        return self.dataframe.loc[id, "MILEAGE"]

    def get_consumption(self, id):
        return self.dataframe.loc[id, "CONSUMPTION_MIXED"]

    def get_e_consumption(self, id):
        return self.dataframe.loc[id, "ELECTRIC_CONSUMPTION_MIXED"]
