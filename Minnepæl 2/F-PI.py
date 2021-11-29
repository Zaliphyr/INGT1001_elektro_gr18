# Hei og velkommen til F-Pi main

r = (0, 0, 0) # road / black
g = (0, 255, 0) # grass / green
o = (255, 0, 0) # obstacle
c = (255, 255, 0) # coin


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


def car_pos_gyro(prev_pos): # Function for the position of the car controlled by gyroscope,
                            # with previous position as input shown by an integer between 0 and 7
    from sense_hat import SenseHat # Importing SenseHat from sense_hat library
    sense = SenseHat()

    orientation = sense.get_orientation_degrees() # Collecting orientational data from sensehat
    yaw = orientation["yaw"] # Singling out the data for the yaw orientation

    if yaw >= 350 or yaw <= 10: # If the "wheel" of the car is almost flat:
        position = prev_pos # Keep the previous position
    elif 350 > yaw > 315: # If the "wheel" of the car is pointed a little to the left:
        position = prev_pos - 1 # Move the car one space to the left
    elif 315 >= yaw >= 270: # If the "wheel" of the car is pointed between 45 and 90 degrees to the left:
        position = prev_pos - 2 # Move the car two spaces to the left
    elif 270 > yaw > 180: # If the "wheel" of the car is at pointed more than 90 degrees to the left:
        position = prev_pos - 3 # Move the car three places to the left
    elif 10 < yaw < 45: # If the "wheel" of the car is pointed a little to the right:
        position = prev_pos + 1 # Move the car one space to the right
    elif 45 <= yaw <= 90: # If the "wheel" of the car is pointed between 45 and 90 degrees to the right:
        position = prev_pos + 2 # Move the car two spaces to the right
    elif 90 < yaw < 180: # If the "wheel" of the car is at pointed more than 90 degrees to the right:
        position = prev_pos + 3 # Move the car three spaces to the right
    else: # If the value is 180 degrees or somehow show something that's not between 0 and 360:
        position = prev_pos # Keep the previous position of the car

    if position < 0: # The car can't go further to the left than 0, therefor if the position is negative:
        position = 0 # Set the position to 0
    elif position > 7: # The car can't go further to the right than 7, therefor if the position is over 7:
        position = 7 # Set the position to 7

    return position # The function returns the value of the postition from 0 to 7

def car_pos_joy(prev_pos): # Function for the position of the car controlled by the joystick,
                           # with previous position as input shown by an integer between 0 and 7
    from sense_hat import SenseHat # Importing SenseHat from sense_hat library
    sense = SenseHat()
    event = sense.stick.wait_for_event() # Henter data fra joystick
    joy_input = event[1]

    if joy_input == "left":
        position = prev_pos - 1
    elif joy_input == "right":
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


def main():
    pass




if __name__ == "__main__":
    main()

