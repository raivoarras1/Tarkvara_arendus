import pygame

def ruudustik(screen, mode, cell_size, color):      #funktsioon ruudustiku joonistamiseks
    i = 0                                           #ruudustiku algkoordinaat x
    j = 0                                           #ruudustiku algkoordinaat y
    while j < mode[1]:                              #tsükkel seni kuni j on väiksem ekraani mõõtmetest
        while i < mode[0]:                          #tsükkel seni kuni i on väiksem ekraani mõõtmetest
            #joonista ruut koordinaadiga (i, j) ja suurusega cell_size
            pygame.draw.rect(screen, color, [i, j, cell_size, cell_size], 1)
            i += cell_size                          #liigu cell_size võrra paremale
        j += cell_size                              #liigu cell_size võrra alla
        i = 0                                       #liigu tagasi rea algusesse

pygame.init()

#Mõned värvid, mida kasutada ruudustiku joonistamiseks
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
yellow = [255, 255, 0]

#Ekraani parameetrid
mode = [640, 480]                                       #suurus, mida kasutada joonistamisel
pygame.display.set_caption("Ülesanne3 - Raivo Arras")   #pealkiri
screen = pygame.display.set_mode(mode)                  #suurus
screen.fill([153, 255, 153])                            #taustavärv

cell_size = 20                                          #ruudu suuruse valimine
color = red                                            #joone värvi valimine
ruudustik(screen, mode, cell_size, color)               #ruudustiku joonistamine

pygame.display.flip()                                   #ekraanipildi värskendamine
running = True

while running:                                          #ekraani lahti hoidmine
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()                                           #ekraani sulgemine
