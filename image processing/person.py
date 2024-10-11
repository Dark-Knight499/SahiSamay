import random
import manage_data
import timetable
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
    return timetable.get_tt(file_location) + ["0"*20]


