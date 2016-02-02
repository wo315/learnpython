cars = 100 # how many cars
space_in_a_car = 4 # How many people in a car
drivers = 30  # How many drivers
passengers = 90 # How many passengers
cars_not_driven = cars - drivers # These cars can not drive for no drivers
cars_driven = drivers # per drivers per car 
carpool_capacity = cars_driven * space_in_a_car # total passengers can be delivered
average_passengers_per_car = passengers / cars_driven # How many passengers can be in a car

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today." 
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

