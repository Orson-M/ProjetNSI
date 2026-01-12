import pyxel
pyxel.init(320, 184, title="JeuNSI")
player_x = 0
player_y = 0
wallside = False
grounded = True 
climbing = False

def player_deplacement(player_x, player_y):
    """déplacement avec les touches de directions"""

    if pyxel.btn(pyxel.KEY_RIGHT):
        if (player_x < 320) :
            player_x = player_x + 1
    if pyxel.btn(pyxel.KEY_LEFT):
        if (player_x > 0) :
            player_x = player_x - 1
   # if pyxel.btn(pyxel.KEY_DOWN):
    #    if (player_y < 184) :
     #       player_y = player_y + 1
    #if pyxel.btn(pyxel.KEY_UP):
      #  if (player_y > 0) :
          #  player_y = player_y - 1
    if pyxel.btn(pyxel.SPACE):
        if (player_y < 320-16):
            player_y = player_y + 8
    return player_x, player_y

def climb(wallside, climbing, player_y):
    if wallside = True and pyxel.btn(pyxel.KEY_UP) = True:
        player_y = player_y + 1
        climbing = True
    else 
        climbing = False
    return climbing, player_y
        
def gravity(player_x, player_y, grounded, climbing):
    if grounded = False:
        if climbing = False:
            player_y = player_y - 1
    return player_x, player_y

def touch_ground(player_x, player_y, grounded):
    return


def update():
    global player_x, player_y

def draw():
    pyxel.cls(1)


pyxel.run(update,draw)

