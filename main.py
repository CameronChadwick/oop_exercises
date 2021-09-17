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

rocket = Rocket(0,0)

rocket.move_rocket(100, 75)
print(rocket.y_loc, rocket.x_loc)

rocket = Rocket(0,0)

rocket.move_rocket(85, 50)
print(rocket.y_loc, rocket.x_loc)

rocket = Rocket(0,0)

rocket.move_rocket(150, 0)
print(rocket.y_loc, rocket.x_loc)

rocket = Rocket(0,0)

rocket.move_rocket(50, 50)
print(rocket.y_loc, rocket.x_loc)

rocket = Rocket(0,0)

rocket.move_rocket(732, 47)
print(rocket.y_loc, rocket.x_loc)

print()
print("Rocket Attributes")

class Rocket():
    def __init__(self,height,crewsize,name):
        self.height = height
        self.crewsize = crewsize
        self.name = name

    def disttraveled(self,move_up):
        self.height += move_up

rocket2 = Rocket(0,5,"High Flyer")

rocket2.disttraveled(236)
print("Name",rocket2.name,"\nAltitude",rocket2.height,"\nCrew",rocket2.crewsize)

print()

rocket2 = Rocket(0,3,"Sky High")

rocket2.disttraveled(568)
print("Name",rocket2.name,"\nAltitude",rocket2.height,"\nCrew",rocket2.crewsize)

print()

rocket2 = Rocket(0,6,"Moon Bound")

rocket2.disttraveled(362)
print("Name",rocket2.name,"\nAltitude",rocket2.height,"\nCrew",rocket2.crewsize)

print()
print("Rocket Methods")

class Rocket():
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos

    def launch(self):
        print("We have liftoff!")

    def travel(self, x_move, y_move):
        self.x_pos += x_move
        self.y_pos += y_move

    def land_rocket(self):
        print("Touchdown in 5 4 3 2 1")
        self.x_pos = 0
        self.y_pos = 0


rocket3 = Rocket(0,0)

rocket3.launch()
rocket3.travel(247,7378)
print(rocket3.x_pos, rocket3.y_pos)

print()

rocket3.land_rocket()
print(rocket3.x_pos, rocket3.y_pos)
