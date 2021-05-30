from pygame import *
#from images import *
font.init()
mixer.init()

window=display.set_mode((800,600))
display.set_caption("Pet_Dog")

bcg=transform.scale(image.load("background.jpg"),(800,600))

game=True
clock=time.Clock()
FPS=60

while game:
    window.blit(bcg,(0,0))
    for e in event.get():
        if e.type==QUIT:
            game=False
    clock.tick(FPS)
    display.update()