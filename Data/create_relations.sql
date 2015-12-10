CREATE TABLE IF NOT EXISTS BloodDonationStorage.Donor_Event_relation (
id INTEGER NOT NULL auto_increment,
donor_id INTEGER NOT NULL,
event_id INTEGER NOT NULL,
PRIMARY KEY (id),
CONSTRAINT donor_foreign FOREIGN KEY (donor_id) REFERENCES Donor(unique_identifier),
CONSTRAINT event_foreign FOREIGN KEY (event_id) REFERENCES Event(id)
) ENGINE = MyISAM;