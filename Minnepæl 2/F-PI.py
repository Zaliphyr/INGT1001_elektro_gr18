# Hei og velkommen til F-Pi main
from sense_hat import SenseHat, ACTION_HELD, ACTION_RELEASED, ACTION_PRESSED
import time
import random

sense = SenseHat()
sense.set_rotation(270)

r = (0, 0, 0)               # road / black
g = (0, 255, 0)             # grass / green
o = (255, 0, 0)             # obstacle / red
c = (248, 231, 28)          # coin      / yellow
v = (48, 135, 145)          # vehicle   / turquoise

meny_pictures = {0: [
    (245, 66, 35), (245, 66, 35), (245, 103, 35), (245, 125, 35), (245, 125, 35), (245, 154, 35), (245, 176, 35), (245, 176, 35),
    (245, 66, 35), (245, 103, 35), (245, 125, 35), (245, 154, 35), (245, 176, 35), (245, 176, 35), (245, 213, 35), (250, 232, 31),
    (245, 103, 35), (245, 125, 35), (245, 125, 35), (245, 154, 35), (245, 176, 35), (245, 213, 35), (250, 232, 31), (255, 246, 162),
    (245, 103, 35), (245, 125, 35), (245, 125, 35), (245, 176, 35), (245, 176, 35), (250, 232, 31), (255, 246, 162), (255, 255, 255),
    (5, 47, 189), (5, 77, 224), (35, 118, 245), (35, 199, 245), (35, 199, 245), (35, 199, 245), (35, 199, 245), (35, 199, 245),
    (5, 77, 224), (35, 118, 245), (35, 177, 245), (35, 177, 245), (35, 177, 245), (35, 177, 245), (35, 177, 245), (35, 177, 245),
    (35, 118, 245), (35, 126, 245), (35, 111, 245), (35, 126, 245), (35, 126, 245), (35, 126, 245), (35, 126, 245), (35, 118, 245),
    (0, 101, 255), (0, 101, 255), (0, 101, 255), (0, 101, 255), (0, 101, 255), (0, 101, 255), (35, 118, 245), (5, 77, 224),
    ],
    1: [
        (0, 0, 0), (0, 0, 0), (255, 255, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 255, 255), (0, 0, 0),
        (0, 0, 0), (255, 255, 255), (0, 0, 0), (255, 255, 255), (0, 0, 0), (255, 255, 255), (0, 0, 0), (255, 255, 255),
        (0, 0, 0), (255, 255, 255), (0, 0, 0), (255, 255, 255), (0, 0, 0), (0, 0, 0), (255, 255, 255), (0, 0, 0),
        (0, 0, 0), (255, 255, 255), (208, 2, 27), (255, 255, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0),
        (0, 0, 0), (255, 255, 255), (208, 2, 27), (255, 255, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0),
        (255, 255, 255), (208, 2, 27), (208, 2, 27), (208, 2, 27), (255, 255, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0),
        (255, 255, 255), (208, 2, 27), (208, 2, 27), (208, 2, 27), (255, 255, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0),
        (0, 0, 0), (255, 255, 255), (255, 255, 255), (255, 255, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0),
    ],
    2: [
        (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0),
        (0, 0, 0), (0, 0, 0), (34, 52, 230), (34, 52, 230), (34, 52, 230), (34, 52, 230), (0, 0, 0), (0, 0, 0),
        (0, 0, 0), (34, 52, 230), (34, 52, 230), (34, 52, 230), (34, 52, 230), (34, 52, 230), (34, 52, 230), (0, 0, 0),
        (0, 0, 0), (34, 52, 230), (34, 52, 230), (34, 52, 230), (34, 52, 230), (34, 52, 230), (34, 52, 230), (0, 0, 0),
        (0, 0, 0), (34, 52, 230), (34, 52, 230), (34, 52, 230), (34, 52, 230), (34, 52, 230), (34, 52, 230), (0, 0, 0),
        (0, 0, 0), (0, 0, 0), (34, 52, 230), (34, 52, 230), (34, 52, 230), (34, 52, 230), (0, 0, 0), (0, 0, 0),
        (0, 0, 0), (0, 0, 0), (0, 0, 0), (34, 52, 230), (34, 52, 230), (0, 0, 0), (0, 0, 0), (0, 0, 0),
        (0, 0, 0), (0, 0, 0), (0, 0, 0), (34, 52, 230), (34, 52, 230), (0, 0, 0), (0, 0, 0), (0, 0, 0),
    ],
    3: [
        (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0),
        (0, 0, 0), (0, 0, 0), (248, 231, 28), (248, 231, 28), (248, 231, 28), (248, 231, 28), (0, 0, 0), (0, 0, 0),
        (0, 0, 0), (248, 231, 28), (0, 0, 0), (248, 231, 28), (248, 231, 28), (0, 0, 0), (248, 231, 28), (0, 0, 0),
        (0, 0, 0), (248, 231, 28), (248, 231, 28), (248, 231, 28), (248, 231, 28), (248, 231, 28), (248, 231, 28),
        (0, 0, 0),
        (0, 0, 0), (248, 231, 28), (0, 0, 0), (248, 231, 28), (248, 231, 28), (0, 0, 0), (248, 231, 28), (0, 0, 0),
        (0, 0, 0), (248, 231, 28), (248, 231, 28), (0, 0, 0), (0, 0, 0), (248, 231, 28), (248, 231, 28), (0, 0, 0),
        (0, 0, 0), (0, 0, 0), (248, 231, 28), (248, 231, 28), (248, 231, 28), (248, 231, 28), (0, 0, 0), (0, 0, 0),
        (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0),
    ],
    4: [
      (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0),
    (0, 255, 0), (0, 255, 0), (255, 0, 0), (255, 0, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0),
    (0, 255, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0),
    (255, 0, 0), (255, 0, 0), (0, 0, 255), (0, 255, 0), (255, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255),
    (255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 0, 255), (0, 255, 0), (255, 0, 0), (0, 0, 255), (0, 0, 255),
    (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 255, 0),
    (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 0, 255), (0, 0, 255), (0, 255, 0), (0, 255, 0),
    (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0), (0, 255, 0),
        ],
    5: [
      (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0),
    (0, 0, 0), (0, 0, 0), (208, 2, 27), (208, 2, 27), (208, 2, 27), (208, 2, 27), (0, 0, 0), (0, 0, 0),
    (0, 0, 0), (208, 2, 27), (208, 2, 27), (208, 2, 27), (208, 2, 27), (208, 2, 27), (208, 2, 27), (0, 0, 0),
    (208, 2, 27), (208, 2, 27), (208, 2, 27), (0, 0, 0), (0, 0, 0), (208, 2, 27), (208, 2, 27), (208, 2, 27),
    (255, 255, 255), (255, 255, 255), (0, 0, 0), (255, 255, 255), (255, 255, 255), (0, 0, 0), (255, 255, 255), (255, 255, 255),
    (255, 255, 255), (255, 255, 255), (255, 255, 255), (0, 0, 0), (0, 0, 0), (255, 255, 255), (255, 255, 255), (255, 255, 255),
    (0, 0, 0), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (0, 0, 0),
    (0, 0, 0), (0, 0, 0), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (0, 0, 0), (0, 0, 0),
     ],
    6: [
        (208, 2, 27), (208, 2, 27), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (208, 2, 27), (208, 2, 27),
        (208, 2, 27), (208, 2, 27), (208, 2, 27), (0, 0, 0), (0, 0, 0), (208, 2, 27), (208, 2, 27), (208, 2, 27),
        (0, 0, 0), (208, 2, 27), (208, 2, 27), (208, 2, 27), (208, 2, 27), (208, 2, 27), (208, 2, 27), (0, 0, 0),
        (0, 0, 0), (0, 0, 0), (208, 2, 27), (208, 2, 27), (208, 2, 27), (208, 2, 27), (0, 0, 0), (0, 0, 0),
        (0, 0, 0), (0, 0, 0), (208, 2, 27), (208, 2, 27), (208, 2, 27), (208, 2, 27), (0, 0, 0), (0, 0, 0),
        (0, 0, 0), (208, 2, 27), (208, 2, 27), (208, 2, 27), (208, 2, 27), (208, 2, 27), (208, 2, 27), (0, 0, 0),
        (208, 2, 27), (208, 2, 27), (208, 2, 27), (0, 0, 0), (0, 0, 0), (208, 2, 27), (208, 2, 27), (208, 2, 27),
        (208, 2, 27), (208, 2, 27), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (208, 2, 27), (208, 2, 27),
    ]
}
j_right_click = False
j_left_click = False
j_middle_click = False

def j_right(event):
    global j_right_click
    if event.action == ACTION_PRESSED:
        j_right_click = True


def j_left(event):
    global j_left_click
    if event.action == ACTION_PRESSED:
        j_left_click = True

def j_middle(event):
    global interrupt
    global j_middle_click
    if event.action == ACTION_PRESSED:
        j_middle_click = True
    elif event.action == ACTION_HELD:
        interrupt = True

def reset_buttons():
    global interrupt
    global j_middle_click
    global j_left_click
    global j_right_click
    interrupt = False
    j_middle_click = False
    j_left_click = False
    j_right_click = False

#example_map = [ [g, r, r, r, r, r, r, g],
#                [g, r, r, r, r, r, r, g],
#                [g, r, r, r, r, r, r, g],
#                [g, r, r, r, r, r, r, g],
#                [g, r, r, r, r, r, r, g],
#                [g, r, r, r, r, r, r, g],
#                [g, r, r, r, r, r, r, g],
#                [g, r, r, r, r, r, r, g],
#
#                [g, r, r, r, r, r, r, g],
#                [g, r, r, r, r, r, r, g],
#                [g, r, r, r, r, r, r, g],
#                [g, r, r, r, r, r, r, g],
#                [g, r, r, r, r, r, r, g],
#                [g, r, r, r, r, r, r, g],
#                [g, r, r, r, r, r, r, g],
#                [g, r, r, r, r, r, r, g]]


def car_pos_joy(prev_pos): # Function for the position of the car controlled by the joystick,
                           # with previous position as input shown by an integer between 0 and 7

    if j_left_click:
        position = prev_pos - 1
        reset_buttons()
    elif j_right_click:
        position = prev_pos + 1
        reset_buttons()
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
    p_map = map                     # Makes a copy of the inserted map
    p_map.pop(len(p_map)-1)         # Removes the bottom row
    p = []                          # Make one row of the map
    p.append(g)
    for j in range(6):
        p.append(r)
    p.append(g)
    p_map.insert(0, p)              # Inserts the new row at the top
    return p_map                    # Returns the new map

def obstacle(kart):                     # Function to create obstacle in each row
    obst = random.randint(1, 6)         # Random number
    kart[0][obst] = o                   # Changes the random element in the first row
    return kart                         # Returns map with obstacles

def obstacle3D(kart):                   # Function to reate obstacle every 3rd row
    count = 3                           # Counter
    if count % 3 == 0:                  # If counter is dividable by 3
        obst = random.randint(1, 6)     # Random number
        kart[0][obst] = o               # Changes the random element
    count += 1                          # Increases counter by 1
    return kart                         # Returns map with obstacles

def enable_screen(game_map, car_pos) :               # Function that sets pixels on sens hat
  road_screen = game_map[8:]     # Chooses the eight last lists of the list
  
  screen_pixels = []
  for e in road_screen :
    for pixel in e :
      screen_pixels.append(pixel)   # Adds all elements in from main map to screen_pixels (total of 64 elements)

  vehicle_pixel = 56 + car_pos      # Finds the last 8 elements, where the car will move horizontal
  screen_pixels[vehicle_pixel] = v  # Set the vehicle to life with posistion from vehicle function

  sense.set_pixels(screen_pixels)

def player_dead() :

  sun_down0 = [
      (245, 66, 35),  (245, 66, 35),  (245, 103, 35), (245, 125, 35), (245, 125, 35), (245, 154, 35), (245, 176, 35),   (245, 176, 35),
      (245, 66, 35),  (245, 103, 35), (245, 125, 35), (245, 154, 35), (245, 176, 35), (245, 176, 35), (245, 213, 35),   (250, 232, 31),
      (245, 103, 35), (245, 125, 35), (245, 125, 35), (245, 154, 35), (245, 176, 35), (245, 213, 35), (250, 232, 31),   (255, 246, 162),
      (245, 103, 35), (245, 125, 35), (245, 125, 35), (245, 176, 35), (245, 176, 35), (250, 232, 31), (255, 246, 162),  (255, 255, 255),
      g,              r,              r,              r,              r,              r,              r,                g,
      g,              r,              r,              r,              r,              r,              r,                g,
      g,              r,              r,              r,              r,              r,              r,                g,
      g,              r,              r,              r,              r,              r,              r,                g,
  ]
  
  sun_down1 = [
      (245, 66, 35),  (245, 66, 35),  (245, 103, 35), (245, 125, 35), (245, 125, 35), (245, 154, 35), (245, 176, 35),   (245, 176, 35),
      (245, 66, 35),  (245, 103, 35), (245, 125, 35), (245, 154, 35), (245, 176, 35), (245, 176, 35), (245, 213, 35),   (250, 232, 31),
      (245, 103, 35), (245, 125, 35), (245, 125, 35), (245, 154, 35), (245, 176, 35), (245, 213, 35), (250, 232, 31),   (255, 246, 162),
      (245, 103, 35), (245, 125, 35), (245, 125, 35), (245, 176, 35), (245, 176, 35), (250, 232, 31), (255, 246, 162),  (255, 255, 255),
      g,              r,              r,              r,              r,              r,              r,                g,
      g,              r,              r,              r,              r,              r,              r,                g,
      g,              r,              r,              r,              r,              r,              r,                g,
      g,              r,              r,              v,              v,              v,              r,                g,
  ]
  
  sun_down2 = [
      (245, 66, 35),  (245, 66, 35),  (245, 103, 35), (245, 125, 35), (245, 125, 35), (245, 154, 35), (245, 176, 35),   (245, 176, 35),
      (245, 66, 35),  (245, 103, 35), (245, 125, 35), (245, 154, 35), (245, 176, 35), (245, 176, 35), (245, 213, 35),   (250, 232, 31),
      (245, 103, 35), (245, 125, 35), (245, 125, 35), (245, 154, 35), (245, 176, 35), (245, 213, 35), (250, 232, 31),   (255, 246, 162),
      (245, 103, 35), (245, 125, 35), (245, 125, 35), (245, 176, 35), (245, 176, 35), (250, 232, 31), (255, 246, 162),  (255, 255, 255),
      g,              r,              r,              r,              r,              r,              r,                g,
      g,              r,              r,              r,              r,              r,              r,                g,
      g,              r,              r,              v,              v,              v,              r,                g,
      g,              r,              r,              v,              v,              v,              r,                g,
  ]
  
  sun_down3 = [
      (245, 66, 35),  (245, 66, 35),  (245, 103, 35), (245, 125, 35), (245, 125, 35), (245, 154, 35), (245, 176, 35),   (245, 176, 35),
      (245, 66, 35),  (245, 103, 35), (245, 125, 35), (245, 154, 35), (245, 176, 35), (245, 176, 35), (245, 213, 35),   (250, 232, 31),
      (245, 103, 35), (245, 125, 35), (245, 125, 35), (245, 154, 35), (245, 176, 35), (245, 213, 35), (250, 232, 31),   (255, 246, 162),
      (245, 103, 35), (245, 125, 35), (245, 125, 35), (245, 176, 35), (245, 176, 35), o,              (255, 246, 162),  (255, 255, 255),
      g,              r,              r,              r,              r,              r,              r,                g,
      g,              r,              r,              v,              v,              v,              r,                g,
      g,              r,              r,              v,              v,              v,              r,                g,
      g,              r,              r,              v,              v,              v,              r,                g,
  ]
  
  sun_down4 = [
      (245, 66, 35),  (245, 66, 35),  (245, 103, 35), (245, 125, 35), (245, 125, 35), (245, 154, 35), (245, 176, 35),   (245, 176, 35),
      (245, 66, 35),  (245, 103, 35), (245, 125, 35), (245, 154, 35), (245, 176, 35), (245, 176, 35), (245, 213, 35),   (250, 232, 31),
      (245, 103, 35), (245, 125, 35), (245, 125, 35), (245, 154, 35), (245, 176, 35), o,              (250, 232, 31),   (255, 246, 162),
      (245, 103, 35), (245, 125, 35), (245, 125, 35), (245, 176, 35), (245, 176, 35), o,              (255, 246, 162),  (255, 255, 255),
      g,              r,              r,              v,              v,              v,              r,                g,
      g,              r,              r,              v,              v,              v,              r,                g,
      g,              r,              r,              v,              v,              v,              r,                g,
      g,              r,              r,              r,              r,              r,              r,                g,
  ]
  
  sun_down5 = [
      (245, 66, 35),  (245, 66, 35),  (245, 103, 35), (245, 125, 35), (245, 125, 35), (245, 154, 35), (245, 176, 35),   (245, 176, 35),
      (245, 66, 35),  (245, 103, 35), (245, 125, 35), (245, 154, 35), (245, 176, 35), (245, 176, 35), (245, 213, 35),   (250, 232, 31),
      (245, 103, 35), (245, 125, 35), (245, 125, 35), (245, 154, 35), (245, 176, 35), o,              (250, 232, 31),   (255, 246, 162),
      (245, 103, 35), (245, 125, 35), (245, 125, 35), v,              v,              o,              (255, 246, 162),  (255, 255, 255),
      g,              r,              v,              v,              v,              o,              r,                g,
      g,              r,              v,              v,              r,              r,              r,                g,
      g,              r,              r,              r,              r,              r,              r,                g,
      g,              r,              r,              r,              r,              r,              r,                g,
  ]
  
  sun_down6 = [
      (245, 66, 35),  (245, 66, 35),  (245, 103, 35), (245, 125, 35), (245, 125, 35), (245, 154, 35), (245, 176, 35),   (245, 176, 35),
      (245, 66, 35),  (245, 103, 35), (245, 125, 35), (245, 154, 35), (245, 176, 35), (245, 176, 35), (245, 213, 35),   (250, 232, 31),
      (245, 103, 35), (245, 125, 35), v,              v,              v,              (245, 213, 35), (250, 232, 31),   (255, 246, 162),
      (245, 103, 35), (245, 125, 35), v,              v,              v,              o,              (255, 246, 162),  (255, 255, 255),
      g,              r,              r,              r,              r,              o,              r,                g,
      g,              r,              r,              r,              r,              o,              r,                g,
      g,              r,              r,              r,              r,              r,              r,                g,
      g,              r,              r,              r,              r,              r,              r,                g,
  ]
  
  sun_down7 = [
      (245, 66, 35),  (245, 66, 35),  (245, 103, 35), (245, 125, 35), (245, 125, 35), (245, 154, 35), (245, 176, 35),   (245, 176, 35),
      (245, 66, 35),  (245, 103, 35), v,              v,              (245, 176, 35), (245, 176, 35), (245, 213, 35),   (250, 232, 31),
      (245, 103, 35), (245, 125, 35), v,              v,              (245, 176, 35), (245, 213, 35), (250, 232, 31),   (255, 246, 162),
      (245, 103, 35), (245, 125, 35), (245, 125, 35), (245, 176, 35), (245, 176, 35), (250, 232, 31), (255, 246, 162),  (255, 255, 255),
      g,              r,              r,              r,              r,              o,              r,                g,
      g,              r,              r,              r,              r,              o,              r,                g,
      g,              r,              r,              r,              r,              o,              r,                g,
      g,              r,              r,              r,              r,              r,              r,                g,
  ]
  
  sun_down8 = [
      (245, 66, 35),  (245, 66, 35),  (245, 103, 35), (245, 125, 35), (245, 125, 35), (245, 154, 35), (245, 176, 35),   (245, 176, 35),
      (245, 66, 35),  v,              (245, 125, 35), (245, 154, 35), (245, 176, 35), (245, 176, 35), (245, 213, 35),   (250, 232, 31),
      (245, 103, 35), (245, 125, 35), v,              (245, 154, 35), (245, 176, 35), (245, 213, 35), (250, 232, 31),   (255, 246, 162),
      (245, 103, 35), (245, 125, 35), (245, 125, 35), (245, 176, 35), (245, 176, 35), (250, 232, 31), (255, 246, 162),  (255, 255, 255),
      g,              r,              r,              r,              r,              r,              r,                g,
      g,              r,              r,              r,              r,              o,              r,                g,
      g,              r,              r,              r,              r,              o,              r,                g,
      g,              r,              r,              r,              r,              o,              r,                g,
  ]
  
  sun_down9 = [
      (245, 66, 35),  (245, 66, 35),  (245, 103, 35), (245, 125, 35), (245, 125, 35), (245, 154, 35), (245, 176, 35),   (245, 176, 35),
      (245, 66, 35),  v,              (245, 125, 35), (245, 154, 35), (245, 176, 35), (245, 176, 35), (245, 213, 35),   (250, 232, 31),
      (245, 103, 35), (245, 125, 35), (245, 125, 35), (245, 154, 35), (245, 176, 35), (245, 213, 35), (250, 232, 31),   (255, 246, 162),
      (245, 103, 35), (245, 125, 35), (245, 125, 35), (245, 176, 35), (245, 176, 35), (250, 232, 31), (255, 246, 162),  (255, 255, 255),
      g,              r,              r,              r,              r,              r,              r,                g,
      g,              r,              r,              r,              r,              r,              r,                g,
      g,              r,              r,              r,              r,              o,              r,                g,
      g,              r,              r,              r,              r,              o,              r,                g,
  ]
  
  sun_down10 = [
      (245, 66, 35),  (245, 66, 35),  (245, 103, 35), (245, 125, 35), (245, 125, 35), (245, 154, 35), (245, 176, 35),   (245, 176, 35),
      (245, 66, 35),  (120, 169, 226),(245, 125, 35), (245, 154, 35), (245, 176, 35), (245, 176, 35), (245, 213, 35),   (250, 232, 31),
      (245, 103, 35), (245, 125, 35), (245, 125, 35), (245, 154, 35), (245, 176, 35), (245, 213, 35), (250, 232, 31),   (255, 246, 162),
      (245, 103, 35), (245, 125, 35), (245, 125, 35), (245, 176, 35), (245, 176, 35), (250, 232, 31), (255, 246, 162),  (255, 255, 255),
      g,              r,              r,              r,              r,              r,              r,                g,
      g,              r,              r,              r,              r,              r,              r,                g,
      g,              r,              r,              r,              r,              r,              r,                g,
      g,              r,              r,              r,              r,              o,              r,                g,
  ]
  
  sun_down11 = [
      (245, 66, 35),  (245, 66, 35),  (245, 103, 35), (245, 125, 35), (245, 125, 35), (245, 154, 35), (245, 176, 35),   (245, 176, 35),
      (245, 66, 35),  (182, 209, 240), (245, 125, 35), (245, 154, 35), (245, 176, 35), (245, 176, 35), (245, 213, 35),   (250, 232, 31),
      (245, 103, 35), (245, 125, 35), (245, 125, 35), (245, 154, 35), (245, 176, 35), (245, 213, 35), (250, 232, 31),   (255, 246, 162),
      (245, 103, 35), (245, 125, 35), (245, 125, 35), (245, 176, 35), (245, 176, 35), (250, 232, 31), (255, 246, 162),  (255, 255, 255),
      g,              r,              r,              r,              r,              r,              r,                g,
      g,              r,              r,              r,              r,              r,              r,                g,
      g,              r,              r,              r,              r,              r,              r,                g,
      g,              r,              r,              r,              r,              r,              r,                g,
  ]
  
  sun_down12 = [
      (245, 66, 35),  (245, 66, 35),  (245, 103, 35), (245, 125, 35), (245, 125, 35), (245, 154, 35), (245, 176, 35),   (245, 176, 35),
      (245, 66, 35),  (216, 231, 247), (245, 125, 35), (245, 154, 35), (245, 176, 35), (245, 176, 35), (245, 213, 35),   (250, 232, 31),
      (245, 103, 35), (245, 125, 35), (245, 125, 35), (245, 154, 35), (245, 176, 35), (245, 213, 35), (250, 232, 31),   (255, 246, 162),
      (245, 103, 35), (245, 125, 35), (245, 125, 35), (245, 176, 35), (245, 176, 35), (250, 232, 31), (255, 246, 162),  (255, 255, 255),
      g,              r,              r,              r,              r,              r,              r,                g,
      g,              r,              r,              r,              r,              r,              r,                g,
      g,              r,              r,              r,              r,              r,              r,                g,
      g,              r,              r,              r,              r,              r,              r,                g,
  ]
  
  sun_down13 = [
      (245, 66, 35),  (245, 66, 35),  (245, 103, 35), (245, 125, 35), (245, 125, 35), (245, 154, 35), (245, 176, 35),   (245, 176, 35),
      (245, 66, 35),  (255, 255, 255), (245, 125, 35), (245, 154, 35), (245, 176, 35), (245, 176, 35), (245, 213, 35),   (250, 232, 31),
      (245, 103, 35), (245, 125, 35), (245, 125, 35), (245, 154, 35), (245, 176, 35), (245, 213, 35), (250, 232, 31),   (255, 246, 162),
      (245, 103, 35), (245, 125, 35), (245, 125, 35), (245, 176, 35), (245, 176, 35), (250, 232, 31), (255, 246, 162),  (255, 255, 255),
      g,              r,              r,              r,              r,              r,              r,                g,
      g,              r,              r,              r,              r,              r,              r,                g,
      g,              r,              r,              r,              r,              r,              r,                g,
      g,              r,              r,              r,              r,              r,              r,                g,
  ]
  
  sun_down14 = [
      (245, 66, 35),  (255, 255, 255),(245, 103, 35), (245, 125, 35), (245, 125, 35), (245, 154, 35), (245, 176, 35),   (245, 176, 35),
      (255, 255, 255),(255, 255, 255),(255, 255, 255), (245, 154, 35), (245, 176, 35), (245, 176, 35), (245, 213, 35),   (250, 232, 31),
      (245, 103, 35), (255, 255, 255),(245, 125, 35), (245, 154, 35), (245, 176, 35), (245, 213, 35), (250, 232, 31),   (255, 246, 162),
      (245, 103, 35), (245, 125, 35), (245, 125, 35), (245, 176, 35), (245, 176, 35), (250, 232, 31), (255, 246, 162),  (255, 255, 255),
      g,              r,              r,              r,              r,              r,              r,                g,
      g,              r,              r,              r,              r,              r,              r,                g,
      g,              r,              r,              r,              r,              r,              r,                g,
      g,              r,              r,              r,              r,              r,              r,                g,
  ]
  
  sun_down15 = [
      (245, 66, 35),  (255, 255, 255),(245, 103, 35), (245, 125, 35), (245, 125, 35), (245, 154, 35), (245, 176, 35),   (245, 176, 35),
      (255, 255, 255),(255, 255, 255),(255, 255, 255), (255, 255, 255), (245, 176, 35), (245, 176, 35), (245, 213, 35),   (250, 232, 31),
      (245, 103, 35), (255, 255, 255),(245, 125, 35), (245, 154, 35), (245, 176, 35), (245, 213, 35), (250, 232, 31),   (255, 246, 162),
      (245, 103, 35), (245, 125, 35), (245, 125, 35), (245, 176, 35), (245, 176, 35), (250, 232, 31), (255, 246, 162),  (255, 255, 255),
      g,              r,              r,              r,              r,              r,              r,                g,
      g,              r,              r,              r,              r,              r,              r,                g,
      g,              r,              r,              r,              r,              r,              r,                g,
      g,              r,              r,              r,              r,              r,              r,                g,
  ]
  

  y = 0.08
  x = 0.15
  
  sense.set_pixels(sun_down0)
  time.sleep(.7)
  sense.set_pixels(sun_down1)
  time.sleep(x)
  sense.set_pixels(sun_down2)
  time.sleep(x)
  sense.set_pixels(sun_down3)
  time.sleep(.4)
  sense.set_pixels(sun_down4)
  time.sleep(.6)
  sense.set_pixels(sun_down5)
  time.sleep(.5)
  sense.set_pixels(sun_down6)
  time.sleep(x)
  sense.set_pixels(sun_down7)
  time.sleep(x)
  sense.set_pixels(sun_down8)
  time.sleep(x)
  sense.set_pixels(sun_down9)
  time.sleep(x)
  sense.set_pixels(sun_down10)
  time.sleep(x)
  sense.set_pixels(sun_down11)
  time.sleep(x)
  sense.set_pixels(sun_down12)
  time.sleep(x)
  sense.set_pixels(sun_down13)
  time.sleep(x)
  sense.set_pixels(sun_down14)
  time.sleep(y)
  sense.set_pixels(sun_down15)
  time.sleep(y)
  sense.set_pixels(sun_down14)
  time.sleep(y)
  sense.set_pixels(sun_down13)
  time.sleep(y)
  sense.set_pixels(sun_down0)
  time.sleep(y)


def map_collision(g_map, car_pos):
    collision = False
    point = False

    if (g_map[14][car_pos] == o):
        collision = True
    
    elif (g_map[14][car_pos] == c):
        point = True
        g_map[14][car_pos] = r
    
    return point, collision

def move_collision(g_map, car_pos):
    collision = False
    point = False

    if(g_map[15][car_pos] == o):
        collision = True
    elif(g_map[15][car_pos] == c):
        point = True
        g_map[15][car_pos] = r
    
    return point, collision


def transition(pic1, pic2, right):
  sleep_time = 0.05
  if right:
    state = []
    for i in range(1, 9):
      for j in range(8):
        for k in range(i, 8):
          state.append(pic1[(8*j)+k])
        for k in range(i):
          state.append(pic2[(8*j)+k])
      sense.set_pixels(state)
      time.sleep(sleep_time)
      state = []
  else:
    state = []
    for i in range(1, 9):
      for j in range(8):
        for k in range(8-i, 8):
          state.append(pic2[(8*j)+k])
        for k in range(8-i):
          state.append(pic1[(8*j)+k])
      sense.set_pixels(state)
      time.sleep(sleep_time)
      state = []


def run_game():
    game_map = map_creator()
    running = True
    coins = 0
    vehicle_pos = 5

    while running:
        for i in range(3):
            vehicle_pos = car_pos_joy(vehicle_pos)
            enable_screen(game_map, vehicle_pos)
            point, collision = move_collision(game_map, vehicle_pos)
            if collision:
                running = False
                break
            if point:
                coins += 1
            time.sleep(0.3)
        point, collision = map_collision(game_map, vehicle_pos)

        if collision:
            running = False

        if point:
            coins += 1
        
        game_map = obstacle(game_map)
        game_map = coin_placer(game_map)
        game_map = mov_map(game_map)
    return coins


def main():
    global j_right_click
    global j_left_click
    global j_middle_click
    meny_selection = 0
    meny_max = 1
    coins = 0

    sense.stick.direction_down = j_left
    sense.stick.direction_up = j_right
    sense.stick.direction_middle = j_middle

    while True:
        if j_right_click:
            reset_buttons()
            meny_selection += 1
            if meny_selection > meny_max:
                meny_selection = 0
                transition(meny_pictures[meny_max], meny_selection[0], True)
            else:
                transition(meny_pictures[meny_selection-1], meny_pictures[meny_selection], True)
        elif j_left_click:
            reset_buttons()
            meny_selection -= 1
            if meny_selection < 0:
                meny_selection = meny_max
                transition(meny_pictures[0], meny_pictures[meny_max], False)
            else:
                transition(meny_pictures[meny_selection+1], meny_pictures[meny_selection], False)
        elif j_middle_click:
            reset_buttons()
            if meny_selection == 0:
                coins = run_game()
                player_dead()
            elif meny_selection == 1:
                break

        sense.set_pixels(meny_pictures[meny_selection])
    sense.clear()
    print(coins)






if __name__ == "__main__":
    main()



