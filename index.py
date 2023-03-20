import pygame
from pygame import mixer
import cohereFn, imgInit


pygame.init()
mixer.init()
clock = pygame.time.Clock()

#initialize the screen
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_rect = screen.get_rect()

#initialize images
blk_rect = imgInit.blk_img.get_rect()
home_rect = imgInit.home_img.get_rect()
lp_rect = imgInit.lp_img.get_rect()
classroom_rect = imgInit.classroom_img.get_rect()
party_rect = imgInit.party_img.get_rect()
washroom_rect = imgInit.washroom_img.get_rect()
screen.blit(imgInit.situation1_init, (50,10))
screen.blit(imgInit.situation1_fail, (50,10))
screen.blit(imgInit.situation1_pass, (50,10))
screen.blit(imgInit.situation2_init, (50,10))
screen.blit(imgInit.situation2_fail, (50,10))
screen.blit(imgInit.situation2_pass, (50,10))
screen.blit(imgInit.situation3_init, (50,10))
screen.blit(imgInit.situation3_fail, (50,10))
screen.blit(imgInit.situation3_pass, (50,10))

#character images
main = pygame.transform.scale(imgInit.main,(100,250))
second = pygame.transform.scale(imgInit.second,(100,250))
third = pygame.transform.scale(imgInit.third,(250,250))
fourth = pygame.transform.scale(imgInit.fourth,(150,300))
teacher = pygame.transform.scale(imgInit.teacher,(250,250))
pygame.display.flip()

#initialize music
mixer.music.load('audio/Intro.mp3')
mixer.music.set_volume(1)
mixer.music.play()

#initialize text
base_font = pygame.font.Font(None, 32)
user_text = ''
input_rect = pygame.Rect(200, 200, 140, 32)
input_color_active = pygame.Color('lightskyblue3')
input_color_passive = pygame.Color('chartreuse4')
input_color = input_color_passive

output_rect = pygame.Rect(400,250,140,32)
output_color = pygame.Color('orange')

#level progression parameters
active = False #for text box highlight
running = True #for game loop

#to make the levels avaliable in order
washroom = False
party = False
classroom = False

#screens
level1 = False
level2 = False
level3 = False
home = False

#once character clicks enter, triggers interface reply
replied = False

#checks game completion, shows endgame screen
level1_pass = False
level2_pass = False
level3_pass = False

#to calculate final score
tries = 0
success = 0

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
               party = True #makes the next level avaliable
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
            if event.key == pygame.K_TAB: #landing page
                washroom = True
                home = True
                level1 = False
                level2 = False
                level3 = False    
                replied = False
            # Check for backspace
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
  
            else: #display text
                user_text += event.unicode

            if event.key == pygame.K_RETURN:
                replied = True
                #call cohere functions when reply is submit depending on level
                if level1:
                    level1_reply = cohereFn.washroomResponse(user_text)
                if level2:
                    level2_reply = cohereFn.partyResponse(user_text)
                if level3:   
                    level3_reply = cohereFn.classroomResponse(user_text)
                user_text = ''
    clock.tick(60)      

    #game logic
    #imput text box
    if active: 
        input_color = input_color_active
    else:
        input_color = input_color_passive

    if washroom == False:#home page upward transition
        while True:
            screen.blit(imgInit.blk_img,(0,j))
            screen.blit(imgInit.home_img,(0,SCREEN_HEIGHT + j))
            if(j== -SCREEN_HEIGHT):
                break
            j -= 0.25
            pygame.display.update()

    if level1: #initialize level setting
        while True:
            #screen transition
            screen.blit(imgInit.lp_img,(i,0))
            screen.blit(imgInit.washroom_img,(SCREEN_WIDTH + i,0))
            if(i==-SCREEN_WIDTH): 
                break
            i -= 0.5 
            #play music
            mixer.music.load('audio\Washroom.mp3')
            mixer.music.set_volume(0.5)
            mixer.music.play()
            pygame.display.update()

        #blit characters
        screen.blit(main,(75,300))
        screen.blit(second,(1000,325))

        # draw rectangle and argument passed which should be on screen
        pygame.draw.rect(screen, input_color, input_rect)
        input_text_surface = base_font.render(user_text, True, (255, 255, 255))
        screen.blit(input_text_surface, (input_rect.x+5, input_rect.y+5))
        input_rect.w = max(100, input_text_surface.get_width()+10)
        clock.tick(60)

        if replied == False: #before response is typed
            screen.blit(imgInit.situation1_init, (50,10))
            #replying user
            pygame.draw.rect(screen, output_color, output_rect)
            output_text_surface = base_font.render("Hey bro, want to take a hit (inhaling one puff of marijuana)?", True, (255, 255, 255))
            screen.blit(output_text_surface, (output_rect.x+5, output_rect.y+5))
            output_rect.w = max(100, output_text_surface.get_width()+10)
            clock.tick(100)   
            pygame.display.flip()

        if replied:
            if level1_reply == "Positive": #if api returns
                level1_pass = True
                tries += 1
                success += 1
                # reply
                pygame.draw.rect(screen, output_color, output_rect)
                output_text_surface = base_font.render("Okay, whatever makes you comfortable!", True, (255, 255, 255))
                screen.blit(output_text_surface, (output_rect.x+5, output_rect.y+5))
                output_rect.w = max(100, output_text_surface.get_width()+10)
                clock.tick(60) 
            
                screen.blit(imgInit.situation1_pass, (50,10))   
                pygame.display.flip()
            else:  
                tries += 1
                # reply
                pygame.draw.rect(screen, output_color, output_rect)
                output_text_surface = base_font.render("Here you go.", True, (255, 255, 255))  
                screen.blit(output_text_surface, (output_rect.x+5, output_rect.y+5))
                output_rect.w = max(100, output_text_surface.get_width()+10)
                clock.tick(60)  
                screen.blit(imgInit.situation1_fail, (50,10))
                pygame.display.flip()

    if level2: #initialize level setting      
        while True:
            screen.blit(imgInit.lp_img,(i,0))
            screen.blit(imgInit.party_img,(SCREEN_WIDTH + i,0))
            if(i==-SCREEN_WIDTH):
                break

            i -= 0.5 
            mixer.music.load('audio/Party.mp3')
            mixer.music.set_volume(0.5)
            mixer.music.play()
            pygame.display.update()   

        screen.blit(main,(75,300))
        screen.blit(second,(500,325))
        screen.blit(third,(600,400))
        screen.blit(fourth,(850,300))

        # draw rectangle and argument passed which should be on screen
        pygame.draw.rect(screen, input_color, input_rect)
        input_text_surface = base_font.render(user_text, True, (255, 255, 255))
        screen.blit(input_text_surface, (input_rect.x+5, input_rect.y+5))
        input_rect.w = max(100, input_text_surface.get_width()+10)
        clock.tick(60)

        if replied == False: #before response is typed
            #replying user
            pygame.draw.rect(screen, output_color, output_rect)
            output_text_surface = base_font.render("Woah, the smoke looks so cool, let’s smoke!", True, (255, 255, 255))
            screen.blit(output_text_surface, (output_rect.x+5, output_rect.y+5))
            output_rect.w = max(100, output_text_surface.get_width()+10)
            clock.tick(60) 

            screen.blit(imgInit.situation2_init, (50,10))
            pygame.display.flip() 

        if replied:
            if level2_reply == "Positive":
                level2_pass = True
                tries += 1
                success += 1
                # reply
                pygame.draw.rect(screen, output_color, output_rect)
                output_text_surface = base_font.render("I guess my head hurts a bit, we can step out.", True, (255, 255, 255))
                screen.blit(output_text_surface, (output_rect.x+5, output_rect.y+5))
                output_rect.w = max(100, output_text_surface.get_width()+10)
                clock.tick(60) 
            
                screen.blit(imgInit.situation2_pass, (50,10))
                pygame.display.flip()
            else:   
                tries += 1
                # reply
                pygame.draw.rect(screen, output_color, output_rect)
                output_text_surface = base_font.render("Sweet! Tonight's gonna be lit!", True, (255, 255, 255))  
                screen.blit(output_text_surface, (output_rect.x+5, output_rect.y+5))
                output_rect.w = max(100, output_text_surface.get_width()+10)
                clock.tick(60)  

                screen.blit(imgInit.situation2_fail, (50,10))
                pygame.display.flip()

    if level3: #initialize level setting
        while True:
            screen.blit(imgInit.lp_img,(i,0))
            screen.blit(imgInit.classroom_img,(SCREEN_WIDTH + i,0))
            if(i==-SCREEN_WIDTH):
                break
            i -= 0.5 
            mixer.music.load('audio/Classroom.mp3')
            mixer.music.set_volume(0.5)
            mixer.music.play()

            pygame.display.update()   
       
        screen.blit(main,(75,300))
        screen.blit(teacher,(800,300))

        # draw rectangle and argument passed which should be on screen
        pygame.draw.rect(screen, input_color, input_rect)
        input_text_surface = base_font.render(user_text, True, (255, 255, 255))
        screen.blit(input_text_surface, (input_rect.x+5, input_rect.y+5))
        input_rect.w = max(100, input_text_surface.get_width()+10)
        clock.tick(60)

        if replied == False: #before response is typed
            #replying user
            pygame.draw.rect(screen, output_color, output_rect)
            output_text_surface = base_font.render("What are the negative effects of marijuana smoke on the human body?", True, (255, 255, 255))
            screen.blit(output_text_surface, (output_rect.x+5, output_rect.y+5))
            output_rect.w = max(100, output_text_surface.get_width()+10)
            clock.tick(60) 

            screen.blit(imgInit.situation3_init, (50,10))
            pygame.display.flip() 

        if replied:
            if level3_reply == "Positive":
                level3_pass = True
                tries += 1
                success += 1
                # reply
                pygame.draw.rect(screen, output_color, output_rect)
                output_text_surface = base_font.render("Well said! You obviously know your stuff!", True, (255, 255, 255))
                screen.blit(output_text_surface, (output_rect.x+5, output_rect.y+5))
                output_rect.w = max(100, output_text_surface.get_width()+10)
                clock.tick(60) 
            
                screen.blit(imgInit.situation3_pass, (50,10))
                pygame.display.flip()
            else:   
                tries += 1
                # reply
                pygame.draw.rect(screen, output_color, output_rect)
                output_text_surface = base_font.render("Hmm... Not sure about that one.", True, (255, 255, 255))  
                screen.blit(output_text_surface, (output_rect.x+5, output_rect.y+5))
                output_rect.w = max(100, output_text_surface.get_width()+10)
                clock.tick(60)  

                screen.blit(imgInit.situation3_fail, (50,10))
                pygame.display.flip()
    
    if home:
        screen.blit(imgInit.lp_img,lp_rect)
        pygame.display.update()
        i=0                   

        #endscreen
        if (level1_pass and level2_pass and level3_pass):
            print("ALL PASSED")
            print(success, tries)
            score = round(((success)/tries)*100)
            if score > 60:
                endScreenText = "%"+" Great work! Stay strong to your values as you navigate through adolescence."
            else:
                endScreenText = "%"+" It took you a few tries but you made good decisions in the end!"  
            
            pygame.draw.rect(screen, input_color, input_rect)
            input_text_surface = base_font.render(str(score) + endScreenText, True, (255, 255, 255))
            screen.blit(input_text_surface, (input_rect.x+5, input_rect.y+5))
            input_rect.w = max(100, input_text_surface.get_width()+10)
            pygame.display.flip() 
            clock.tick(60)

pygame.quit()