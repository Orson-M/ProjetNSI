import re

import pyxel
pyxel.init(320, 184, title="JeuNSI")
pyxel.load("my_resource.pyxres")
scale = 8
scale_multiplier = scale // 8 
x = 1*scale
y = 1*scale
vy = 0 # Has to be either 8 or 16 based on the tilemap used
rhitbox = False
lhitbox = False
uhitbox = False
dhitbox = False
dead = False
level = 1
player_size = 2

# pget(x, y) to get the status
def hitbox (x,y): # This function checks the hitbox of the player 
    global rhitbox, lhitbox, uhitbox, dhitbox, scale, player_size, scale_multiplier

    if scale == 8: # This checks the hitbox if the game is in 8x texture mode (stadard)
        if player_size == 2:
            for i in range(0,11*scale_multiplier):
                if pyxel.pget(x+i,y-1) != 0:
                    uhitbox = True
                    return uhitbox
                else:
                    uhitbox = False


            for i in range(0,11*scale_multiplier):
                if pyxel.pget(x+i,y+17) != 0:
                    dhitbox = True
                    return dhitbox
                else:
                    dhitbox = False


            for i in range(0,16*scale_multiplier):
                if pyxel.pget(x+12,y+i) != 0:
                    rhitbox = True
                    return rhitbox
                else:
                    rhitbox = False
        

            for i in range(0,16*scale_multiplier):
                if pyxel.pget(x-1,y+i) != 0:
                    lhitbox = True
                    return lhitbox
                else:
                    lhitbox = False
        if player_size == 1:
            for i in range(0,2*scale_multiplier):
                if pyxel.pget(x+i,y-1) != 0:
                    uhitbox = True
                    return uhitbox
                else:
                    uhitbox = False


            for i in range(0,2*scale_multiplier):
                if pyxel.pget(x+i,y+6) != 0:
                    dhitbox = True
                    return dhitbox
                else:
                    dhitbox = False


            for i in range(0,5*scale_multiplier):
                if pyxel.pget(x+2,y+i) != 0:
                    rhitbox = True
                    return rhitbox
                else:
                    rhitbox = False
        
            for i in range(0,5*scale_multiplier):
                if pyxel.pget(x-1,y+i) != 0:
                    lhitbox = True
                    return lhitbox
                else:
                    lhitbox = False

    """ if scale == 16: # This checks the hitbox if the game is in 16x texture mode
        for i in range(0,12):
            if pyxel.pget(x+i,y-1) != 0:
                uhitbox = True
                return uhitbox
            else:
                uhitbox = False


        for i in range(0,12):
            if pyxel.pget(x+i,y+12) != 0:
                dhitbox = True
                return dhitbox
            else:
                dhitbox = False


        for i in range(0,24):
            if pyxel.pget(x+16,y+i) != 0:
                rhitbox = True
                return rhitbox
            else:
                rhitbox = False
    

        for i in range(0,24):
            if pyxel.pget(x-1,y+i) != 0:
                lhitbox = True
                return lhitbox
            else:
                lhitbox = False"""

def spikes_dat(x,y): #This fuction checks if the player is touching a spike tile, and if so, and has the data of the spikes
    global level, dead, scale,scale_multiplier
    # coordinates in the list are tile positions (8x8 pixels)
    tiles = []
    if level == 1:
        tiles = [(3,5), (3,6), (3,7), (3,8), (3,9), (3,10), (3,11), (3,12), (3,13), (3,14), (3,15), (3,16), (3,17), (3,18),(3,19), (3,20), (3,21), (3,22), (3,23), (8,5), (8,6), (8,7), (8,8), (8,9), (8,10), (8,11), (8,12), (8,13), (8,14), (8,15), (9,4), (10,4), (11,4), (18,14), (18,15), (18,16), (18,17), (18,18), (18,19), (19,13), (20,13), (21,13), (23,13), (23,3), (23,4), (23,5), (23,6), (25,0), (25,1), (25,2), (25,3), (25,4), (25,5), (25,6), (30,9), (30,10), (30,11), (30,12), (30,13), (30,14), (30,15), (30,16), (30,17), (30,18), (30,19), (30,20), (37,10), (37,11), (37,12), (37,13), (37,14), (37,15)]
    if level == 2:
        tiles = [(9,23),(9,22),(9,21),(9,20), (10,20), (11,20), (12,20), (13,20), (14,21), (14,22), (14,23), (14,24), (14,25), (14,26), (20,4), (20,5), (20,6), (20,7), (20,8), (20,9), (20,10), (20,11), (20,12), (20,13), (20,14), (20,15), (17,19), (17,20), (17,21), (17,22), (17,23), (24,15), (24,14), (24,13), (24,12), (24,11), (24,10), (24,9), (24,8), (24,7), (24,6), (24,5), (24,4), (27,12), (27,13), (27,20), (27,21), (27,22), (27,23)]
    if level == 3:
        tiles = [(90,23),(90,22),(90,21),(90,20), (91,19), (92,23),(92,22),(92,21),(92,20),(92,19),(92,18),]
    # convert a pixel coordinate to tile coordinate
    def to_tile(a, b):
        return a // scale, b // scale

    #up
    if player_size == 2:
        for i in range(0,11*scale_multiplier):
            if to_tile(x+i, y-1) in tiles:
                dead = True
                return dead
        #dn
        for i in range(0,11*scale_multiplier):
            if to_tile(x+i, y+17) in tiles:
                dead = True
                return dead
        #right
        for i in range(0,16*scale_multiplier):
            if to_tile(x+12, y+i) in tiles:
                dead = True
                return dead
        #left
        for i in range(0,16*scale_multiplier):
            if to_tile(x-1, y+i) in tiles:
                dead = True
                return dead
    if player_size == 1:
        for i in range(0,2*scale_multiplier):
            if to_tile(x+i, y-1) in tiles:
                dead = True
                return dead
        #dn
        for i in range(0,2*scale_multiplier):
            if to_tile(x+i, y+5) in tiles:
                dead = True
                return dead
        #right
        for i in range(0,5*scale_multiplier):
            if to_tile(x+2, y+i) in tiles:
                dead = True
                return dead
        #left
        for i in range(0,5*scale_multiplier):
            if to_tile(x-1, y+i) in tiles:
                dead = True
                return dead
    
    return False
        
def death():
    global x,y,level,dead,vy
    if dead == True:
        vy = 0
        if level == 1:
            x = 1*scale
            y = 2*scale
            dead = False
        if level == 2:
            x = 2*scale
            y = 16*scale
            dead = False
        if level == 3:
            x = 3*scale
            y = 16*scale

def update():
    global x,y,vy,alt_init,climbing,rhitbox,lhitbox,uhitbox,dhitbox, level, dead
    
    # Check for death and reset position
    death()   
    player()
    hitbox(x, y)
    spikes_dat(x, y)
    level_change()
    dev_bypass()
    print("RH:", rhitbox, ", LH:", lhitbox, ", UH:", uhitbox, ", DH:", dhitbox)

    # Movements in "update" function for historical reasons
    if pyxel.btn(pyxel.KEY_D) == True and rhitbox == False:
        if x < 320   :
            x = x + 2
    if pyxel.btn(pyxel.KEY_Q) == True and lhitbox == False:
        if x > 0 and pyxel.pget(x-1,y) == 0 :
            x = x - 2    
    # Gravity
    if dhitbox == False :
        vy += 0.5
    else:
        vy = 0

    # Jumping
    if vy < 0 and (y - alt_init >= 20 or uhitbox):
        vy = 0
    if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_Z) and dhitbox == True:
        vy = -4
        alt_init = y



    if y > 184:
        dead = True


    y += vy

    if dhitbox and vy > 0:
        while dhitbox:
            y -= 1
            hitbox(x, y)
    if uhitbox and vy < 0:
        while uhitbox:
            y += 1
            hitbox(x, y)
    print(x,y)

def levels():
    global level,scale
    if level == 1:
        return pyxel.bltm(0, 0, 0, 0, 0, 320, 184, 0)
    if level == 2:
        return pyxel.bltm(0, 0, 0, 384, 0, 320, 184, 0)
    if level == 3:
        return pyxel.bltm(0, 0, 0, 88*scale, 0, 320, 184, 0)
    

def level_change():
    global level
    if level == 1 and x > 310 and y > 170: #go 2
        level = 2
    if level == 2 and x < 0: #go 3
        level = 3

def dev_bypass():
    global level,x,y,dead
    if pyxel.btnp(pyxel.KEY_1):
        level = 1
        x = 1*scale
        y = 2*scale
        return level, x, y
    if pyxel.btnp(pyxel.KEY_2):
        level = 2
        x = 2*scale
        y = 16*scale
        return level, x, y
    if pyxel.btnp(pyxel.KEY_3):
        level = 3
        x = 3*scale
        y = 16*scale
        return level, x, y

def player():
    global level, x, y, player_size
    if level == 1 or level == 2:
        player_size = 2
        pyxel.blt(x,y,0,16,32,11,16,0)
        return player_size
    if level == 3:
        player_size = 1
        pyxel.blt(x,y,0,32,35,2,5,0)
        return player_size

def draw():
    global x,y
    pyxel.cls(0)
    player()
    levels()



pyxel.run(update,draw)

