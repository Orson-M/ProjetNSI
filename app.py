import pyxel
pyxel.init(320, 184, title="JeuNSI")
x = 20
y = 0
wallside = False
climbing = False
vy = 0

# pget(x, y) to get the status

def update():
    global x,y,vy, grounded
    print(pyxel.pget(x,y+13))
    print(vy)

    if pyxel.btn(pyxel.KEY_D) == True and pyxel.pget(x+7, y+10) == 0:
        if x < 320   :
            x = x + 2
    if pyxel.btn(pyxel.KEY_Q) == True and pyxel.pget(x-1, y+10) == 0:
        if x > 0 and pyxel.pget(x-1,y) == 0 :
            x = x - 2       
    if pyxel.pget(x,y+13) == 0:
        vy += 1
    if pyxel.pget(x,y+13) != 0:
        vy = 0
    if pyxel.btnp(pyxel.KEY_Z) and pyxel.pget(x,y+13) != 0:
        y = y - 10
    
    y += vy
    
    
def draw():
    pyxel.cls(0)
    # pyxel.load()
    pyxel.rect(x,y,6,12,2)
    pyxel.rect(0,100,160,150,6)
    pyxel.rect(0,150,320,184,6)


pyxel.run(update,draw)