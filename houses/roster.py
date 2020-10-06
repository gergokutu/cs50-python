# TODO
from cs50 import SQL
from sys import argv

# check command line arguments
if len(argv) < 2:
    print("usage error, roster.py houseName")
    exit()

# open the db and execute the query
db = SQL("sqlite:///students.db")
students = db.execute("SELECT * FROM students WHERE house = (?) ORDER BY last", argv[1])

# print each person with birth year
for student in students:
    if student['middle'] != None:
        print(f"{student['first']} {student['middle']} {student['last']}, born {student['birth']}")
    else:
        print(f"{student['first']} {student['last']}, born {student['birth']}")