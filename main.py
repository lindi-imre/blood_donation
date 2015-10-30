from donor import Person
from event import Event

print("<~~~~~~~~----------------------^^^^^^^----------------------~~~~~~~>")
print("Welcome in the blood donor and event location register application!")
print("Please select what would you like to register:\n1 - Donor registration\n2 - Donor event location registration")
menu = input(">> ")
while not menu == "1" or not menu == "2":
    if menu == "1":
        Person.donor_register_app()
        print("Please select what would you like to register:\n1 - Donor event location registration\n2 - Exit")
        menu2 = input(">> ")
        while not menu2 == "1" or not menu2 == "2":
            if menu2 == "1":
                Event.event_data()
                exit()
            elif menu2 == "2":
                exit()
    elif menu == "2":
        Event.event_data()
        print("Please select what would you like to register:\n1 - Donor registration\n2 - Exit")
        menu3 = input(">> ")
        while not menu3 == "1" or not menu3 == "2":
            if menu3 == "1":
                Person.donor_register_app()
                exit()
            elif menu3 == "2":
                exit()
    else:
        print("Please select a valid menu number!")
        menu = input(">> ")
