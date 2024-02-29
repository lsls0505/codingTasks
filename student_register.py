# Getting input from user
students = int(input("How many students are registering? :"))
id_number = ""

for _ in range(0, students):
    id_number = input("Enter the next student ID number: ")
    with open('reg_form.txt', 'a') as f:
        f.write(str(f"{id_number}...\n"))

print("Student ID numbers are saved to text file reg_form.txt")