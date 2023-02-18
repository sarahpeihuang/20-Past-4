import pygame


pygame.init()
#initialize the screen
width = 1000
height = 500
screen = pygame.display.set_mode((width, height))
screen_rect = screen.get_rect()

lp_img = pygame.image.load('landing page.jpg')
lp_img = pygame.transform.scale(lp_img,(width,height))
lp_rect = lp_img.get_rect()

classroom_img = pygame.image.load('classroom.jpg')
classroom_img = pygame.transform.scale(classroom_img,(width,height))
classroom_rect = classroom_img.get_rect()

party_img = pygame.image.load('party.jpg')
party_img = pygame.transform.scale(party_img,(width,height))
party_rect = party_img.get_rect()

washroom_img = pygame.image.load('washroom.jpg')
washroom_rect = washroom_img.get_rect()


pygame.display.flip()

#the game loop
running = True
washroom = True
party = False
classroom = False
i=0

while running:
    #event loop
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #quit the game
            running = False
        elif event.type == pygame.KEYDOWN:
            screen.blit(lp_img,(i,0))
            i -= 1
            if event.key == pygame.K_1 and washroom: #level one: washroom
               party = True
               screen = pygame.display.set_mode((washroom_rect.width, washroom_rect.height))
               screen_rect = screen.get_rect()
               #render
               pygame.display.flip()
               screen.blit(washroom_img,washroom_rect)

            if event.key == pygame.K_2 and party: #level 2: party
               classroom = True
               screen = pygame.display.set_mode((party_rect.width, party_rect.height))
               screen_rect = screen.get_rect()

            if event.key == pygame.K_3 and classroom: #level 3: classroom   
                screen = pygame.display.set_mode((classroom_rect.width, classroom_rect.height))
                screen_rect = screen.get_rect()

    #game logic

    #render
    pygame.display.flip()
    screen.blit(lp_img,lp_rect)
pygame.quit()