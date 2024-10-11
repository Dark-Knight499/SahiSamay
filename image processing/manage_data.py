import heapq
import timetable as tt
import json

n = -1

days = ["Monday: ", "Tuesday: ", "Wednesday: ", "Thursday: ", "Friday: ", "Saturday: "]

timeslots = [
    "8am - 8:30am",
    "8:30am - 9am",
    "9am - 9:30am",
    "9:30am - 10am",
    "10am - 10:30am",
    "10:30am - 11am",
    "11am - 11:30am",
    "11:30am - 12pm",
    "12pm - 12:30pm",
    "12:30pm - 1pm",
    "1pm - 1:30pm",
    "1:30pm - 2pm",
    "2pm - 2:30pm",
    "2:30pm - 3pm",
    "3pm - 3:30pm",
    "3:30pm - 4pm",
    "4pm - 4:30pm",
    "4:30pm - 5pm",
    "5pm - 5:30pm",
    "5:30pm - 6pm"
]



# class Person:
#     person_list = []
#
#     def __init__(self, name, timetable, dept, ipd_day, senior, id):
#         self.name = name
#         self.timetable = timetable
#         self.dept = dept
#         self.ipd_day = ipd_day
#         self.senior = senior
#         self.id = id
#         Person.person_list.append(self)
# def load_data():
#     global n
#     with open('database.json', 'r') as file:
#         data = json.load(file)
#     n = len(data) - 1
#     for i, j in enumerate(data):
#         Person(data[i]['name'], data[i]['timetable'], data[i]['dept'], data[i]['ipd_day'], data[i]['senior'], str(j))
def append_to_db(name, dept, img, senior=False):
    global n
    with open('database.json', 'r') as file:
        data = json.load(file)
    n += 1
    timetable = tt.get_tt(img)

    ipd_day = 0
    for i, j in enumerate(timetable):
        if i == "1"*20:
            ipd_day = j
            break

    data[str(n)] = {
        "name": name,
        "timetable": timetable,
        "dept": dept,
        "ipd_day": ipd_day,
        "senior": senior,
        "id": n
    }

    with open('database.json', 'w') as file:
        json.dump(data, file, indent=4)
    return timetable

def get_indexes(lst, value):
    indexes = []
    for i, v in enumerate(lst):
        if v == value:
            indexes.append(i)
    return indexes


def all_slots(tt_lists):
    slots = []
    no_of_people = len(tt_lists)
    for day in range(0, 6):
        for slot in range(0, 20):
            free_people = 0
            for person in range(0, no_of_people):
                if tt_lists[person][day][slot] == "0":
                    free_people += 1
            slots.append(free_people)
    return slots


def indices_to_slots(list_of_indices):
    global days, timeslots
    slots_in_words = []
    for i in list_of_indices:
        slot = []
        for j in i:
            s = days[j//20] + timeslots[j % 20]
            slot.append(s)
        slots_in_words.append(slot)
    return slots_in_words


# Accepts list of person class objs
def top_slots(tt_list):
    # ipd_day = set()
    # for obj in persons:
    #     ipd_day.add(obj.ipd_day)
    slots = all_slots(tt_list)
    top_5 = heapq.nlargest(5, slots)
    list_of_indices = []
    for i in top_5:
        index = get_indexes(slots, i)
        list_of_indices.append(index)
    # ignoring_ipd = list_of_indices
    # for i in list_of_indices:
    #     for j in i:
    #         if j//20 in ipd_day:
    #             i.remove(j)

    return indices_to_slots(list_of_indices)


# , indices_to_slots(ignoring_ipd)