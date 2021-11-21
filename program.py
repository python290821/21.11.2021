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
# cols = [desc[0] for desc in cursor.description]
# print(cols)

# run on select result and put rows in list
_emp = []
for row in cursor:
    e = Employee(row[0], row[1], row[2], row[3], row[4])
    _emp.append(e)
print(_emp)

