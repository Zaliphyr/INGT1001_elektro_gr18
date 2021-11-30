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

