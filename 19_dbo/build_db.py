import csv
import sqlite3

db = sqlite3.connect("foo")
c = db.cursor()
c.execute("CREATE TABLE students(name TEXT, age INTEGER, userid INTEGER)")
c.execute("CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER)")
with open('students.csv', newline = '') as csvfile:
    reader = csv.DictReader(csvfile)
    for line in reader:
        name = str(line['name'])
        age = int(line['age'])
        id = int(line['id'])
        print("INSERT INTO students (name, age, userid) " + f"VALUES ('{name}', {age}, {id})")
        c.execute("INSERT INTO students (name, age, userid) " + f"VALUES ('{name}', {age}, {id})")
        # c.execute("INSERT INTO roster(name) VALUES (?)", line['name'])
with open('courses.csv', newline = '') as csvfile:
    reader = csv.DictReader(csvfile)
    for line in reader:
        code = str(line['code'])
        mark = int(line['mark'])
        id = int(line['id'])
        print("INSERT INTO courses (code, mark, id) " + f"VALUES ('{code}', {mark}, {id})")
        c.execute("INSERT INTO courses (code, mark, id) " + f"VALUES ('{code}', {mark}, {id})")
db.commit()
db.close()
