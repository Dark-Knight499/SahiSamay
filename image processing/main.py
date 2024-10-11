import manage_data

# manage_data.load_data()

t1 = manage_data.append_to_db("Vaibhav", "Coding", "./image/C1.png")
t2 = manage_data.append_to_db("Harsh", "Coding", "./image/C2.png")
t3 = manage_data.append_to_db("Om", "Coding", "./image/C3.png", True)

topslots = manage_data.top_slots([t1, t2, t3])

print("Without IPD")
for i in topslots[0]:
    print(i)

print("With IPD")
for i in topslots[1]:
    for j in i:
        print(j)
