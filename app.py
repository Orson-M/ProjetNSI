import pyxel
pyxel.init(320, 184, title="JeuNSI")
player_x = 0
player_y = 0
wallside = False
grounded = True 
climbing = False
vy = 0
# pget(x, y) to get the status
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
    #if pyxel.btn(pyxel.KEY_SPACE):
       # if (player_y < 320-16):
            #player_y = player_y + 8
    return player_x, player_y

def climb(wallside, climbing, player_y):
    if wallside == True and pyxel.btn(pyxel.KEY_UP) == True:
        player_y = player_y + 1
        climbing = True
    else:
        climbing = False
    return climbing, player_y
        
def jump(player_x, player_y, grounded, climbing):
    if grounded == False and climbing == False :
            player_y = player_y - 1
    return player_x, player_y

def touch_ground(player_x, player_y, grounded):
    if pget(player_x, player_y + 1) == 0:
        grounded = False 
    return grounded


def update():
    global player_x, player_y, vy
    if pyxel.btnp(pyxel.KEY_SPACE):
        vy = -5
    vy += 1
    player_y += vy
    if player_y > 100:
        vy = 0
        player_y=100

def draw():
    pyxel.cls(1)
    pyxel.rect(player_x,player_y,4,8,2)


pyxel.run(update,draw)
