#To separate names and birthdate into two different sections
names = []
birthdate = []

f = open("DOB.txt", "r")
data = f.readlines()

for line in data:
        parts = line.split()
        names.append(parts[:2])  
        birthdate.append(parts[2:])  

f.close()

print("names")
for i, names in enumerate(names, start=1):
        print("{}. {}".format(i, " ".join(names)))

print("birthdate")
for i, birthdate in enumerate(birthdate, start=1):
        print("{}. {}".format(i, " ".join(birthdate)))