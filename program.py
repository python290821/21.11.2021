import sqlite3

class Employee:
    def __init__(self, id, name, age, address, salary):
        self.id = id
        self.name = name
        self.age = age
        self.address = address
        self.salary = salary

    def __repr__(self):
        return str(self.__dict__)

    def __str__(self):
        return str(self.__dict__)

# connect
conn = sqlite3.connect('mydb2.db')
print("connection to db opened")

# select
cursor = conn.execute("SELECT * FROM COMPANY")
cols = {desc[1][0]:desc[0] for desc in enumerate(cursor.description)}
print(cols) # nice

# run on select result and put rows in list
_emp = dict()
for row in cursor:
    e = Employee(row[cols['ID']], row[cols['NAME']],
                 row[cols['AGE']], row[cols['ADDRESS']],
                 row[cols['SALARY']])
    _emp[row[cols['ID']]] = e
print(_emp)
print(_emp[3]) # print by id

