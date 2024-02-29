# Getting inputs from users
swimming = int(input("Please enter your swimming time: "))
cycling = int(input("Please enter your cycling time: "))
running = int(input("Please enter your running time: "))

# Number is the sum of all input
number = swimming + cycling + running

# Determining the award by number
if number <= 100:
    print("Provincial Colours")
elif (number >= 101) and (number <= 105):
    print("Provincial Half Colours")
elif (number >= 106) and (number <= 110):
    print("Provincial Scroll")
else:
    print("No award")