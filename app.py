import pyxel
pyxel.init(320, 184, title="JeuNSI")
pyxel.load("my_resource.pyxres")
x = 20
y = 0
alt_init = y
wallside = False
climbing = False
vy = 0
rhitbox = False
lhitbox = False
uhitbox = False
dhitbox = False

# pget(x, y) to get the status

def hitbox (x,y):
    global rhitbox, lhitbox, uhitbox, dhitbox
    # up 1
    if pyxel.pget(x,y-1) != 0:
        uhitbox = True
        return uhitbox
    # up 2
    elif pyxel.pget(x+1,y-1) != 0:
        uhitbox = True
        return uhitbox
    # up 3
    elif pyxel.pget(x+2,y-1) != 0:
        uhitbox = True
        return uhitbox 
    # up 4
    elif pyxel.pget(x+3,y-1) != 0:
        uhitbox = True
        return uhitbox    
    # up 5
    elif pyxel.pget(x+4,y-1) != 0:
        uhitbox = True
        return uhitbox
    # up 6
    elif pyxel.pget(x+5,y-1) != 0:
        uhitbox = True
        return uhitbox
    else:
         uhitbox = False
         return uhitbox

    # dn 1
    if pyxel.pget(x,y+13) != 0:
        dhitbox = True
        return dhitbox
    # dn 2
    if pyxel.pget(x+1,y+13) != 0:
        dhitbox = True
        return dhitbox
    # dn 3
    if pyxel.pget(x+2,y+13) != 0:
        dhitbox = True
        return dhitbox
    # dn 4
    if pyxel.pget(x+3,y+13) != 0:
        dhitbox = True
        return dhitbox
    # dn 5
    if pyxel.pget(x+4,y+13) != 0:
        dhitbox = True
        return dhitbox
    # dn 6
    if pyxel.pget(x+5,y+13) != 0:
        dhitbox = True
        return dhitbox

    #left 1
    if pyxel.pget(x-1,y) != 0:
        lhitbox = True
        return lhitbox
    #left 2
    if pyxel.pget(x-1,y+1) != 0:
        lhitbox = True
        return lhitbox
    #left 3
    if pyxel.pget(x-1,y+2) != 0:
        lhitbox = True
        return lhitbox
    #left 4
    if pyxel.pget(x-1,y+3) != 0:
        lhitbox = True
        return lhitbox
    #left 5
    if pyxel.pget(x-1,y+4) != 0:
        lhitbox = True
        return lhitbox
    #left 6
    if pyxel.pget(x-1,y+5) != 0:
        lhitbox = True
        return lhitbox
    #left 7
    if pyxel.pget(x-1,y+6) != 0:
        lhitbox = True
        return lhitbox
    #left 8
    if pyxel.pget(x-1,y+7) != 0:
        lhitbox = True
        return lhitbox
    #left 9
    if pyxel.pget(x-1,y+8) != 0:
        lhitbox = True
        return lhitbox
    #left 10
    if pyxel.pget(x-1,y+9) != 0:
        lhitbox = True
        return lhitbox
    #left 11
    if pyxel.pget(x-1,y+10) != 0:
        lhitbox = True
        return lhitbox
    #left 12
    if pyxel.pget(x-1,y+11) != 0:
        lhitbox = True
        return lhitbox

    #right 1
    if pyxel.pget(x+7,y) != 0:
        rhitbox = True
        return rhitbox
    #right 2
    if pyxel.pget(x+7,y+1) != 0:
        rhitbox = True
        return rhitbox
    #right 3
    if pyxel.pget(x+7,y+2) != 0:
        rhitbox = True
        return rhitbox
    #right 4
    if pyxel.pget(x+7,y+3) != 0:
        rhitbox = True
        return rhitbox
    #right 5
    if pyxel.pget(x+7,y+4) != 0:
        rhitbox = True
        return rhitbox
    #right 6    
    if pyxel.pget(x+7,y+5) != 0:
        rhitbox = True
        return rhitbox
    #right 7
    if pyxel.pget(x+7,y+6) != 0:
        rhitbox = True
        return rhitbox
    #right 8
    if pyxel.pget(x+7,y+7) != 0:
        rhitbox = True
        return rhitbox
    #right 9
    if pyxel.pget(x+7,y+8) != 0:
        rhitbox = True
        return rhitbox
    #right 10
    if pyxel.pget(x+7,y+9) != 0:
        rhitbox = True
        return rhitbox
    #right 11
    if pyxel.pget(x+7,y+10) != 0:
        rhitbox = True
        return rhitbox
    #right 12
    if pyxel.pget(x+7,y+11) != 0:
        rhitbox = True
        return rhitbox


def update():
    global x,y,vy,alt_init,wallside,climbing
    print(x,y)

    if pyxel.btn(pyxel.KEY_D) == True and pyxel.pget(x+7, y+10) == 0:
        if x < 320   :
            x = x + 2
    if pyxel.btn(pyxel.KEY_Q) == True and pyxel.pget(x-1, y+10) == 0:
        if x > 0 and pyxel.pget(x-1,y) == 0 :
            x = x - 2    

    if pyxel.pget(x,y+13) == 0:
        vy += 0.5
    if pyxel.pget(x,y+13) != 0:
        vy = 0

    if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_Z) and pyxel.pget(x,y+13) != 0:
        alt_init = y
        if y - alt_init < 20 and pyxel.pget(x,y+13) != 0:
            vy = -5
        if y - alt_init > 20 or pyxel.pget(x,y-1) != 0:
            vy = 0
    if y > 320:
        vy = 0
        x = 0 
        y = 20
    
    if pyxel.btnp(pyxel.KEY_R) == True and pyxel.pget(x+7,y-12 or x-1,y-12) != 0:
        climbing = True
    else:
        climbing = False


    

    y += vy

    
def draw():
    global x,y
    pyxel.cls(0)
    pyxel.rect(x,y,6,12,2)
    pyxel.bltm(0, 0, 0, 0, 0, 320, 184, 0)



pyxel.run(update,draw)

