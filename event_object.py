class EventObject(object):

    def __init__(self, id, date_of_event, start_time, end_time, zip_code, city, address, available_beds, \
                 planned_donor_number, final_donor_number):
        self.id = id
        self.date_of_event = date_of_event
        self.start_time = start_time
        self.end_time = end_time
        self.zip_code = zip_code
        self.city = city
        self.address = address
        self.available_beds = available_beds
        self.planned_donor_number = planned_donor_number
        self.final_donor_number = final_donor_number
