import pygame
from index import SCREEN_HEIGHT,SCREEN_WIDTH

#initialize images
blk_img = pygame.image.load("images\Black.jpg")
blk_img = pygame.transform.scale(blk_img,(SCREEN_WIDTH, SCREEN_HEIGHT))

home_img = pygame.image.load('images\Home.jpg')
home_img = pygame.transform.scale(home_img,(SCREEN_WIDTH, SCREEN_HEIGHT))

lp_img = pygame.image.load('images\Landing page.jpg')
lp_img = pygame.transform.scale(lp_img,(SCREEN_WIDTH, SCREEN_HEIGHT))

classroom_img = pygame.image.load('images\Classroom.jpg')
classroom_img = pygame.transform.scale(classroom_img,(SCREEN_WIDTH, SCREEN_HEIGHT))

party_img = pygame.image.load('images\Party.jpg')
party_img = pygame.transform.scale(party_img,(SCREEN_WIDTH, SCREEN_HEIGHT))

washroom_img = pygame.image.load('images\Washroom.jpg')
washroom_img = pygame.transform.scale(washroom_img,(SCREEN_WIDTH, SCREEN_HEIGHT))

situation1_init = pygame.image.load('images\Situation_1_init.png')
situation1_init = pygame.transform.scale(situation1_init,(SCREEN_WIDTH-100,SCREEN_HEIGHT/4))

situation1_fail = pygame.image.load('images\Sit1 fail.jpg')
situation1_fail = pygame.transform.scale(situation1_fail,(SCREEN_WIDTH-100,SCREEN_HEIGHT/4))

situation1_pass = pygame.image.load('images\Sit1_pass.jpg')
situation1_pass = pygame.transform.scale(situation1_pass,(SCREEN_WIDTH-100,180))

situation2_init = pygame.image.load('images\Situation_2.png')
situation2_init = pygame.transform.scale(situation2_init,(SCREEN_WIDTH-100,SCREEN_HEIGHT/4))

situation2_fail = pygame.image.load('images\Situation_2_WRONG.png')
situation2_fail = pygame.transform.scale(situation2_fail,(SCREEN_WIDTH-100,SCREEN_HEIGHT/4))

situation2_pass = pygame.image.load('images\Situation_2_CORRECT.png')
situation2_pass = pygame.transform.scale(situation2_pass,(SCREEN_WIDTH-100,195))

situation3_init = pygame.image.load('images\Sit3.jpg')
situation3_init = pygame.transform.scale(situation3_init,(SCREEN_WIDTH-100,SCREEN_HEIGHT/4))

situation3_fail = pygame.image.load('images\Situation 3 INCORRECT.png')
situation3_fail = pygame.transform.scale(situation3_fail,(SCREEN_WIDTH-100,SCREEN_HEIGHT/4))

situation3_pass = pygame.image.load('images\Situation_3_CORRECT.png')
situation3_pass = pygame.transform.scale(situation3_pass,(SCREEN_WIDTH-100,180))

#character images
main = pygame.image.load('images\Main.png')

second = pygame.image.load('images\Second.png')

third = pygame.image.load('images\Third.png')

fourth = pygame.image.load('images\Fourth.png')

teacher = pygame.image.load('images\Teacher.png')
