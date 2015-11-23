class DonationObject(object):

    def __init__(self, name, date_of_event, start_time, end_time, zip_code, city, address, available_beds, \
                 planned_donor_number, event_duration_time, colon_in_duration_time, final_donor_number, \
                 success_rate, success_text):
        self.name = name
        self.date_of_event = date_of_event
        self.start_time = start_time
        self.end_time = end_time
        self.zip_code = zip_code
        self.city = city
        self.address = address
        self.available_beds = available_beds
        self.planned_donor_number = planned_donor_number
        self.event = event
        self.event_duration_time = event_duration_time
        self.colon_in_duration_time = colon_in_duration_time
        self.final_donor_number = final_donor_number
        self.success_rate = success_rate
        self.success_text = success_text
