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


def car_pos_joy(prev_pos): # Function for the position of the car controlled by the joystick,
                           # with previous position as input shown by an integer between 0 and 7
    from sense_hat import SenseHat # Importing SenseHat from sense_hat library
    sense = SenseHat()
    event = sense.stick.wait_for_event() # Henter data fra joystick
    joy_input = event[1]

    if joy_input == "down":
        position = prev_pos - 1
    elif joy_input == "up":
        position = prev_pos + 1
    else:
        position = prev_pos

    if position < 0: # The car can't go further to the left than 0, therefor if the position is negative:
        position = 0 # Set the position to 0
    elif position > 7: # The car can't go further to the right than 7, therefor if the position is over 7:
        position = 7 # Set the position to 7
    
    return position


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


def coin_placer(g_map):                      # Function that places a coin somwhere on the map
   
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


def enable_screen(game_map, car_pos) :               # Function that sets pixels on sens hat
  road_screen = game_map.copy()
  road_screen = road_screen[8:]     # Chooses the eight last lists of the list
  
  screen_pixels = []
  for e in road_screen :
    for pixel in e :
      screen_pixels.append(pixel)   # Adds all elements in from main map to screen_pixels (total of 64 elements)

  vehicle_pixel = 56 + car_pos      # Finds the last 8 elements, where the car will move horizontal
  screen_pixels[vehicle_pixel] = v  # Set the vehicle to life with posistion from vehicle function

  sense.set_pixels(screen_pixels)


def map_collision(g_map, car_pos):
    collision = False
    point = False

    if (g_map[14][car_pos] == o):
        collision = True
    
    elif (g_map[14][car_pos] == c):
        point = True
    
    return point, collision


def main():
    game_map = map_creator()
    running = True
    coins = 0
    vehicle_pos = 5

    while running:
        enable_screen(game_map, vehicle_pos)
        point, collision = map_collision(game_map, vehicle_pos)

        if collision:
            running = False

        if point:
            coins += 1
        
        game_map = obstacle(game_map, coins)
        game_map = coin_placer(game_map)
        game_map = mov_map(game_map)






if __name__ == "__main__":
    main()



