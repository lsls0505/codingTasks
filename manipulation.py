# Getting input from user
str_manip = input("Please input a string: ")

# Calculate and display the lenghth of str_manip
print(len(str_manip))
print(str_manip[-1])

# Find the last letter in str_manip and replace every occurence of this letter in str_manip with @
str_manip.replace(str_manip[-1], "@")
print(str_manip.replace(str_manip[-1], "@"))

# Create a five-letter word making up of the first three characters and last two characters in str_manip
print(str_manip[-1:-4:-1])
print((str_manip[0:3]) + (str_manip[-1:-3:-1][::-1]))