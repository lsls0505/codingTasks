# Getting inputs from users
city_flight = input("Please enter the city you are flying to (a/b): ")
num_nights = int(input("Please enter the number of nights you will be staying at a hotel: "))
rental_days = int(input("Please enter the number of days you will be hiring a car: "))

# Total cost of hotel stay as the number of nights you will be staying at a hotel
def hotel_cost(num_nights): 
    total = 1 * num_nights
    return total 

# Total cost of flight as the city you are flying to
def plane_cost(city_flight): 
    plane_cost = 0 
    if city_flight == "a":
        plane_cost = 1
    elif city_flight == "b":
        plane_cost = 2
    return plane_cost
    
# Total cost of car rental as the number of rental days
def car_rental(rental_days):
    total = 1 * rental_days
    return total 
    
# Total cost of holiday
def holiday_cost(num_nights, city_flight, rental_days):
    total = hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days) 
    return total

result = holiday_cost(num_nights, city_flight, rental_days)
print("Total holiday cost is " + str(result))