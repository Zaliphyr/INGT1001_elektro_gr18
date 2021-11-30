# Hei og velkommen til F-Pi main
from sense_hat import SenseHat, ACTION_HELD, ACTION_RELEASED, ACTION_PRESSED
import time
import random

sense = SenseHat()

r = (0, 0, 0)               # road / black
g = (0, 255, 0)             # grass / green
o = (255, 0, 0)             # obstacle / red
c = (248, 231, 28)          # coin      / yellow
v = (48, 135, 145)          # vehicle   / turquoise


example_map = [ [g, r, r, r, r, r, r, g],
                [g, r, r, r, r, r, r, g],
                [g, r, r, r, r, r, r, g],
                [g, r, r, r, r, r, r, g],
                [g, r, r, r, r, r, r, g],
                [g, r, r, r, r, r, r, g],
                [g, r, r, r, r, r, r, g],
                [g, r, r, r, r, r, r, g],

                [g, r, r, r, r, r, r, g],
                [g, r, r, r, r, r, r, g],
                [g, r, r, r, r, r, r, g],
                [g, r, r, r, r, r, r, g],
                [g, r, r, r, r, r, r, g],
                [g, r, r, r, r, r, r, g],
                [g, r, r, r, r, r, r, g],
                [g, r, r, r, r, r, r, g]]


bil_pos = 0


def map_creator():                  # Function to create an empty map
    g_map = []
    for i in range(16):             # Map is 16 rows
        p = []
        p.append(g)                 # Add first bit of grass
        for j in range(6):          # Add 6 row pieces in the middle
            p.append(r)
        p.append(g)                 # Add last piece of grass
        g_map.append(p)
    return g_map                    # Returns the finished map




def coin_placer():                      # Function that places a coin somwhere on the map
    g_map = map_creator()

    obstacle = True
    while obstacle == True:             # The code will run as long as theres an obstacle where the coin is proposed to go        
        x = int(random.randint(1, 6))   # x is a random integer which corresponds to a pixel on the top row
        y = int(random.randint(0, 3))   # y is a random integer which defines how often a coin should be placed
        #print("y: ", y)
        coin_placement = g_map[0][x]    # Variable for which pixel to place the coin. Adds to first row 

        if o == coin_placement:         # Checks to see if theres an obstacle in where the coin should be placed
            obstacle = True
            #print("Oi! Her er det en hindring!")
        elif y == 1:                    # There's a 25% chance that y is 1, and then a coin will be placed
            g_map[0][x] = c             # Replaces the current index with a coin, and stops the while loop
            obstacle = False

            """
            print("Nytt kart:")
            for row in g_map:
                print(row)
            """
        else:
            #print("Ingen coin denne gangen.")
            break
    
    return g_map



def mov_map(map):                   # Function to move the map
    p_map = map.copy()              # Makes a copy of the inserted map
    p_map.pop(len(p_map)-1)         # Removes the bottom row
    p = []                          # Make one row of the map
    p.append(g)
    for j in range(6):
        p.append(r)
    p.append(g)
    p_map.insert(0, p)              # Inserts the new row at the top
    return p_map                    # Returns the new map

  
def obstacle(kart, score):          # Function to create obstacle in first row
    if score < 1000:                # Checking how high the score is
        obst = random.randint(1, 6) # Random number
        kart[0][obst] = o           # Changes the elements in the first row
    elif 1000 <= score < 2000:
        for i in range(2):
            obst = random.randint(1, 6)
            kart[0][obst] = o
    elif 2000 <= score < 3000:
        for i in range(3):
            obst = random.randint(1, 6)
            kart[0][obst] = o
    elif 3000 <= score < 4000:
        for i in range(4):
            obst = random.randint(1, 6)
            kart[0][obst] = o
    else:
        for i in range(5):
            obst = random.randint(1, 6)
            kart[0][obst] = o
    
    print(kart[0])
    return kart

obstacle(map_creator(), score)


def ENABLE_screen() :               # Function that sets pixels on sens hat

        # HUSK ENDRE \/
  road_screen = example_map[8:]     # Chooses the eight last lists of the list
  
  screen_pixels = []
  for e in road_screen :
    for pixel in e :
      screen_pixels.append(pixel)   # Adds all elements in from main map to screen_pixels (total of 64 elements)

  vehicle_pixel = 56 + bil_pos      # Finds the last 8 elements, where the car will move horizontal
  screen_pixels[vehicle_pixel] = v  # Set the vehicle to life with posistion from vehicle function

  sense.set_pixels(screen_pixels)

def main():
    pass

def map_collision():                # Function to detect collision
    
    g_map = map_creator()           # Import map
    pos = bil_pos()                 # Import car position
    collision = False
    point = False

    if (g_map[14][pos] == g_map[14][o]):    # Detects collision if there is an obstacle in front of the car
        collision = True
    
    elif (g_map[14][pos] == g_map[14][c]):  # Detects points if a coin is in front of the car
        point = True
    
    return point,collision                  # Returns point and collision





if __name__ == "__main__":
    main()



