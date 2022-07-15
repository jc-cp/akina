import datetime

class DataHandler:
    def __int__(self, dataframe):
        self.dataframe = dataframe

    @staticmethod
    def get_car_age(self, id):
        current_date_time = datetime.datetime.now()
        date = current_date_time.date()
        year = float(date.strftime("%Y"))
        registry_year = self.dataframe.loc(id, "REGISTRATION_YEAR")
        return year - registry_year

    @staticmethod
    def get_emission(self, id):
        return self.dataframe.log(id, "CO2_EMISSION")

    @staticmethod
    def get_displacement(self, id):
        return self.dataframe.log(id, "DISPLACEMENT")

    @staticmethod
    def get_fuel_type(self, id):
        return self.dataframe.log(id, "FUEL_TYPE")

    @staticmethod
    def get_registry_date(self, id):
        return self.dataframe.loc(id, "REGISTRATION_YEAR")

    @staticmethod
    def get_listing_price(self, id):
        return self.dataframe.loc(id, "PRICE_PUBLIC")

    @staticmethod
    def get_mileage(self, id):
        return