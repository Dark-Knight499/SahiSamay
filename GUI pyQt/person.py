import random
# person.py
class Person:
    person_list = []

    def __init__(self):
        self.name = None
        self.dept = None
        self.year = None
        self.timetable = []
        Person.person_list.append(self)

def getTimeTable(file_location):
    return ["00000000000000000000"] * 7  

