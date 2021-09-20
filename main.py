import math

class Rocket():
    def __init__(self, y_loc, x_loc):
        self.x_loc = x_loc
        self.y_loc = y_loc

    def move_rocket(self, move_y, move_x):
        self.x_loc += move_x
        self.y_loc += move_y

    def get_distance(self, rocket1_y,rocket1_x):
        y_dist = (rocket1_y - self.y_loc)**2
        x_dist = (rocket1_x - self.x_loc)**2
        dist = math.sqrt(x_dist+y_dist)
        return dist

print("Rocket Distances")

rocketdist = Rocket(0,0)

newdist = rocketdist.get_distance(0,100)
print(newdist)


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

    def get_distance(self, rocket1_x,rocket1_y):
        y_dist = (rocket1_y - self.y_loc)**2
        x_dist = (rocket1_x - self.x_loc)**2
        dist = math.sqrt(x_dist+y_dist)
        return dist

    def safety_check(self,rocketx,rockety):
        current_dist = self.get_distance(rocketx,rockety)
        if current_dist < 50:
            print("Rockets are too close")
        else:
            print("Rockets at safe distance")


rocket4 = Rocket(0,0)

rocket5 = Rocket(0,100)

rocket4.safety_check(rocket5.x_pos,rocket5.y_pos)