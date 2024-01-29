import pygame

pygame.init()

screen=pygame.display.set_mode([300,300])               #joonista aken suurusega 300x300px
pygame.display.set_caption("Lumemees - Raivo Arras")    #Akna pealkirja määramine
screen.fill([0, 0, 0])                                  #akna taustavärv "must"

#joonistamine
#lumepallid
pygame.draw.circle(screen, [255, 255, 255], [150,75], 30)   #ülemine pall
pygame.draw.circle(screen, [255, 255, 255], [150,140], 40)  #keskmine pall
pygame.draw.circle(screen, [255, 255, 255], [150,225], 50)  #alumine pall
#silmad
pygame.draw.circle(screen, [0, 0, 0], [140,70], 5)          #vasak silm
pygame.draw.circle(screen, [0, 0, 0], [160,70], 5)          #parem silm
#nina
pygame.draw.polygon(screen, [255, 0, 0], [[145,80],[155,80],[150,95]])

#akna värskendamine
pygame.display.flip()
running = True

#akna lahti hoidmine
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#akna sulgemine
pygame.quit()