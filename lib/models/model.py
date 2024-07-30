import sqlite3
connection = sqlite3.connect("crm.db")
cursor = connection.cursor()

# class Student:
#     def __init__(self,name,emergency_phone, id=None):
#         self.id = id
#         self.name = name
#         self.emergency_phone = emergency_phone
    
#     # Post
#     def save_student(self):
#         res = cursor.execute('''
#         INSERT INTO students(name,emergency_phone)
#         VALUES(?,?);
#         ''', (self.name,self.emergency_phone))
#         # cursor.execute('''
#         # INSERT INTO students(name,emergency_phone)
#         # VALUES("{self.name}",{self.emergency_phone});
#         # ''')
#         connection.commit()
#         all = Student.all()
#         self.id = all[-1].id

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

#return of all donations for a specific donor

    def total_donations(self):
        total = 0
        res_don = cursor.execute('SELECT amount FROM donations WHERE donor_id = ?', (self.id,))
        for don in res_don.fetchall():
            total += don[0] 
        return total

    def average_donation(self):
        res_don = cursor.execute('SELECT AVG(amount) FROM donations WHERE donor_id = ?', (self.id,))
        avg = res_don.fetchone()[0]
        return int(avg) if avg is not None else 0

    @classmethod
    def get_one(cls,id):
        res = cursor.execute(f"SELECT * FROM donors WHERE id = {id};")
        data = res.fetchone()
        print(data)
        donor = Donor(
                id = data[0],
                name = data[1],
                state= data[2]
            )
        return donor
# #deleting a donor by id (remove schedules, since we're only doing students) and here is test-- my_teach.delete()
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

       
        # Donor.save_donor()
        # all.append(donor)

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
    def get_one(cls,id):
        res = cursor.execute(f"SELECT * FROM campaigns WHERE id = {id};")
        data = res.fetchone()
        print(data)
        campaign = Campaign(
                id = data[0],
                name = data[1]
            )
        return campaign

    #property of campaign

    def get_name(self):
        return self._name
    def set_name(self, value):
        if type(value) is str and len(value) > 3:
            self._name = value
        else:
            raise ValueError("invalid name length")

    campaign_name = property(get_name, set_name)

class Donation:
    all_donations = []
    def __init__(self, amount, id = None,):
        self.id = id
        self._amount = amount

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

    #might not neeeeedddd below


    # def get_one(donation_id):
    #     result = cursor.execute('SELECT * FROM donations WHERE id = ?', (donation_id,))
    #     data = result.fetchone()
    #     if data:
    #         return Donation(id=data[0], amount=data[1])
    #     else:
    #         return None