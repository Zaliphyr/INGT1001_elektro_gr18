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
    print("╚" + ("═"*box_width) + "╝")
    for i in range(space-1):                # Prints the empty lines reserved for text
        print(" " * (box_width+2))

# Function to send text to the screen
def update_screen(text_list):
    print("\033[F" * space, end="\x1b[1K\r")

    for i in text_list:
        print("║" + i.ljust(box_width) + "║")
    print("╚" + ("═"*box_width) + "╝")
    for i in range(space-(len(text_list)+1)):
        print(" " * (box_width+2))


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

    if position < 1:        # The car can't go further to the left than 0, therefor if the position is negative:
        position = 1        # Set the position to 0
    elif position > 6:      # The car can't go further to the right than 7, therefor if the position is over 7:
        position = 6        # Set the position to 7
    
    return position

def car_pos_gyro(prev_pos): # Function for the position of the car controlled by gyroscope,
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
    
    return kart


def enable_screen(game_map, car_pos) :               # Function that sets pixels on sense hat
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

def choose_name() :
    name = ""
    name_list = []
    alfab = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    white = (255, 255, 255)
    black = (0, 0, 0)
    green = (0, 77, 26)
    
    
    
    x = 0
    while len(name_list) < 3 :
        sense.show_letter(alfab[x], text_colour=white, back_colour=black)
      
        if j_up_click :
            reset_buttons()
            x -= 1
        elif j_down_click:
            reset_buttons()
            x += 1
        elif j_middle_click:
            reset_buttons()
            name_list.append(alfab[x])
            sense.show_letter(alfab[x], text_colour=(0, 255, 0), back_colour=black)
            time.sleep(0.2)
            x = 0
    
    for e in name_list :
      name += e
    
    
    time.sleep(0.2)
    sense.show_message(name, text_colour=(0, 255, 0), back_colour=black)
    
    return name

def update_csv(name, coins) :                                               # Function that updates an already created file
    list_names = []
    with open('SCOREBOARD_FPI.csv', newline='') as f:
        file_content = csv.reader(f, delimiter=' ', quotechar='|')          # Opens the .csv file and reads all lines:
        for player in file_content :                                        # like this ["name", "coins"]
            for i, v in enumerate(player) :                                 #           ["ABC", "13"] ...
               list_names.append(v)                                         # Adds all list into one list ["name", "coins", "ABC", "13"] ..
    
    player_exist = False
    for e in list_names :                                                   # Iterates over the created list (list_names)
        if e == name :                                                      # to see if the name already exists
            player_exist = True                                             # using the Booelen variable player_exist
        
            
    if player_exist :
        new_record = False      
        for i, v in enumerate(list_names) :
            if v == name :                                                  # Updates the one player that aldreay exists and
                if int(list_names[i+1]) >= int(coins) :
                  pass
                else :
                  new_record = True
                  list_names[i + 1] = str(coins)                              # gives it a new record (coins)
        with open('SCOREBOARD_FPI.csv', "w") as f:                          # Overwrites the current file
            for i, v in enumerate(list_names) :                             
                if i % 2 == 0 :
                    f.write("%s %s\n"% (list_names[i], list_names[i + 1]))  # and adds all the players from list_names
        if new_record :
          print("Player", name, "updated ->", coins, "coins")
        else :
          print("Player", name, ", not new record")                                            # with updated scores

    else :    
        
        with open('SCOREBOARD_FPI.csv', "a") as f:                          # If the name chosen does not already exist
            f.write("%s %s\n"% (name, player_scoreboard[name]))             # the aldreay created file gets appended with the new name and its score (coins)
        print("Player", name, "added ->", coins, "coins" )


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
    game_map = map_creator()            # Creates the map
    running = True
    coins = 0
    vehicle_pos = 5

    last_time_ran_car = 0.0
    last_time_ran_map = 0.0

    reset_sense()

    while running:
        now = time.time()
        sense.get_gyroscope()

        if now - last_time_ran_car > 1/3:                                              # Allows 3 movements before map moves
            vehicle_pos = car_pos_gyro(vehicle_pos)                      # Updates viechle position
            enable_screen(game_map, vehicle_pos)                        # Sends it to the led matrix
            point, collision = move_collision(game_map, vehicle_pos)    # Checks for collition or coin on move horisontally
            if collision:
                running = False
                break
            if point:
                coins += 1
            last_time_ran_car = now

        if now - last_time_ran_map > 1:
            point, collision = map_collision(game_map, vehicle_pos)         # Checks for collition or coin vertically

            if collision:
                running = False

            if point:
                coins += 1
            
            game_map = obstacle(game_map, coins)    # Adds new obstacles off screen
            game_map = coin_placer(game_map)        # Adds new coins off screen
            game_map = mov_map(game_map)            # Moves the map

            last_time_ran_map = now

    return coins

def memory(coins) :                                                         # Function that adds choose_name() and update_csv() 
    name = choose_name()                                                    # Find the variable name
    global player_scoreboard
    player_scoreboard = {"Name" : "Coins"}                                  # Create a dict with player names and scores
    player_scoreboard[name] = coins
    player_scoreboard
    if os.path.isfile('./SCOREBOARD_FPI.csv') :                             # If the .csv file already exist the 
        update_csv(name, coins)                                             # update_csv() runs
    else :
        with open('SCOREBOARD_FPI.csv', "w") as f:                          # Otherwise the file will first be created here !
            for name in player_scoreboard :
                f.write("%s %s\n"% (name, player_scoreboard[name]))
        print("Scoreboard created")

def main():
    meny_selection = 0          # Selects the first menu
    meny_max = 1                # Sets the max number of menues used
    coins = 0

    sense.stick.direction_down = j_left         # Binds the joystick to the joy functions
    sense.stick.direction_up = j_right          #
    sense.stick.direction_middle = j_middle     #
    sense.stick.direction_right = j_down        #
    sense.stick.direction_left = j_up           #

    # Add top of display in console
    startingLines()

    while True:
        if j_right_click:       # Checks for joy right movement
            reset_buttons()     # Reset the joy values
            meny_selection += 1 # Moves the menu
            if meny_selection > meny_max:   # Check for menu rollover
                meny_selection = 0
                transition(meny_pictures[meny_max], meny_selection[0], True)    # Moves image on screen
            else:
                transition(meny_pictures[meny_selection-1], meny_pictures[meny_selection], True)    # Moves image on screen
        elif j_left_click:      # Checks for joy left movement
            reset_buttons()     # Reset the joy values
            meny_selection -= 1 # Moves the menu
            if meny_selection < 0:  # Check for menu rollover
                meny_selection = meny_max
                transition(meny_pictures[0], meny_pictures[meny_max], False)    # Moves image on screen
            else:
                transition(meny_pictures[meny_selection+1], meny_pictures[meny_selection], False)   # Moves image on screen
        elif j_middle_click:    # Check for joy middle click
            reset_buttons()     # Reset joy values
            if meny_selection == 0:
                coins = run_game()
                player_dead()
                memory(coins)
            elif meny_selection == 1:
                break

        sense.set_pixels(meny_pictures[meny_selection]) # Update screen
    sense.clear()







if __name__ == "__main__":
    main()



