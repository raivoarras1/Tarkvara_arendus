import pygame, sys, random
pygame.init()

screenX = 640
screenY = 480
screen=pygame.display.set_mode([screenX,screenY])                #joonista aken suurusega 640x480px
pygame.display.set_caption("Ülesanne4 - Raivo Arras")    #Akna pealkirja määramine
clock = pygame.time.Clock()

#piltide lisamine
bg = pygame.image.load("bg_rally.jpg")                           #Taustapildi laadimine
red_car = pygame.image.load("f1_red.png")
blue_car = pygame.image.load("f1_blue.png")

screen.blit(bg,[0,0])           #taustapildi kuvamine
screen.blit(red_car, [300, 380])

posX, posY = random.randint(150, 350), random.randint(0,100)
speedY = 2

gameover = False
while not gameover:
    # fps
    clock.tick(60)
    #mängu sulgemine ristist
    events = pygame.event.get()
    for i in pygame.event.get():
       if i.type == pygame.QUIT:
           sys.exit()

    #pildi lisamine ekraanile
    screen.blit(blue_car, (posX,posY))
    posY += speedY

    if posY > screenY:
        posX, posY = random.randint(150, 350), random.randint(0,25)

    pygame.display.flip()   #akna värskendamine
    screen.blit(bg, [0, 0])  # taustapildi kuvamine
    screen.blit(red_car, [300, 380])

#akna sulgemine ristist
pygame.quit()