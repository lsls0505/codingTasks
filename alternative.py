# Getting input from user, generating alternative character in string using upper(), lower () and loop 
sentence = input("Please input a string: ")
result = ""
for index in range(len(sentence)):
        if index %2 ==0:
                result = result + sentence[index].upper()
        else:
                result = result + sentence[index].lower()
print("The alternate case string is : " + str(result))

# Getting input from user, generating alternative word in string using split(), join () and loop
sentence = input("Please enter a string: ").split()
result = " ".join([x.upper() if i % 2 else x.lower() for i, x in enumerate(sentence)])
print(result)