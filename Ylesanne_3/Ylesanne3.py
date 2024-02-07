import pygame

def ruudustik(screen, mode, cell_size, color, rida, veerg):      #funktsioon ruudustiku joonistamiseks
    i = 0                                       #ruudustiku algkoordinaat x
    j = 0                                       #ruudustiku algkoordinaat y
    r = 0                                       #rea numbri algväärtus
    v = 0                                       #veeru numbri algväärtus
    while j < mode[1] and r < rida:             #tsükkel seni kuni j on väiksem ekraani mõõtmetest ja ridade arv on väiksem etteantud arvust
        while i < mode[0] and v < veerg:        #tsükkel seni kuni i on väiksem ekraani mõõtmetest ja veergude arv on väiksem etteantud arvust
            #joonista ruut koordinaadiga (i, j) ja suurusega "cell_size" * "cell_zize"
            pygame.draw.rect(screen, color, [i, j, cell_size, cell_size], 1)
            i += cell_size                      #liigu "cell_size" võrra paremale
            v += 1                              #veeru numbri suurendamine
        j += cell_size                          #kui rida on täis, siis liigu cell_size võrra alla
        r += 1                                  #rea numbri suurendamine
        i = 0                                   #liigu tagasi rea algusesse
        v = 0                                   #veeru numbri "reset"

pygame.init()

#Mõned värvid, mida kasutada ruudustiku joonistamiseks
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
yellow = [255, 255, 0]

#Ekraani parameetrid
mode = [640, 480]                                           #akna suurus, mida kasutada
pygame.display.set_caption("Ülesanne3 - Raivo Arras")       #akna pealkiri
screen = pygame.display.set_mode(mode)                      #akna loomine
screen.fill([153, 255, 153])                                #akna taustavärv

cell_size = 20                                              #ruudu suuruse valimine
color = red                                                 #joone värvi valimine
rida = 100                                                  #mitu rida joonistada (seni kuni mahub)
veerg = 100                                                 #mitu veergu joonistada (seni kuni mahub)
ruudustik(screen, mode, cell_size, color, rida, veerg)      #ruudustiku joonistamine

pygame.display.flip()                                       #ekraanipildi värskendamine
running = True

while running:                                              #ekraani lahti hoidmine
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()                                               #ekraani sulgemine
