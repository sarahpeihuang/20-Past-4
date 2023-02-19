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

situation1_init = pygame.image.load('sit1 fail.jpg')
situation1_init = pygame.transform.scale(situation1_init,(width-100,height/3))
situation1_init_rect = situation1_init.get_rect()
screen.blit(situation1_init, (50,50))

situation1_fail = pygame.image.load('classroom.jpg')
situation1_fail = pygame.transform.scale(situation1_fail,(width-100,height/3))
screen.blit(situation1_fail, (50,50))

situation1_pass = pygame.image.load('classroom.jpg')
situation1_pass = pygame.transform.scale(situation1_pass,(width-100,height/3))
situation1_pass_rect = situation1_pass.get_rect()

situation2_init = pygame.image.load('classroom.jpg')
situation2_init = pygame.transform.scale(situation2_init,(width-100,height/3))
situation2_init_rect = situation2_init.get_rect()

situation2_fail = pygame.image.load('classroom.jpg')
situation2_fail = pygame.transform.scale(situation2_fail,(width-100,height/3))
situation2_fail_rect = situation2_fail.get_rect()

situation2_pass = pygame.image.load('classroom.jpg')
situation2_pass = pygame.transform.scale(situation2_pass,(width-100,height/3))
situation2_pass_rect = situation2_pass.get_rect()

situation3_init = pygame.image.load('classroom.jpg')
situation3_init = pygame.transform.scale(situation3_init,(width-100,height/3))
situation3_init_rect = situation3_init.get_rect()

situation3_fail = pygame.image.load('classroom.jpg')
situation3_fail = pygame.transform.scale(situation3_fail,(width-100,height/3))
situation3_fail_rect = situation3_fail.get_rect()

situation3_pass = pygame.image.load('classroom.jpg')
situation3_pass = pygame.transform.scale(situation3_pass,(width-100,height/3))
situation3_pass_rect = situation3_pass.get_rect()

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

output_rect = pygame.Rect(500,250,140,32)
output_color = pygame.Color('orange')

n_rect1 = pygame.Rect(50, 50, 140, 32)
n_rect2 = pygame.Rect(50, 82, 140, 32)
n_rect3 = pygame.Rect(50, 114, 140, 32)
n_rect4 = pygame.Rect(50, 146, 140, 32)
n_color = pygame.Color('purple')

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

            #narrarator line 1
            pygame.draw.rect(screen, n_color,n_rect1)
            n_text_surface = base_font.render("After a long morning class, you need to take a quick break before the rest of the day. You walk into the", True, (255, 255, 255))
            screen.blit(n_text_surface, (n_rect1.x+5, n_rect1.y+5))
            n_rect1.w = max(100,n_text_surface.get_width()+10)
            pygame.display.flip()
            clock.tick(6) 
            #line 2
            pygame.draw.rect(screen, n_color,n_rect2)
            n_text_surface = base_font.render("washroom and to your surprise, there is smoke everywhere. Once the smoke slowly cleared up,", True, (255, 255, 255))
            screen.blit(n_text_surface, (n_rect2.x+5, n_rect2.y+5))
            n_rect2.w = max(100,n_text_surface.get_width()+10)
            pygame.display.flip() 
            clock.tick(7)
            #line 3
            pygame.draw.rect(screen, n_color,n_rect3)
            n_text_surface = base_font.render("you turn to see a classmate taking a puff out of his joint (crushed cannabis in tobacco wrapper).", True, (255, 255, 255))
            screen.blit(n_text_surface, (n_rect3.x+5, n_rect3.y+5))
            n_rect3.w = max(100,n_text_surface.get_width()+10)
            pygame.display.flip() 
            clock.tick(8) 
            #line 4
            pygame.draw.rect(screen, n_color,n_rect4)
            n_text_surface = base_font.render(" TYPE YOUR RESPONSE BELOW.", True, (255, 255, 255))
            screen.blit(n_text_surface, (n_rect4.x+5, n_rect4.y+5))
            n_rect4.w = max(100,n_text_surface.get_width()+10)
            pygame.display.flip() 
            clock.tick(9)

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
                clock.tick(1) 
            
                #narrarator line 1
                pygame.draw.rect(screen, n_color,n_rect1)
                n_text_surface = base_font.render("That’s right! Peer pressure is a difficult issue to overcome, but you got this. It is important to respect", True, (255, 255, 255))
                screen.blit(n_text_surface, (n_rect1.x+5, n_rect1.y+5))
                n_rect1.w = max(100,n_text_surface.get_width()+10)
                pygame.display.flip() 
                clock.tick(50) 
                #line 2
                pygame.draw.rect(screen, n_color,n_rect2)
                n_text_surface = base_font.render("your personal body and health, while knowing your limits when dealing with peer influence.", True, (255, 255, 255))
                screen.blit(n_text_surface, (n_rect2.x+5, n_rect2.y+5))
                n_rect2.w = max(100,n_text_surface.get_width()+10)
                pygame.display.flip()
                clock.tick(2)
                #line 3
                pygame.draw.rect(screen, n_color,n_rect3)
                n_text_surface = base_font.render("PRESS TAB TO RETURN TO THE MAP AND GO TO LEVEL 2.", True, (255, 255, 255))
                screen.blit(n_text_surface, (n_rect3.x+5, n_rect3.y+5))
                n_rect3.w = max(100,n_text_surface.get_width()+10)
                pygame.display.flip()
                clock.tick(49)
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

                screen.blit(situation1_fail, (50,50))
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

            #narrarator line 1
            pygame.draw.rect(screen, n_color,n_rect1)
            n_text_surface = base_font.render("You are invited to a party on a Friday night. After being in the room for over an hour,", True, (255, 255, 255))
            screen.blit(n_text_surface, (n_rect1.x+5, n_rect1.y+5))
            n_rect1.w = max(100,n_text_surface.get_width()+10)
            pygame.display.flip()
            clock.tick(6) 
            #line 2
            pygame.draw.rect(screen, n_color,n_rect2)
            n_text_surface = base_font.render("it is filled with smoke from all the joints (crushed cannabis in tobacco wrapper)", True, (255, 255, 255))
            screen.blit(n_text_surface, (n_rect2.x+5, n_rect2.y+5))
            n_rect2.w = max(100,n_text_surface.get_width()+10)
            pygame.display.flip() 
            clock.tick(6)
            #line 3
            pygame.draw.rect(screen, n_color,n_rect3)
            n_text_surface = base_font.render("You want to breathe some fresh air and step outside, but your friend wants to stay", True, (255, 255, 255))
            screen.blit(n_text_surface, (n_rect3.x+5, n_rect3.y+5))
            n_rect3.w = max(100,n_text_surface.get_width()+10)
            pygame.display.flip() 
            clock.tick(6) 
            #line 4
            pygame.draw.rect(screen, n_color,n_rect4)
            n_text_surface = base_font.render("where they are and resume smoking. TYPE YOUR RESPONSE BELOW.", True, (255, 255, 255))
            screen.blit(n_text_surface, (n_rect4.x+5, n_rect4.y+5))
            n_rect4.w = max(100,n_text_surface.get_width()+10)
            pygame.display.flip() 
            clock.tick(6)

        if replied:
            if level1_reply == "Positive":
                level2_pass = True
                tries += 1
                # reply
                pygame.draw.rect(screen, output_color, output_rect)
                output_text_surface = base_font.render("I guess my head hurts a bit, we can step out.", True, (255, 255, 255))
                screen.blit(output_text_surface, (output_rect.x+5, output_rect.y+5))
                output_rect.w = max(100, output_text_surface.get_width()+10)
                pygame.display.flip() 
                clock.tick(60) 
            
                #narrarator line 1
                pygame.draw.rect(screen, n_color,n_rect1)
                n_text_surface = base_font.render("You’ve got it! You have detected the toxic environment, removed yourself from the poor air quality,", True, (255, 255, 255))
                screen.blit(n_text_surface, (n_rect1.x+5, n_rect1.y+5))
                n_rect1.w = max(100,n_text_surface.get_width()+10)
                pygame.display.flip() 
                clock.tick(60) 
                #line 2
                pygame.draw.rect(screen, n_color,n_rect2)
                n_text_surface = base_font.render("and encouraged your friend to stop smoking. In fact, it is estimated that indoor cannabis emits", True, (255, 255, 255))
                screen.blit(n_text_surface, (n_rect2.x+5, n_rect2.y+5))
                n_rect2.w = max(100,n_text_surface.get_width()+10)
                pygame.display.flip()
                clock.tick(60)
                #line 3
                pygame.draw.rect(screen, n_color,n_rect3)
                n_text_surface = base_font.render("as much CO2 emissions as an additional 3.3 million cars on the road each year.", True, (255, 255, 255))
                screen.blit(n_text_surface, (n_rect3.x+5, n_rect3.y+5))
                n_rect3.w = max(100,n_text_surface.get_width()+10)
                pygame.display.flip()
                clock.tick(60)
                #line 3
                pygame.draw.rect(screen, n_color,n_rect4)
                n_text_surface = base_font.render("PRESS TAB TO RETURN TO THE MAP AND GO TO LEVEL 2.", True, (255, 255, 255))
                screen.blit(n_text_surface, (n_rect4.x+5, n_rect4.y+5))
                n_rect4.w = max(100,n_text_surface.get_width()+10)
                pygame.display.flip()
                clock.tick(60)
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

                #narrarator line 1
                pygame.draw.rect(screen, n_color,n_rect1)
                n_text_surface = base_font.render("Don’t forget to assess the polluted environment and address it. Please try again.", True, (255, 255, 255))
                screen.blit(n_text_surface, (n_rect1.x+5, n_rect1.y+5))
                n_rect1.w = max(100,n_text_surface.get_width()+10)
                pygame.display.flip() 
                clock.tick(60) 
                #line 2
                pygame.draw.rect(screen, n_color,n_rect2)
                n_text_surface = base_font.render("PRESS TAB TO RETURN TO THE MAP AND RETRY LEVEL 2.", True, (255, 255, 255))
                screen.blit(n_text_surface, (n_rect2.x+5, n_rect2.y+5))
                n_rect2.w = max(100,n_text_surface.get_width()+10)
                pygame.display.flip()
                clock.tick(60)

    if level3:
        while True:
            screen.blit(lp_img,(i,0))
            screen.blit(classroom_img,(width + i,0))
            if(i==-width):
                break
            i -= 0.5 
            mixer.music.load('classroom.mp3')
            pygame.display.update()   
       

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

            #narrarator line 1
            pygame.draw.rect(screen, n_color,n_rect1)
            n_text_surface = base_font.render("After a long morning class, you need to take a quick break before the rest of the day. You walk into the", True, (255, 255, 255))
            screen.blit(n_text_surface, (n_rect1.x+5, n_rect1.y+5))
            n_rect1.w = max(100,n_text_surface.get_width()+10)
            pygame.display.flip()
            clock.tick(6) 
            #line 2
            pygame.draw.rect(screen, n_color,n_rect2)
            n_text_surface = base_font.render("washroom and to your surprise, there is smoke everywhere. Once the smoke slowly cleared up,", True, (255, 255, 255))
            screen.blit(n_text_surface, (n_rect2.x+5, n_rect2.y+5))
            n_rect2.w = max(100,n_text_surface.get_width()+10)
            pygame.display.flip() 
            clock.tick(7)
            #line 3
            pygame.draw.rect(screen, n_color,n_rect3)
            n_text_surface = base_font.render("you turn to see a classmate taking a puff out of his joint (crushed cannabis in tobacco wrapper).", True, (255, 255, 255))
            screen.blit(n_text_surface, (n_rect3.x+5, n_rect3.y+5))
            n_rect3.w = max(100,n_text_surface.get_width()+10)
            pygame.display.flip() 
            clock.tick(8) 
            #line 4
            pygame.draw.rect(screen, n_color,n_rect4)
            n_text_surface = base_font.render(" TYPE YOUR RESPONSE BELOW.", True, (255, 255, 255))
            screen.blit(n_text_surface, (n_rect4.x+5, n_rect4.y+5))
            n_rect4.w = max(100,n_text_surface.get_width()+10)
            pygame.display.flip() 
            clock.tick(9)

        if replied:
            if level1_reply == "Positive":
                level3_pass == True
                tries += 1
                # reply
                pygame.draw.rect(screen, output_color, output_rect)
                output_text_surface = base_font.render("Well said! You obviously know your stuff!", True, (255, 255, 255))
                screen.blit(output_text_surface, (output_rect.x+5, output_rect.y+5))
                output_rect.w = max(100, output_text_surface.get_width()+10)
                pygame.display.flip() 
                clock.tick(1) 
            
                #narrarator line 1
                pygame.draw.rect(screen, n_color,n_rect1)
                n_text_surface = base_font.render("That’s right! Peer pressure is a difficult issue to overcome, but you got this. It is important to respect", True, (255, 255, 255))
                screen.blit(n_text_surface, (n_rect1.x+5, n_rect1.y+5))
                n_rect1.w = max(100,n_text_surface.get_width()+10)
                pygame.display.flip() 
                clock.tick(50) 
                #line 2
                pygame.draw.rect(screen, n_color,n_rect2)
                n_text_surface = base_font.render("your personal body and health, while knowing your limits when dealing with peer influence.", True, (255, 255, 255))
                screen.blit(n_text_surface, (n_rect2.x+5, n_rect2.y+5))
                n_rect2.w = max(100,n_text_surface.get_width()+10)
                pygame.display.flip()
                clock.tick(2)
                #line 3
                pygame.draw.rect(screen, n_color,n_rect3)
                n_text_surface = base_font.render("PRESS TAB TO RETURN TO THE MAP AND GO TO LEVEL 2.", True, (255, 255, 255))
                screen.blit(n_text_surface, (n_rect3.x+5, n_rect3.y+5))
                n_rect3.w = max(100,n_text_surface.get_width()+10)
                pygame.display.flip()
                clock.tick(49)
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

                #narrarator line 1
                pygame.draw.rect(screen, n_color,n_rect1)
                n_text_surface = base_font.render("Remember to not succumb to peer pressure. Please try again.", True, (255, 255, 255))
                screen.blit(n_text_surface, (n_rect1.x+5, n_rect1.y+5))
                n_rect1.w = max(100,n_text_surface.get_width()+10)
                pygame.display.flip() 
                clock.tick(6) 
                #line 2
                pygame.draw.rect(screen, n_color,n_rect2)
                n_text_surface = base_font.render("PRESS TAB TO RETURN TO THE MAP AND RETRY LEVEL 1.", True, (255, 255, 255))
                screen.blit(n_text_surface, (n_rect2.x+5, n_rect2.y+5))
                n_rect2.w = max(100,n_text_surface.get_width()+10)
                pygame.display.flip()
                clock.tick(7)
    
    if home:
        screen.blit(lp_img,lp_rect)
        pygame.display.update()
        i=0                   

        if (level1_pass and level2_pass) and (level2_pass and level3_pass):
            print("ALL PASSED")
            #narrarator line 1
            pygame.draw.rect(screen, n_color,n_rect1)
            n_text_surface = base_font.render("You completed all the levels successfully!", True, (255, 255, 255))
            screen.blit(n_text_surface, (n_rect1.x+5, n_rect1.y+5))
            n_rect1.w = max(100,n_text_surface.get_width()+10)
            pygame.display.flip()
            clock.tick(6) 
            #line 2
            score = (fails/tries)*100
            if score > 60:
                endScreenText = "%"+" Great work! You know your stuff. Stay strong to your values as you navigate through adolescence."
            else:
                endScreenText = "%"+" It took you a few tries but you made good decisions in the end! Stay strong to your values as you navigate through adolescence."  
            pygame.draw.rect(screen, n_color,n_rect2)
            n_text_surface = base_font.render(endScreenText, True, (255, 255, 255))
            screen.blit(n_text_surface, (n_rect2.x+5, n_rect2.y+5))
            n_rect2.w = max(100,n_text_surface.get_width()+10)
            pygame.display.flip()
            clock.tick(2)


pygame.quit()