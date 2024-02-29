sum = 0
count = 0
while True:
    number = (int(input()))
    if number == -1:
        break
    sum += number 
    count += 1
print(sum/count)
