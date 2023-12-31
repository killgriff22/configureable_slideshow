from pygame import *
path = open("path", "r").read()
screen = display.set_mode((800,800))
#set window caption to file name
display.set_caption(path.split("/")[-1])
while True:
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            exit()
    screen.fill((0,0,0))
    img = image.load(path).convert()
    img = transform.scale(img, (800,800))
    screen.blit(img, (0,0))
    display.flip()