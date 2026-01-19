import pyxel
pyxel.init(320, 184, title="JeuNSI")
x = 0
y = 0
wallside = False
grounded = True 
climbing = False
vy = 0

# pget(x, y) to get the status
def player_deplacement(x,y):
    """déplacement avec les touches de directions"""

    if pyxel.btn(pyxel.KEY_D) == True:
        if x < 320 and pyxel.pget(x+1,y) == 0  :
            x = x + 2
    if pyxel.btn(pyxel.KEY_Q) == True:
        if x > 0 and pyxel.pget(x-1,y) == 0:
            x = x - 2
    return x

"""def climb(wallside, climbing, player_y):
    if wallside == True and pyxel.btn(pyxel.KEY_UP) == True:
        player_y = player_y + 1
        climbing = True
    else:
        climbing = False
    return climbing, player_y"""

def touch_ground(player_x, player_y,g):
    if pyxel.pget(x, y + 1) != 0:
        g = True
    else:
        g = False
        return g
    grounded = touch_ground(g)
    
def update():
    global x,y,player_x,player_y,vy, grounded
        
    if pyxel.btnp(pyxel.KEY_Z) and grounded == True:
        vy = -10
    vy += 1
    y += vy
    if grounded == True:
        vy = 0
        

    player_x = player_deplacement(x)
    
def draw():
        pyxel.cls(0)
        pyxel.rect(0,180,321,4,4)
        pyxel.rect(player_x,y,6,12,2)


pyxel.run(update,draw)

