CREATE TABLE IF NOT EXISTS BloodDonationStorage.Event (
id INTEGER NOT NULL auto_increment,
date_of_event DATE NOT NULL,
start_time TIME NOT NULL,
end_time TIME NOT NULL,
zip_code VARCHAR(4) NOT NULL,
city VARCHAR(30) NOT NULL,
address VARCHAR(25) NOT NULL,
number_of_available_beds VARCHAR(8) NOT NULL,
planned_donor_number VARCHAR(10) NOT NULL,
final_donor_number VARCHAR(10) NOT NULL,
PRIMARY KEY (id)
) ENGINE = MyISAM;