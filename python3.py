cars=100
spaceInCars=4.0
drivers = 30
passenger = 30 
carsNotDrive = cars - drivers
carDriven=drivers
carpoolCapacity = carDriven * spaceInCars
avgPassCar = passenger /carDriven


print "There are  " , cars, "cars available "
print "There are only ", drivers ,"drivers available"
print "There will be ", carsNotDrive ,"Empty cars today"
print "WE can transport ", carpoolCapacity,"People Today "
print "we Have " , passenger,"to carpool today"
print "we need to put about ",avgPassCar,"in each car" 
print 