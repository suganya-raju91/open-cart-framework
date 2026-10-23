# Importing faker library
# pip install faker
from faker import Faker
# Creating its instance
fake = Faker()
# Generating data
print("First Name",fake.first_name())
print("Last Name",fake.last_name())
print("Name:", fake.name())
print("Address:", fake.address()) 
print("Phone Number:", fake.phone_number()) 
print("Email:", fake.email()) 
print("Job Title:", fake.job()) 
print("Company:", fake.company())