import pygame, random
pygame.init()

screenX = 640   # ekraani suurus
screenY = 480
skoor = 0       # algne skoor
redX = 300      # punase auto algne x-koordinaat, raja keskel
font = pygame.font.Font(pygame.font.match_font('arial'), 24)   # teksti fondi ja suuruse määramine
screen=pygame.display.set_mode([screenX,screenY])                   # joonista aken ette antud suurusega
pygame.display.set_caption("Ülesanne4 - Raivo Arras")               # akna pealkirja määramine
clock = pygame.time.Clock()                                         # objekti "kell" loomine

#piltide lisamine
bg = pygame.image.load("bg_rally.jpg")                   # taustapildi laadimine
red_car = pygame.image.load("f1_red.png")                # punase auto pildi laadimine
blue_car = pygame.image.load("f1_blue.png")              # sinise auto pildi laadimine

# Esimese sinise auto algkoordinaadi genereerimine, et mahuks rajale ja alustaks raja algusest
bluX, bluY = random.randint(145, 450), 0

speedY = 5      #autode liikumiskiirus

# akna lahti hoidmine kuniks ristist suletakse
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)                              # fps, ekraanikuva värskendamise sagedus

    screen.blit(blue_car, [bluX,bluY])     # sinise auto kuvamine ekraanile
    bluY += speedY                              # sinise auto y-koordinaadi muutmine vastavalt kiirusele

    # kui sinine auto jõuab ekraani lõppu
    if bluY > screenY:
        # siis genereeritakse uue sinise auto algkoordinaat (raja piirides, erinevale kõrgusele)
        bluX, bluY = random.randint(145, 450), random.randint(-25, 100)
        #ja lisatakse skoorile +1
        skoor += 1

    # punase auto liigutamine vastavalt sellele, kas sinine auto jääb talle ette
    difference_x = bluX - redX              # võrdle autode x-koordinaate
    if redX in range (185, 410):            # kui punane auto on raja keskosas
        serv = 0                            # siis servad ei ole ohtlikud

    if difference_x in range (-45, 0):      # kui autod on kokku põrkamas ja sinine auto on vasakul
        if redX > 450:                      # kui punane auto on parema serva ääres
            serv = 2                        # siis märgi parem serv "ohtlikuks"
        if serv == 2:                       # kui parem serv on ohtlik
            redX -= 4                       # siis liiguta punast autot kiiresti vasakule
        else:                               # vastasel juhul...
            redX += 2                       # liiguta punast autot paremale

    if difference_x in range (0, 45):       # kui autod on kokku põrkamas ja sinine auto on paremal
        if redX < 145:                      # kui punane auto on raja vasaku serva ääres
            serv = 1                        # siis märgi vasak serv "ohtlikuks"
        if serv == 1:                       # kui vasak serv on ohtlik
            redX += 4                       # siis liiguta punast auto kiiresti paremale
        else:                               # vastasel juhul...
            redX -= 2                       # liiguta punast autot vasakule

    kuva_skoor = font.render("Skoor: " + str(skoor), True, [0, 0, 0]) # skoori teksti loomine
    pygame.display.flip()                                    # akna värskendamine
    screen.blit(bg, [0, 0])                             # taustapildi kuvamine/värskendamine
    screen.blit(red_car, [redX, 380])                   # punase auto pildi kuvamine/värskendamine
    screen.blit(kuva_skoor, [530, 30])                  # skoori teksti kuvamine/värskendamine

# akna sulgemine ristist
pygame.quit()