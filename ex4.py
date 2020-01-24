# variable assignment to int 100
cars = 100
# variable assignment to float 4.0
space_in_a_car = 4.0
# variable assignment to int 30
drivers = 30
# variable assignment to int 90
passengers = 90
# variable assignment to int (cars - drivers)
cars_not_driven = cars - drivers
# variable assignment to int (drivers)
cars_driven = drivers
# variable assignment to float (cars_driven * space_in_a_car)
carpool_capacity = cars_driven * space_in_a_car
# variable assignment to float (passengers / cars_driven)
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
        "in each car.")
