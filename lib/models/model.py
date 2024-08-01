import sqlite3
connection = sqlite3.connect("crm.db")
cursor = connection.cursor()
from faker.providers import BaseProvider
import random
import matplotlib.pyplot as plt


class Donor:
    all = []
    def __init__(self, name, state, id = None):
        self.id = id
        self.name = name
        self.state = state
        self.donor_donations = []
    
    #property of donor

    def get_name(self):
        return self._name
    def set_name(self, value):
        if type(value) is str and len(value) > 3:
            self._name = value
        else:
            raise ValueError("invalid name length")

    donor_name = property(get_name, set_name)

#getting a single donor by id

    @classmethod
    def get_one(cls,id):
        res = cursor.execute('SELECT * FROM donors WHERE id = ?', (id,))
        data = res.fetchone()
        print(data)
        donor = Donor(
                id = data[0],
                name = data[1],
                state= data[2]
            )
        return donor
# #deleting a donor by id 
    def delete_donor(self):
        cursor.execute(f'''
        DELETE FROM donors
        WHERE id = {self.id}
        ''')
        connection.commit()

#get all donors
    @classmethod
    def all(cls):
        res = cursor.execute("SELECT * FROM donors")
        data = res.fetchall()
        all_donors =[]
        for donor in data:
            donor = Donor(
                id = donor[0],
                name = donor[1],
                state= donor[2]
            )
            all_donors.append(donor)
        return all_donors

# posting/creating new donor
    def save_donor(self):
        res = cursor.execute('''
        INSERT INTO donors(name, state)
        VALUES(?,?);
        ''', (self.name, self.state))
        connection.commit()
        all = Donor.all()
        self.id = all[-1].id

       


# #updating/patch of existing donor here is test -- student.patch
    def patch_donor_name(self,name):
        cursor.execute('''
        UPDATE donors
        SET name = ?
        WHERE id = ?
        ''',(name,self.id))
        connection.commit()
        self.name = name

class Campaign:
    all = []
    def __init__(self, name, id = None):
        self.id = id
        self._name = name
        self.donations = []

#showing total donations for a specific campaign
    def total_donations(self):
        total = 0
        res_don = cursor.execute('SELECT amount FROM donations WHERE campaign_id = ?', (self.id,))
        for don in res_don.fetchall():
            total += don[0] 
        return total

    @classmethod
    def get_one(cls, id):
        cursor.execute('SELECT id, name FROM campaigns WHERE id = ?', (id,))
        row = cursor.fetchone()
        if row:
            return cls(id=row[0], name=row[1])
        else:
            return None

    #property of campaign

    def get_name(self):
        return self._name
    def set_name(self, value):
        if type(value) is str and len(value) > 3:
            self._name = value
        else:
            raise ValueError("invalid name length")

    campaign_name = property(get_name, set_name)

    #saving instances of a campaign

    def save_campaign(self):
        res = cursor.execute('''
        INSERT INTO campaigns(name)
        VALUES(?);
        ''', (self._name,))
        connection.commit()
        all = Campaign.all()
        self.id = all[-1].id

    @classmethod
    def all(cls):
        cursor.execute('SELECT * FROM campaigns')
        rows = cursor.fetchall()
        return [cls(*row) for row in rows]

#below are my methods for setting up mathplotlib

    def plot_total_donations_by_campaign():
        campaigns = []
        cursor.execute('SELECT id, name FROM campaigns')
        for row in cursor.fetchall():
            campaigns.append(Campaign(id=row[0], name=row[1]))

        campaign_names = [campaign._name for campaign in campaigns]
        total_donations = [campaign.total_donations() for campaign in campaigns]

        plt.figure(figsize=(10, 5))
        plt.bar(campaign_names, total_donations, color='blue')
        plt.xlabel('Campaign Name')
        plt.ylabel('Total Donations')
        plt.title('Total Donations by Campaign')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        plt.show()

class Donation:

    all = []
    def __init__(self, amount, donor_id, campaign_id, id = None,):
        self.id = id
        self._amount = amount
        self.donor_id = donor_id
        self.campaign_id= campaign_id
#saving/creating donations
    def save_donation(self):
        res = cursor.execute('''
        INSERT INTO donations(amount, donor_id, campaign_id)
        VALUES(?,?,?);
        ''', (self.amount, self.donor_id, self.campaign_id))
        connection.commit()
        all_donations = Donation.all()
        self.id = all_donations[-1].id

#getting all donations for using faker
    
    @classmethod
    def all(cls):
        cursor.execute('SELECT * FROM donations')
        rows = cursor.fetchall()
        return [cls(*row) for row in rows]
#getting all time donations
    @classmethod
    def total_donations(cls):
        res_don = cursor.execute('SELECT SUM(amount) FROM donations')
        total = res_don.fetchone()[0]
        return total if total is not None else 0
    
    @classmethod
    def avg_donations(cls):
        res_don = cursor.execute('SELECT AVG(amount) FROM donations')
        avg = res_don.fetchone()[0]
        return int(avg) if avg is not None else 0

    @classmethod
    def count_donations(cls):
        res_don = cursor.execute('SELECT COUNT(amount) FROM donations')
        count = res_don.fetchone()[0]
        return count if count is not None else 0

 #property of donation

    def get_amount(self):
        return self._amount
    def set_amount(self, value):
        if type(value) is int and len(value) > 1:
            self._amount = value
        else:
            raise ValueError("invalid amount")

    amount = property(get_amount, set_amount)


#created this class specifically to assign animal names as campaign names for faker

class AnimalProvider(BaseProvider):
    def animal(self):
        animals = [
            'cat', 'dog', 'horse', 'lion', 'tiger', 'bear', 'elephant', 'giraffe', 'zebra', 'kangaroo'
        ]
        return random.choice(animals)