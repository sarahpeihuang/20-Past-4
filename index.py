import pygame, sys
from pygame import mixer


pygame.init()
mixer.init()
clock = pygame.time.Clock()

#initialize the screen
width = 1200
height = 600
screen = pygame.display.set_mode((width, height))
screen_rect = screen.get_rect()

#initialize images
blk_img = pygame.image.load('black.jpg')
blk_img = pygame.transform.scale(blk_img,(width,height))
blk_rect = blk_img.get_rect()

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

#initialize music
mixer.music.load('intro.mp3')
mixer.music.set_volume(1)
mixer.music.play()

#initialize text
base_font = pygame.font.Font(None, 32)
user_text = ''
input_rect = pygame.Rect(200, 200, 140, 32)
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('chartreuse4')
color = color_passive
active = False

running = True
washroom = False
party = False
classroom = False

level1 = False
level2 = False
level3 = False
home = False

i=0
j=0
while running:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #quit the game
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
        if event.type == pygame.KEYDOWN:   
            if event.key == pygame.K_UP and washroom: #level one: washroom
               level1 = True
               level2 = False
               level3 = False
               home = False
               party = True #makes the enxt level avaliable
            if event.key == pygame.K_LEFT and party: #level 2: party
               level1 = False
               level2 = True
               level3 = False
               home = False   
               classroom = True #makes the final level avaliable
            if event.key == pygame.K_RIGHT and classroom: #level 3: classroom   
               level1 = False
               level2 = False
               level3 = True 
               home = False   
            if event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT: #landing page
                washroom = True
                home = True
                level1 = False
                level2 = False
                level3 = False    
            # Check for backspace
            if event.key == pygame.K_BACKSPACE:
  
                # get text input from 0 to -1 i.e. end.
                user_text = user_text[:-1]
  
            # Unicode standard is used for string
            # formation
            else:
                user_text += event.unicode
                #print("+++++++"+str(user_text))

            if event.key == pygame.K_RETURN:
                print(str(user_text))
                user_text = ''

            

    #game logic
    if active:
        color = color_active
    else:
        color = color_passive

    # draw rectangle and argument passed which should be on screen
    pygame.draw.rect(screen, color, input_rect)
    text_surface = base_font.render(user_text, True, (255, 255, 255))
      
    # render at position stated in arguments
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
      
    # set width of textfield so that text cannot get outside of user's text input
    input_rect.w = max(100, text_surface.get_width()+10)
      
    pygame.display.flip() # display.flip() will update only a portion of the screen to updated, not full area
    clock.tick(60) # clock.tick(60) means that for every second at most 60 frames should be passed.

    if washroom == False:
        while True:
            screen.blit(blk_img,(0,j))
            screen.blit(home_img,(0,height + j))
            if(j== -height):
                break
            j -= 0.25
            pygame.display.update()


    if level1:
        while True:
            screen.blit(lp_img,(i,0))
            screen.blit(washroom_img,(width + i,0))
            if(i==-width): 
                break
            i -= 0.5 
            mixer.music.load('washroom.mp3')
            mixer.music.play()
            pygame.display.update()
            
    if level2:
        while True:
            screen.blit(lp_img,(i,0))
            screen.blit(party_img,(width + i,0))
            if(i==-width):
                break

            i -= 0.5 
            mixer.music.load('party.mp3')
            mixer.music.play()
            pygame.display.update()   

    if level3:
        while True:
            screen.blit(lp_img,(i,0))
            screen.blit(classroom_img,(width + i,0))
            if(i==-width):
                break
            i -= 0.5 
            mixer.music.load('classroom.mp3')
            pygame.display.update()   

    if home:
        screen.blit(lp_img,lp_rect)
        pygame.display.update()
        i=0                   

pygame.quit()