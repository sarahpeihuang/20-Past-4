import pygame
from pygame import mixer
import cohereFn


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

situation1_init = pygame.image.load('Situation_1_init.png')
situation1_init = pygame.transform.scale(situation1_init,(width-100,height/4))
screen.blit(situation1_init, (50,10))

situation1_fail = pygame.image.load('sit1 fail.jpg')
situation1_fail = pygame.transform.scale(situation1_fail,(width-100,height/4))
screen.blit(situation1_fail, (50,10))

situation1_pass = pygame.image.load('sit1_pass.jpg')
situation1_pass = pygame.transform.scale(situation1_pass,(width-100,height/4))
screen.blit(situation1_pass, (50,10))

situation2_init = pygame.image.load('Situation_2.png')
situation2_init = pygame.transform.scale(situation2_init,(width-100,height/4))
screen.blit(situation2_init, (50,10))

situation2_fail = pygame.image.load('Situation_2_WRONG.png')
situation2_fail = pygame.transform.scale(situation2_fail,(width-100,height/4))
screen.blit(situation2_fail, (50,10))

situation2_pass = pygame.image.load('Situation_2_CORRECT.png')
situation2_pass = pygame.transform.scale(situation2_pass,(width-100,height/4))
screen.blit(situation2_pass, (50,10))

situation3_init = pygame.image.load('sit3.jpg')
situation3_init = pygame.transform.scale(situation3_init,(width-100,height/4))
screen.blit(situation3_init, (50,10))

situation3_fail = pygame.image.load('Situation 3 INCORRECT.png')
situation3_fail = pygame.transform.scale(situation3_fail,(width-100,height/4))
screen.blit(situation3_fail, (50,10))

situation3_pass = pygame.image.load('Situation_3_CORRECT.png')
situation3_pass = pygame.transform.scale(situation3_pass,(width-100,height/4))
screen.blit(situation3_pass, (50,10))

main = pygame.image.load('main.png')
main = pygame.transform.scale(main,(100,250))

second = pygame.image.load('second.png')
second = pygame.transform.scale(second,(100,250))

third = pygame.image.load('third.png')
third = pygame.transform.scale(third,(250,250))

fourth = pygame.image.load('fourth.png')
fourth = pygame.transform.scale(fourth,(150,300))

teacher = pygame.image.load('teacher.png')
teacher = pygame.transform.scale(teacher,(250,250))
pygame.display.flip()

#initialize music
mixer.music.load('intro.mp3')
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

active = False

running = True
washroom = False
party = False
classroom = False

level1 = False
level2 = False
level3 = False
home = False
replied = False

level1_pass = False
level2_pass = False
level3_pass = False

tries = 0
fails = 0

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
            if event.key == pygame.K_TAB: #landing page
                washroom = True
                home = True
                level1 = False
                level2 = False
                level3 = False    
                replied = False
            # Check for backspace
            if event.key == pygame.K_BACKSPACE:
                # get text input from 0 to -1 i.e. end.
                user_text = user_text[:-1]
  
            else:
                user_text += event.unicode
                #print("+++++++"+str(user_text))

            if event.key == pygame.K_RETURN:
                replied = True
                if level1:
                    level1_reply = cohereFn.washroomResponse(user_text)
                if level2:
                    level2_reply = cohereFn.partyResponse(user_text)
                if level3:   
                    level3_reply = cohereFn.classroomResponse(user_text)
                user_text = ''
    clock.tick(60)      

    #game logic
    if active:
        input_color = input_color_active
    else:
        input_color = input_color_passive

    if washroom == False:#home page upward transition
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

        screen.blit(main,(75,300))
        screen.blit(second,(1000,325))


        # draw rectangle and argument passed which should be on screen
        pygame.draw.rect(screen, input_color, input_rect)
        input_text_surface = base_font.render(user_text, True, (255, 255, 255))
        screen.blit(input_text_surface, (input_rect.x+5, input_rect.y+5))
        input_rect.w = max(100, input_text_surface.get_width()+10)
        pygame.display.flip() 
        clock.tick(60)

        if replied == False: #before response is typed
            #replying user
            pygame.draw.rect(screen, output_color, output_rect)
            output_text_surface = base_font.render("Hey bro, want to take a hit (inhaling one puff of marijuana)?", True, (255, 255, 255))
            screen.blit(output_text_surface, (output_rect.x+5, output_rect.y+5))
            output_rect.w = max(100, output_text_surface.get_width()+10)
            pygame.display.flip() 
            clock.tick(60) 

            screen.blit(situation1_init, (50,10))
            pygame.display.flip()

        if replied:
            if level1_reply == "Positive":
                level1_pass = True
                tries += 1
                # reply
                pygame.draw.rect(screen, output_color, output_rect)
                output_text_surface = base_font.render("Okay, whatever makes you comfortable!", True, (255, 255, 255))
                screen.blit(output_text_surface, (output_rect.x+5, output_rect.y+5))
                output_rect.w = max(100, output_text_surface.get_width()+10)
                pygame.display.flip() 
                clock.tick(60) 
            
                screen.blit(situation1_pass, (50,10))   
                pygame.display.flip()
            else:  
                tries += 1
                fails += 1 
                # reply
                pygame.draw.rect(screen, output_color, output_rect)
                output_text_surface = base_font.render("Here you go.", True, (255, 255, 255))  
                screen.blit(output_text_surface, (output_rect.x+5, output_rect.y+5))
                output_rect.w = max(100, output_text_surface.get_width()+10)
                pygame.display.flip() 
                clock.tick(60)  

                screen.blit(situation1_fail, (50,10))
                pygame.display.flip()

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

        screen.blit(main,(75,300))
        screen.blit(second,(500,325))
        screen.blit(third,(600,400))
        screen.blit(fourth,(850,300))

        # draw rectangle and argument passed which should be on screen
        pygame.draw.rect(screen, input_color, input_rect)
        input_text_surface = base_font.render(user_text, True, (255, 255, 255))
        screen.blit(input_text_surface, (input_rect.x+5, input_rect.y+5))
        input_rect.w = max(100, input_text_surface.get_width()+10)
        pygame.display.flip() 
        clock.tick(60)

        if replied == False: #before response is typed
            #replying user
            pygame.draw.rect(screen, output_color, output_rect)
            output_text_surface = base_font.render("Woah, the smoke looks so cool, let’s smoke!", True, (255, 255, 255))
            screen.blit(output_text_surface, (output_rect.x+5, output_rect.y+5))
            output_rect.w = max(100, output_text_surface.get_width()+10)
            pygame.display.flip() 
            clock.tick(60) 

            screen.blit(situation2_init, (50,10))
            pygame.display.flip() 

        if replied:
            if level2_reply == "Positive":
                level2_pass = True
                tries += 1
                # reply
                pygame.draw.rect(screen, output_color, output_rect)
                output_text_surface = base_font.render("I guess my head hurts a bit, we can step out.", True, (255, 255, 255))
                screen.blit(output_text_surface, (output_rect.x+5, output_rect.y+5))
                output_rect.w = max(100, output_text_surface.get_width()+10)
                pygame.display.flip() 
                clock.tick(60) 
            
                screen.blit(situation2_pass, (50,10))
                pygame.display.flip()
            else:   
                tries += 1
                fails += 1                 
                # reply
                pygame.draw.rect(screen, output_color, output_rect)
                output_text_surface = base_font.render("Sweet! Tonight's gonna be lit!", True, (255, 255, 255))  
                screen.blit(output_text_surface, (output_rect.x+5, output_rect.y+5))
                output_rect.w = max(100, output_text_surface.get_width()+10)
                pygame.display.flip() 
                clock.tick(60)  

                screen.blit(situation2_fail, (50,10))
                pygame.display.flip()

    if level3:
        while True:
            screen.blit(lp_img,(i,0))
            screen.blit(classroom_img,(width + i,0))
            if(i==-width):
                break
            i -= 0.5 
            mixer.music.load('classroom.mp3')
            pygame.display.update()   
       
        screen.blit(main,(75,300))
        screen.blit(teacher,(800,300))

        # draw rectangle and argument passed which should be on screen
        pygame.draw.rect(screen, input_color, input_rect)
        input_text_surface = base_font.render(user_text, True, (255, 255, 255))
        screen.blit(input_text_surface, (input_rect.x+5, input_rect.y+5))
        input_rect.w = max(100, input_text_surface.get_width()+10)
        pygame.display.flip() 
        clock.tick(60)

        if replied == False: #before response is typed
            #replying user
            pygame.draw.rect(screen, output_color, output_rect)
            output_text_surface = base_font.render("What are the negative effects of marijuana smoke on the human body?", True, (255, 255, 255))
            screen.blit(output_text_surface, (output_rect.x+5, output_rect.y+5))
            output_rect.w = max(100, output_text_surface.get_width()+10)
            pygame.display.flip() 
            clock.tick(60) 

            screen.blit(situation3_init, (50,10))
            pygame.display.flip() 

        if replied:
            if level3_reply == "Positive":
                level3_pass = True
                tries += 1
                # reply
                pygame.draw.rect(screen, output_color, output_rect)
                output_text_surface = base_font.render("Well said! You obviously know your stuff!", True, (255, 255, 255))
                screen.blit(output_text_surface, (output_rect.x+5, output_rect.y+5))
                output_rect.w = max(100, output_text_surface.get_width()+10)
                pygame.display.flip() 
                clock.tick(60) 
            
                screen.blit(situation3_pass, (50,10))
                pygame.display.flip()
            else:   
                tries += 1
                fails += 1                 
                # reply
                pygame.draw.rect(screen, output_color, output_rect)
                output_text_surface = base_font.render("Hmm... Not sure about that one.", True, (255, 255, 255))  
                screen.blit(output_text_surface, (output_rect.x+5, output_rect.y+5))
                output_rect.w = max(100, output_text_surface.get_width()+10)
                pygame.display.flip() 
                clock.tick(60)  

                screen.blit(situation3_fail, (50,10))
                pygame.display.flip()
    
    if home:
        screen.blit(lp_img,lp_rect)
        pygame.display.update()
        i=0                   

        if (level1_pass and level2_pass and level3_pass):
            print("ALL PASSED")
            #narrarator line 1
            score = ((fails/tries)*100)
            if score > 60:
                endScreenText = "%"+" Great work! You know your stuff. Stay strong to your values as you navigate through adolescence."
            else:
                endScreenText = "%"+" It took you a few tries but you made good decisions in the end! Stay strong to your values as you navigate through adolescence."  
            
            pygame.draw.rect(screen, input_color, input_rect)
            input_text_surface = base_font.render(str(score) + endScreenText, True, (255, 255, 255))
            screen.blit(input_text_surface, (input_rect.x+5, input_rect.y+5))
            input_rect.w = max(100, input_text_surface.get_width()+10)
            pygame.display.flip() 
            clock.tick(60)
            #line 2
            
            pygame.draw.rect(screen, output_color,input_rect)
            output_text_surface = base_font.render("You completed all the levels successfully!", True, (255, 255, 255))
            screen.blit(output_text_surface, (output_rect.x+5, output_rect.y+5))
            output_rect.w = max(100,output_text_surface.get_width()+10)
            pygame.display.flip()
            clock.tick(60)


pygame.quit()