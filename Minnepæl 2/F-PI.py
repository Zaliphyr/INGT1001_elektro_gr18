# Hei og velkommen til F-Pi main
from sense_hat import SenseHat, ACTION_HELD, ACTION_RELEASED, ACTION_PRESSED
import time
import random
import csv
import os

def reset_sense():          # A function used to reset sense so that the gyroscope works properly
    global sense            # Accessing the global variable sense
    sense = SenseHat()      # This is the sense hat
    sense.set_rotation(270) # Selects correct led matrix rotation
reset_sense()

box_width = 120             # The max width for the text in the console, this is changable here
space = 10                  # Avalable lines for printing text

# Colors used on the map
r = (0, 0, 0)               # road / black
g = (0, 255, 0)             # grass / green
o = (255, 0, 0)             # obstacle / red
c = (248, 231, 28)          # coin      / yellow
v = (48, 135, 145)          # vehicle   / turquoise

# Pictures used for the menu
meny_pictures = {0: [
      (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0),
    (0, 0, 0), (0, 0, 0), (0, 0, 0), (76, 207, 26), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0),
    (0, 0, 0), (0, 0, 0), (0, 0, 0), (76, 207, 26), (76, 207, 26), (0, 0, 0), (0, 0, 0), (0, 0, 0),
    (0, 0, 0), (0, 0, 0), (0, 0, 0), (76, 207, 26), (76, 207, 26), (76, 207, 26), (0, 0, 0), (0, 0, 0),
    (0, 0, 0), (0, 0, 0), (0, 0, 0), (76, 207, 26), (76, 207, 26), (76, 207, 26), (0, 0, 0), (0, 0, 0),
    (0, 0, 0), (0, 0, 0), (0, 0, 0), (76, 207, 26), (76, 207, 26), (0, 0, 0), (0, 0, 0), (0, 0, 0),
    (0, 0, 0), (0, 0, 0), (0, 0, 0), (76, 207, 26), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0),
    (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0),
  ],
    1: [
      (0, 0, 0), (0, 0, 0), (0, 0, 0), (248, 231, 28), (248, 231, 28), (0, 0, 0), (0, 0, 0), (0, 0, 0),
    (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (248, 231, 28), (0, 0, 0), (0, 0, 0), (0, 0, 0),
    (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (248, 231, 28), (0, 0, 0), (0, 0, 0), (0, 0, 0),
    (255, 255, 255), (255, 255, 255), (255, 255, 255), (248, 231, 28), (248, 231, 28), (248, 231, 28), (223, 86, 23), (223, 86, 23),
    (0, 0, 0), (0, 0, 0), (255, 255, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (223, 86, 23),
    (255, 255, 255), (255, 255, 255), (255, 255, 255), (0, 0, 0), (0, 0, 0), (223, 86, 23), (223, 86, 23), (223, 86, 23),
    (255, 255, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (223, 86, 23),
    (255, 255, 255), (255, 255, 255), (255, 255, 255), (0, 0, 0), (0, 0, 0), (223, 86, 23), (223, 86, 23), (223, 86, 23),
  ],
    2: [
      (0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 255, 255), (255, 255, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0),
    (0, 0, 0), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (0, 0, 0),
    (0, 0, 0), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (0, 0, 0),
    (255, 255, 255), (255, 255, 255), (255, 255, 255), (0, 0, 0), (0, 0, 0), (255, 255, 255), (255, 255, 255), (255, 255, 255),
    (255, 255, 255), (255, 255, 255), (255, 255, 255), (0, 0, 0), (0, 0, 0), (255, 255, 255), (255, 255, 255), (255, 255, 255),
    (0, 0, 0), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (0, 0, 0),
    (0, 0, 0), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (0, 0, 0),
    (0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 255, 255), (255, 255, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0),
  ],
    3: [
      (208, 2, 27), (208, 2, 27), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (208, 2, 27), (208, 2, 27),
    (208, 2, 27), (208, 2, 27), (208, 2, 27), (0, 0, 0), (0, 0, 0), (208, 2, 27), (208, 2, 27), (208, 2, 27),
    (0, 0, 0), (208, 2, 27), (208, 2, 27), (208, 2, 27), (208, 2, 27), (208, 2, 27), (208, 2, 27), (0, 0, 0),
    (0, 0, 0), (0, 0, 0), (208, 2, 27), (208, 2, 27), (208, 2, 27), (208, 2, 27), (0, 0, 0), (0, 0, 0),
    (0, 0, 0), (0, 0, 0), (208, 2, 27), (208, 2, 27), (208, 2, 27), (208, 2, 27), (0, 0, 0), (0, 0, 0),
    (0, 0, 0), (208, 2, 27), (208, 2, 27), (208, 2, 27), (208, 2, 27), (208, 2, 27), (208, 2, 27), (0, 0, 0),
    (208, 2, 27), (208, 2, 27), (208, 2, 27), (0, 0, 0), (0, 0, 0), (208, 2, 27), (208, 2, 27), (208, 2, 27),
    (208, 2, 27), (208, 2, 27), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (208, 2, 27), (208, 2, 27),
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


car_text = [[   "Nissan Skyline GT-R R34 1999",
                "Farge: Lys grå",
                "2.6 L twin-turbocharged RB26DETT I6",
                "276 bhp @ 7000 rpm",
                "400 Nm",
                "AWD",
                "0-100: 4.9s",
                "Top Speed: 266 km/h"],

                ["Toyota Supra MK IV 1993",
                "Farge: Oransje",
                "3.0 L twin-turbocharged 2JZ-GTE I6",
                "276 bhp @ 5600 rpm",
                "434 Nm",
                "RWD",
                "0-100: 4.7s",
                "Top Speed: 285 km/h"],

                ["Dodge Charger R/T 1970",
                "Farge: Lilla",
                "7.0 L 426 HEMI V8",
                "425 bhp @ 5000 rpm",
                "665 Nm",
                "RWD",
                "0-100: 5.4s",
                "Top Speed: 211 km/h"],

                ["Ferrari F40 1987",
                "Farge: Rød",
                "2.9 L twin-turbocharged Tipo F120A V8",
                "471 bhp @ 7000 rpm",
                "578 Nm",
                "RWD",
                "0-100: 4.3s",
                "Top Speed: 327 km/h"],
                
                ["Postman Pat sin bil",
                "Farge: rød",
                "10.0L Quad-Turbocharged W24",
                "10000bhp @ 7000rpm",
                "12000Nm",
                "AWD",
                "0-100km/h: 0.6s",
                "Top Speed: 6600km/h (Mach 5.384)"],
                
                ["Subaru Impreza",
                "Farge: (5, 0, 255) - #0500FF",
                "2.0L Turbo 6MT B4",
                "261 hp @ 6000 rpm",
                "343Nm",
                "AWD",
                "0-100km/h: 5.5s",
                "Top Speed: 244km/h"],
                ["Mini 1000 Mk II 1976",
                "Farge: (205, 255, 0) - #CDFF00",
                "39 bhp @ 4750 rpm",
                "1.0L BMC Austin A-series 998",
                "0-100km/h: 19s",
                "70Nm",
                "FWD",
                "Top Speed: 130km/h"],
                
                ["DeLorean DMC-12",
                "Farge: (155, 155, 155) - #9B9B9B",
                "2.85L ZMJ-159 V6",
                "130bhp @ 5500 rpm",
                "207Nm",
                "RWD",
                "0-100km/h: 9.6s",
                "Top Speed: 209km/h"]]

# These become true when joy directions are pressed
j_right_click = False
j_left_click = False
j_middle_click = False
j_up_click = False
j_down_click = False

# Function bound to joy right
def j_right(event):
    global j_right_click
    if event.action == ACTION_PRESSED:
        j_right_click = True

# Function bound to joy left
def j_left(event):
    global j_left_click
    if event.action == ACTION_PRESSED:
        j_left_click = True

# Function bound to joy up
def j_up(event):
    global j_up_click
    if event.action == ACTION_PRESSED:
        j_up_click = True

# Function bound to joy down
def j_down(event):
    global j_down_click
    if event.action == ACTION_PRESSED:
        j_down_click = True

# Function bound to joy middle
def j_middle(event):
    global interrupt
    global j_middle_click
    if event.action == ACTION_PRESSED:
        j_middle_click = True
    elif event.action == ACTION_HELD:
        interrupt = True

# Needs to be runned after using a joy direction
def reset_buttons():
    global interrupt
    global j_middle_click
    global j_left_click
    global j_right_click
    global j_up_click
    global j_down_click
    interrupt = False
    j_middle_click = False
    j_left_click = False
    j_right_click = False
    j_up_click = False
    j_down_click = False

# Function to print the console header
def startingLines():
    print("╔" + ("═"*box_width) + "╗")
    print("║" + (" "*box_width) + "║")
    print("║" + "███████╗      ██████╗ ██╗".center(box_width, " ") + "║")
    print("║" + "██╔════╝      ██╔══██╗██║".center(box_width, " ") + "║")
    print("║" + "█████╗  █████╗██████╔╝██║".center(box_width, " ") + "║")
    print("║" + "██╔══╝  ╚════╝██╔═══╝ ██║".center(box_width, " ") + "║")
    print("║" + "██║           ██║     ██║".center(box_width, " ") + "║")
    print("║" + "╚═╝           ╚═╝     ╚═╝".center(box_width, " ") + "║")
    print("║" + (" "*box_width) + "║")
    print("║" + " ▀                                                                          ".center(box_width, " ") + "║")
    print("║" + "▄▀█ █▀█ █▀▀ ▀█▀ █▀   █▄▀ █ █ █   █▀▀ █▀ ▀█▀ █▀▀   █▄▄ █ █   █▀ █▀█ █ █   █  ".center(box_width, " ") + "║")
    print("║" + "█▀█ █▀▄ ██▄  █  ▄█   █ █ █▄█ █▄▄ ██▄ ▄█  █  ██▄   █▄█ █ █▄▄ ▄█ █▀▀ █ █▄▄ █▄▄".center(box_width, " ") + "║")
    print("║" + (" "*box_width) + "║")
    for i in range(space-1):
        print("║" + (" "*box_width) + "║")
    print("╚" + ("═"*box_width) + "╝")

# Function to send text to the screen
def update_screen(text_list):
    print("\033[F" * space, end="\x1b[1K\r")

    for i in text_list:
        print("║" + i.ljust(box_width) + "║")
    for i in range(space-(len(text_list)+1)):
        print("║" + (" "*box_width) + "║")
    print("╚" + ("═"*box_width) + "╝")

# Function for the position of the car controlled by the joystick,
def car_pos_joy(prev_pos):
                           # with previous position as input shown by an integer between 0 and 7

    if j_left_click:
        position = prev_pos - 1
        reset_buttons()
    elif j_right_click:
        position = prev_pos + 1
        reset_buttons()
    else:
        position = prev_pos

    if position < 1:        # The car can't go further to the left than 0, therefor if the position is negative:
        position = 1        # Set the position to 0
    elif position > 6:      # The car can't go further to the right than 7, therefor if the position is over 7:
        position = 6        # Set the position to 7
    
    return position

# Function for the position of the car controlled by gyroscope
def car_pos_gyro(prev_pos):
                            # with previous position as input shown by an integer between 0 and 7

    orientation = sense.get_gyroscope() # Collecting orientational data from sensehat
    yaw = orientation["yaw"] # Singling out the data for the yaw orientation
    if yaw >= 340 or yaw <= 20: # If the "wheel" of the car is almost flat:
        position = prev_pos # Keep the previous position
    elif 340 > yaw > 180: # If the "wheel" of the car is pointed to the left:
        position = prev_pos - 1 # Move the car one space to the left
    elif 20 < yaw < 180: # If the "wheel" of the car is pointed to the right:
        position = prev_pos + 1 # Move the car one space to the right
    else: # If the wheel is turned 180 degrees or the reading somehow gives another number:
        position = prev_pos # Keep the previous position


    if position < 1: # The car can't go further to the left than 1, therefor if the position is negative:
        position = 1 # Set the position to 1
    elif position > 6: # The car can't go further to the right than 6, therefor if the position is over 6:
        position = 6 # Set the position to 6

    return position # The function returns the value of the postition from 1 to 6

# Function to create an empty map
def map_creator():
    g_map = []
    for i in range(16):             # Map is 16 rows
        p = []
        p.append(g)                 # Add first bit of grass
        for j in range(6):          # Add 6 row pieces in the middle
            p.append(r)
        p.append(g)                 # Add last piece of grass
        g_map.append(p)
    return g_map                    # Returns the finished map

# Function that places a coin somwhere on the map
def coin_placer(g_map):
   
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

# Function to move the map
def mov_map(map):
    p_map = map                     # Makes a copy of the inserted map
    p_map.pop(len(p_map)-1)         # Removes the bottom row
    p = []                          # Make one row of the map
    p.append(g)
    for j in range(6):
        p.append(r)
    p.append(g)
    p_map.insert(0, p)              # Inserts the new row at the top
    return p_map                    # Returns the new map

# Function to create obstacle in each row
def obstacle(kart):
    obst = random.randint(1, 6)         # Random number
    kart[0][obst] = o                   # Changes the random element in the first row
    return kart                         # Returns map with obstacles

# Function to reate obstacle every 3rd row
def obstacle3D(kart):
    if o not in kart[1] and o not in kart[2]:   # If there is no obstacles in the 2nd and 3rd row
        obst = random.randint(1, 6)     # Random number
        kart[0][obst] = o               # Changes the random element in the first row
    return kart                         # Return map with obstacles with obstacles every 3rd row

# Function that sets pixels on sense hat
def enable_screen(game_map, car_pos):
  road_screen = game_map[8:]                         # Chooses the eight last lists of the list
  
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
  

def map_collision():                # Function to detect collision
    
    g_map = map_creator()           # Import map
    pos = bil_pos()                 # Import car position
    collision = False
    point = False

    if (g_map[14][pos] == g_map[14][o]):    # Detects collision if there is an obstacle in front of the car
        collision = True
    
    elif (g_map[14][pos] == g_map[14][c]):  # Detects points if a coin is in front of the car
        point = True
        g_map[14][car_pos] = r
    
    return point,collision                  # Returns point and collision

def scores_hat():

    scores = open("score_list.txt")                             # Open file with top scores
    sense.show_message("TOP 3", scroll_speed = 0.03)            # Scroll message saying TOP 3
    for i in range(3):                                          # Read the first three lines of the file and scroll them
        sense.show_message(scores.readline(), scroll_speed = 0.03)  
    scores.close()                                              # Close the file to avoid complications
     

def scores_console():

    scores = open("scores_list.txt")            # Open file with top scores
    
    scorelist = []                              # Create an empty list
    scorelist.append("Leaderboard")             # Add message Leaderboard to list
    for i in range(5):                    
        scorelist.append(scores.readline())     # Add the first 5 lines in the txt file to the list
    
    update_screen(scorelist)                    # Use update_screen function to display the top 5 scores in
                                                # the console
    scores.close()                              # Close the file to avoid complications



if __name__ == "__main__":
    main()



