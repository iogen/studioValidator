with open('roster.txt', 'r') as file:
    person = "^("

    for line in file:
        id, fname, lname, wustlkey, e, classname, space, type, email = line.split(",")
        person = person + wustlkey + "|"

    person = person + ")$"

with open('validator.txt', 'w') as file:
    file.write(person)
