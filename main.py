import sys
import csv
import random
import faker
from datetime import datetime 
# Initialize Faker to generate fake data
fake = faker.Faker()

# Create a list of user data
names = []
logins = []
bookings = []
cust_ids = [x for x in range(1, 101)]
random.shuffle(cust_ids)

for i in range(1, 101):
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    password = "helloworld"
    username = first_name + "." + last_name 
    last_login = "2024-12-03 14:14:03"
    password_changed = "2024-12-04 14:32:14"
    start_date = "2025-02-20"
    end_date = "2025-02-22"
    room_id = random.randint(1,331)
    booking_cust_id = cust_ids[i - 1]


    names.append([i,
        first_name, last_name
    ])

    logins.append([username,
        email, password, last_login, password_changed, i
    ])

    bookings.append([i,
        start_date, end_date, room_id, booking_cust_id
    ])

# Define the CSV file names
names_csv_file = "names_csv_file.csv"
logins_csv_file = "logins_csv_file.csv"
bookings_csv_file = "bookings_csv_file.csv"

# Define the header for the CSV files
names_header = ["customder_id", "f_name", "l_name"]
logins_header = ["username", "email", "password", "last_login", "password_changed", "customder_id"]
bookings_header = ["booking_id", "start_date", "end_date", "room_id", "customder_id"]

# Writing data to CSV
with open(names_csv_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(names)

with open(logins_csv_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(logins)

with open(bookings_csv_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(bookings)


print("CSV files have been created.")




