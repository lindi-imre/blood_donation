from donor import Person
from event import Event

print("<~~~~~~~~----------------------^^^^^^^----------------------~~~~~~~>")
print("Welcome in the blood donor and event location register application!")
print("Please select what would you like to register:\n1 - Donor registration\n2 - Donor event location registration")
menu = input(">> ")
while not menu == "1" or not menu == "2":
    if menu == "1":
        Person.donor_register_app()
    elif menu == "2":
        Event.event_data()

    else:
        print("Please select a valid menu number!")
        menu = input(">> ")


