CREATE TABLE IF NOT EXISTS BloodDonationStorage.Donor (
name VARCHAR(80) NOT NULL,
weight VARCHAR(3) NOT NULL,
gender VARCHAR(6) NOT NULL,
date_of_birth DATE NOT NULL,
last_donation DATE,
last_month_sickness VARCHAR(3) NOT NULL,
unique_identifier VARCHAR(8) NOT NULL,
expiration_of_id DATE NOT NULL,
blood_type VARCHAR(3) NOT NULL,
hemoglobin VARCHAR(3) NOT NULL,
email VARCHAR(80) NOT NULL,
mobil VARCHAR(12) NOT NULL,
is_suitable VARCHAR(3) NOT NULL,
PRIMARY KEY (unique_identifier)
) ENGINE = MyISAM;