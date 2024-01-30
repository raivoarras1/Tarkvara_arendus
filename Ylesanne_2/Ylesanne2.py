import pygame

pygame.init()

screen=pygame.display.set_mode([640,480])                #joonista aken suurusega 640x480px
pygame.display.set_caption("Ülesanne2 - Raivo Arras")    #Akna pealkirja määramine

#piltide lisamine
bg = pygame.image.load("bg_shop.png")                           #Taustapildi laadimine
seller = pygame.image.load("seller.png")                        #tegelase pildi laadimine
seller = pygame.transform.scale(seller, [257, 305])        #tegelase pildi suuruse määramine
chat = pygame.image.load("chat.png")                            #jutumulli pildi laadimine
chat = pygame.transform.scale(chat, [258, 202])            #jutumulli pildi suuruse määramine
font = pygame.font.Font(pygame.font.match_font('arial'), 20)    #teksti fondi ja suuruse määramine
tekst = font.render("Tere, olen Raivo Arras", True, [255,255,255])  #teksi sisu ja värvi määramine

screen.blit(bg,[0,0])           #taustapildi kuvamine
screen.blit(seller,[103,159])   #tegelase pildi kuvamine (täpses asukohas)
screen.blit(chat,[245,66])      #tekstimulli kuvamine (täpses asukohas)
screen.blit(tekst, [274,135])   #teksti kuvamine (täpses asukohas)

pygame.display.flip()   #akna värskendamine
running = True

#akna lahti hoidmine
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#akna sulgemine ristist
pygame.quit()