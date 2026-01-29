import pyxel
pyxel.init(320, 184, title="JeuNSI")
pyxel.load("my_resource.pyxres")
x = 20
y = 0
wallside = False
climbing = False
vy = 0

# pget(x, y) to get the status

def update():
    global x,y,vy
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
    if pyxel.btnp(pyxel.KEY_SPACE) and pyxel.pget(x,y+13) != 0:
        y = y - 12
    
    if y > 320:
        vy = 0
        x = 0 
        y = 20
    
    y += vy

    
def draw():
    global x,y
    pyxel.cls(0)
    pyxel.rect(x,y,6,12,2)
    pyxel.bltm(0, 0, 0, 0, 0, 320, 184)



pyxel.run(update,draw)
