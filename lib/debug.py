#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
# import ipdb
from models.model import Donor
from models.model import Campaign
from models.model import Donation



# ipdb.set_trace()

if __name__ == '__main__':

    donor1 = Donor(name = "Timothy Magee", state= "WA", id= 3)
    donor2 = Donor("Wyatt John", "NV")
    donor = Donor(name="Wyatt John", state="NV", id=4)
    donor3 =Donor(name = "Megan Riley", state= "OH", id= 4)

    # Donor.get_one(1)
    # donor1.save_donor()
    # donor3.save_donor()
    # donor.delete_donor()
    # donor1.patch_donor_name("Tim")

#     campaign = Campaign(name="Meow 123")
#     print(campaign.campaign_name)

# print(donor.donations)
# campaign = Campaign(name="Frog", id=1)

# avg_donations = campaign.total_donations()




total_donations = Donation.total_donations()

print(total_donations)

# print(campaign.campaign_name) 
# try:
#     campaign.campaign_name = "AE"  # Name too short
# except ValueError as e:
#     print(e)
 
