from donor import Person
from event import Event


print("Welcome in the blood donor and location register application!")
print("Please select what would you register: 1 - Donor registration, 2 - Donor location registration")
menu = input(">> ")
if menu == 1:
    Person.donor_register_app()

elif int(menu) == 2:
    Event.event_data()
