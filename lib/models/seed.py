# with open('seeds.sql', 'r') as sql_file:
#     sql_script = sql_file.read()
# # Then we can use execute script to run it
# cursor.executescript(sql_script)
# # Don't forget the commit
# connection.commit()
from model import *
from faker import Faker
from faker.providers import BaseProvider
import random

faker = Faker()
fake = Faker()
fake.add_provider(AnimalProvider)
with open('lib/models/seeds.sql', 'r') as sql_file:
    sql_script = sql_file.read()
# Then we can use execute script to run it
cursor.executescript(sql_script)
# Don't forget the commit
connection.commit()


print("Creating donors")
all_donors = []
for i in range(47):
    donor = Donor(
        name = faker.name(),
        state = faker.state_abbr()
    )
    donor.save_donor()
    all_donors.append(donor)

print("Creating donations")
all_donations = []
for i in range(200):
    donation = Donation(
        amount = random.randint(100,10000),
        donor_id = random.randint(4,50),
        campaign_id = random.randint(1,10)
    )
    donation.save_donation()
    all_donations.append(donation)

print("Creating campaigns")
all_campaigns = []
for i in range(10):
    campaign = Campaign(
        name = fake.animal(),
    )
    campaign.save_campaign()
    all_campaigns.append(donation)


    from faker import Faker
from faker.providers import BaseProvider
import random

# Custom provider for animals
class AnimalProvider(BaseProvider):
    def animal(self):
        animals = [
            'cat', 'dog', 'horse', 'lion', 'tiger', 'bear', 'elephant', 'giraffe', 'zebra', 'kangaroo'
        ]
        return random.choice(animals)

# Initialize Faker and add the custom provider
fake = Faker()
fake.add_provider(AnimalProvider)

# Define Campaign class
class Campaign:
    all = []
    
    def __init__(self, name, id=None):
        self.id = id
        self._name = name
        self.donations = []
    
    def save_campaign(self):
        Campaign.all.append(self)

# Creating campaigns
print("Creating campaigns")
all_campaigns = []
for i in range(10):
    campaign = Campaign(
        name=fake.animal(),  # Use the custom animal provider
    )
    campaign.save_campaign()
    all_campaigns.append(campaign)  # Append campaign instead of donation

# Print created campaigns
for campaign in all_campaigns:
    print(f"Campaign Name: {campaign._name}, ID: {campaign.id}")
