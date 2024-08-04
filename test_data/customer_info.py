"""
The module contains the methods to generate fake customer data.
"""

from faker import Faker


class Customer:
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.postal_code = None

    def generate_customer_data(self):
        fake = Faker()

        self.first_name = fake.first_name_female()
        self.last_name = fake.last_name_female()
        self.postal_code = fake.postcode()

    def __str__(self):
        return f"User name is '{self.first_name}' '{self.last_name}', postal code is '{self.postal_code}'"
