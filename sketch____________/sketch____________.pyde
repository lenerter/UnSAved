
x=0
g=0
u=0
h=0
l=0
i = 0
c1=0
c2=0
c3=0
c=0
w=0
Sp=2
SB=0
DB=0
CH=0
CT=0
cB1=0
cB2=0
cB3=0
def setup():
    global i
    size(2000,1000)
    noStroke()
    background(255)
    frameRate(120000000)
def draw():
    global x, g, h, u, i , l, c, c1, c2, c3, w, Sp, DB, SB, cB1, cB2, cB3, CH, CT
    background(255)
    i = loadImage("lox.jpg")
    w = loadImage("ntl.jpg")
    fill(0)
    rect(200,200,400,400)
    rect(800,200,400,400)
    rect(500,600,400,400)
    rect(1350,0,400,400)
    rect(1350,400,400,400)
    if c1 > 0 and cB1 == 0:
        fill(0,255,0)
        rect(0,800,100,100)
        SB=1
    if c1 > 0 and c2 > 0 and cB2 ==0:
        fill(100,255,100)
        rect(1000,900,100,100)
        DB=1
        SB=0
        sB1=0
    if cB3 ==0:
        fill(155)
        rect(400,600,100,100)
        CH=1
    if c1 == 0:
        fill(255,255,0)
        rect(610,400,180,180)
    if c1 > 0 and c2 == 0:
        fill(255,255,0)
        rect(1800,100,180,180)
    if c1 > 0 and c2 > 0 and c3 == 0:
        fill(255,255,0)
        rect(0,700,180,180)
    fill(125)
    rect(500,0,400,200)
    fill(random(0,255),random(0,255),random(0,255))
    rect(x,g,100,100)
    textSize(40)
    text(c,100,100)
    if x+100 > 500 and x < 900 and g+100 > 600 and g < 900:
        l=1
    if x+100 > 200 and x < 600 and g+100 > 200 and g < 600:
        l=1
    if x+100 > 800 and x < 1200 and g+100 > 200 and g < 600:
        l=1
    if x+100 > 1350 and x < 1750 and g+100 > 0 and g < 400:
        l=1
    if x+100 > 1350 and x < 1750 and g+100 > 400 and g < 800:
        l=1 
    if x+100 > 610 and x < 790 and g+100 > 400 and g < 580:
        if c < 1:
            c1=1
    if x+100 > 1800 and x < 1980 and g+100 > 100 and g < 280:
        if c < 2 and c > 0:
            c2=1
    if x+100 > 0 and x < 180 and g+100 > 700 and g < 880:
        if c < 3 and c > 1:
            c3=1
    if SB == 1:
        if x+100 > 0 and x < 100 and g+100 > 800 and g < 900:
            Sp=7
            cB1=0
    if DB == 1:
        if x+100 > 1000 and x < 1100 and g+100 > 900 and g < 1000:
            Sp=1
            cB2=0
    if key == CODED:
        if keyCode == UP: 
            g-=Sp
        if keyCode == LEFT:
            x-=Sp
        if keyCode == RIGHT:
            x+=Sp
        if keyCode == DOWN:
            g+=Sp
    if c1 == 1:
        c+=1
        c1=2
    if c2 == 1:
        c+=1
        c2=2
    if c3 == 1:
        c+=1
        c3=2
    if c == 3:
        l=2                 #win
    if key == 'r':
        x=0
        g=0
        l=0
        c=0
        c1=0
        c2=0
        c3=0
        Sp=2
        SB=0
        DB=0
        cB1=0
        cB2=0
        cB3=0
    if key == 'd':
        l=1
    if key == 'w':
        l=2
    if key == 'a':
        l=0
        x=0
        g=0
        Sp=2
        SB=0
        DB=0
        cB1=0
        cB2=0
    if key == 's':
        Sp=10
    if key == 'q':
        Sp=2
    if l == 1:
        image(i,0,0,2000,1000)
        fill(255)
        textSize(30)
        text("Press R to Restart",900,900)
    if l == 2:
        image(w,0,0,2000,1000)
        fill(255)
        textSize(30)
        text("Press R to Restart",900,900)
    if CH == 1:
        if x+100 > 400 and x < 500 and g+100 > 600 and g < 700:
            cB3=1
            CT=1
    if CT == 1:
        text("CHEATS MENU - w=win,s=Supersped,d=kill,a=Arrive to live,q=normal speed",100,200)        
    
