import pygame, time


pygame.init()
#initialize the screen
width = 1000
height = 500
screen = pygame.display.set_mode((width, height))
screen_rect = screen.get_rect()

home_img = pygame.image.load('home.jpg')
home_img = pygame.transform.scale(home_img,(width,height))
home_rect = home_img.get_rect()

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
washroom_img = pygame.transform.scale(washroom_img,(width,height))
washroom_rect = washroom_img.get_rect()


pygame.display.flip()

#the game loop
running = True
washroom = False
party = False
classroom = False

level1 = False
level2 = False
level3 = False
home = False

i=0

while running:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #quit the game
            running = False
        elif event.type == pygame.KEYDOWN:   
            if event.key == pygame.K_1 and washroom: #level one: washroom
               level1 = True
               level2 = False
               level3 = False
               home = False
               party = True #makes the enxt level avaliable
            if event.key == pygame.K_2 and party: #level 2: party
               level1 = False
               level2 = True
               level3 = False
               home = False   
               classroom = True #makes the final level avaliable
            if event.key == pygame.K_3 and classroom: #level 3: classroom   
               level1 = False
               level2 = False
               level3 = True 
               home = False   
            if event.key == pygame.K_SPACE:
                washroom = True
                home = True
                level1 = False
                level2 = False
                level3 = False    

    #game logic
    if washroom == False:
        screen.blit(home_img,home_rect)
        pygame.display.update()
        img = home_img

    if level1:
        while True:
            screen.blit(lp_img,(i,0))
            screen.blit(washroom_img,(width + i,0))
            if(i==-width):
                break
            i -= 0.5 
            pygame.display.update()
            
    if level2:
        while True:
            screen.blit(lp_img,(i,0))
            screen.blit(party_img,(width + i,0))
            if(i==-width):
                break
            i -= 0.5 
            pygame.display.update()   

    if level3:
        while True:
            screen.blit(lp_img,(i,0))
            screen.blit(classroom_img,(width + i,0))
            if(i==-width):
                break
            i -= 0.5 
            pygame.display.update()   

    if home:
        screen.blit(lp_img,lp_rect)
        pygame.display.update()
        i=0                   

pygame.quit()