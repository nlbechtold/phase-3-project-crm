

class Donor:
    all = []
    def __init__(self, id = None, name, state):
        self.id = id
        self.name = name
        self.state = state
        self.donations = []
    
    #property of donor

    def get_name(self):
        return self._name
    def set_name(self, value):
        if type(value) is string and len(value)>3
            self._name = value
        else:
            raise ValueError("invalid name length")

    donor_name = property(get_name, set_name)

#methods of donor, to get a donor by id input
# testing-# my_teach= Teacher.get_one(3)

    @classmethod
    def get_one(cls,id):
        res = cursor.execute(f"SELECT * FROM students WHERE id = {id};")
        data = res.fetchone()
        st = Student(
                id = data[0],
                name = data[1],
                emergency_phone= data[2]
            )
        return st
#deleting a donor by id (remove schedules, since we're only doing students)
    def delete(self):
        cursor.execute(f'''
        DELETE FROM students
        WHERE id = {self.id}
        ''')
        cursor.execute(f'''
        DELETE FROM schedules
        WHERE student_id = {self.id}
        ''')
        connection.commit()

class Donation:
    all = []
    def __init__(self, id = None, amount):
        self.id = id
        self.amount = amount
    
    #property of donation

    def get_amount(self):
        return self._amount
    def set_amount(self, value):
        if type(value) is int and len(value)>1
            self._amount = value
        else:
            raise ValueError("invalid amount")

    amount = property(get_amount, set_amount)

    


class Campaign:
    all = []
    def __init__(self, id = None, name):
        self.id = id
        self.name = name
        self.donations = []
    
    #property of campaign

        def get_name(self):
        return self._name
    def set_name(self, value):
        if type(value) is string and len(value)>3
            self._name = value
        else:
            raise ValueError("invalid name length")

    campaign_name = property(get_name, set_name)