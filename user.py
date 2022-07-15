class User:
    def __init__(self, name, age, km_per_month, birthday=None, holding_time=None, driving_experience=None, location=None):
        self.name = name
        self.age = age
        self.km_per_month = km_per_month
        if birthday is not None:
            self.birthday = birthday
        if holding_time is not None:
            self.holding_time = holding_time
        if driving_experience is not None:
            self.driving_experience = driving_experience
        if location is not None:
            self.location = location
