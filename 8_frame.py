#This file is the bone structure for building any other pygame
import pygame
####################기본 초기화 (반드시 해야하는것들)########################
pygame.init() #mandatory to initialize

#화면 크키 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Mich Game") #Game Name

#FPS
clock = pygame.time.Clock()
###########################################################################

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)

#Event Loop - is game running?
running = True
while running:
    dt = clock.tick(30) #화면의 초당 프레임 수
    # print("fps: " + str(clock.get_fps()))
    
    #2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get(): #this line is mandatory when using a pygame (어떤 이벤트가 발생하면)
        if event.type == pygame.QUIT: #When the tab closes
            running = False

    #3. 게임 케릭터 위치 정의

    #4. 충돌처리
    
    #5. 화면에 그리기
    pygame.display.update() # as while True loops, 계속 화면 update해줌 frame by frame

#pygame done
pygame.quit()