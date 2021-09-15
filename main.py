class Rocket():
    def __init__(self, y_loc, x_loc):
        self.x_loc = x_loc
        self.y_loc = y_loc


    def move_rocket(self, move_y, move_x):
        self.x_loc += move_x
        self.y_loc += move_y

    def get_distance(self, rocket1_y, rocket2_y, rocket1_x, rocket2_x):
        self.y_dist = rocket1_y - rocket2_y
        self.x_dist = rocket1_x - rocket2_x

print("Rocket Distances")

rocketdist = Rocket(0,0)

rocketdist.get_distance(100,85,75,50)
print(rocketdist.y_dist, rocketdist.x_dist)

rocketdist = Rocket(0,0)

rocketdist.get_distance(150,85,50,0)
print(rocketdist.y_dist, rocketdist.x_dist)

rocketdist = Rocket(0,0)

rocketdist.get_distance(732,100,75,47)
print(rocketdist.y_dist, rocketdist.x_dist)

print()

print("Rocket Positions")

rocket1 = Rocket(0,0)

rocket1.move_rocket(100, 75)
print(rocket1.y_loc, rocket1.x_loc)

rocket2 = Rocket(0,0)

rocket2.move_rocket(85, 50)
print(rocket2.y_loc, rocket2.x_loc)

rocket3 = Rocket(0,0)

rocket3.move_rocket(150, 0)
print(rocket3.y_loc, rocket3.x_loc)

rocket4 = Rocket(0,0)

rocket4.move_rocket(50, 50)
print(rocket4.y_loc, rocket4.x_loc)

rocket5 = Rocket(0,0)

rocket5.move_rocket(732, 47)
print(rocket5.y_loc, rocket5.x_loc)