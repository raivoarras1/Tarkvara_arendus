import pygame

pygame.init()

screen=pygame.display.set_mode([300,300])           #joonista aken suurusega 300x300px
pygame.display.set_caption("Foor - Raivo Arras")    #Akna pealkirja määramine
screen.fill([0, 0, 0])                              #akna taustavärv "must"

#joonistamine
#foorituled - punane, kollane, roheline (värv, keskpunkt. raadius)
pygame.draw.circle(screen, [255, 0, 0], [150,60], 40)
pygame.draw.circle(screen, [255, 255, 0], [150,145], 40)
pygame.draw.circle(screen, [0, 255, 0], [150,230], 40)
#kast ümber fooritulede (värv, [kasti ülemine vasak nurk, kasti suurus], raami paksus)
pygame.draw.rect(screen, [150, 150, 150], [100, 10, 100, 270], 1)   #kast ümber fooritulede

pygame.display.flip()   #akna värskendamine
running = True

#akna lahti hoidmine
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#akna sulgemine ristist
pygame.quit()