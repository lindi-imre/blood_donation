from donor_registration_basic_datas import Person

print("Welcome in the blood donor and location register application!")
print("Please select what would you register: 1 - Donor registration, 2 - Donor location registration")
if int(input()) == 1:
    Person.donor_register_app()

elif int(input) == 2:
    pass
