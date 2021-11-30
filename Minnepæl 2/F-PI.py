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



def main():
    pass




if __name__ == "__main__":
    main()

