#Quiz) 하늘에서 떨어지는 똥 피하기 게임

#Rule:
# 1. 케릭터는 화면 가장 아래에 위치, 좌우로만 이동가능
# 2. 똥은 화면 가장 위에서 떨어짐, x좌표는 매번 랜덤으로 설정
# 3. 캐릭터가 똥을 피하면 다음 똥이 떨어짐
# 4. 캐릭터가 똥과 충돌하면 게임 종료
# 5. FPS = 30

import pygame, random
pygame.init() #mandatory to initialize

#화면 크키 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("똥 피하기 게임")

#FPS
clock = pygame.time.Clock()

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)

background = pygame.image.load("C:\\Users\\miche\\OneDrive\\Document\\Personal\\Python\\intermediate\\pygame_basic\\background.png")
character = pygame.image.load("C:\\Users\\miche\\OneDrive\\Document\\Personal\\Python\\intermediate\\pygame_basic\\character.png")
character_size = character.get_rect().size #gets image's size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width/2)
character_y_pos = screen_height - character_height #화면 세로 아래 위치

character_speed = 0.6
enemy_speed = 10

to_x = 0

enemy = pygame.image.load("C:\\Users\\miche\\OneDrive\\Document\\Personal\\Python\\intermediate\\pygame_basic\\enemy.png")
enemy_size = enemy.get_rect().size #gets image's size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0,screen_width - enemy_width) #화면 가로의 가운데 위치
enemy_y_pos = 0 #Falls from the top

#Event Loop - is game running?
running = True
while running:
    dt = clock.tick(30) #화면의 초당 프레임 수
    # print("fps: " + str(clock.get_fps()))
    
    #2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get(): #this line is mandatory when using a pygame (어떤 이벤트가 발생하면)
        if event.type == pygame.QUIT: #When the tab closes
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed #to_x = to_x - 5
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP: #방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    # 3. 캐릭터 위치 정의
    character_x_pos += to_x * dt

    #가로 경계값 처리
    if character_x_pos < 0: #grid starts from left top - so this is for left wall
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width: # screen_width would be the end of the right wall
        character_x_pos = screen_width - character_width

    enemy_y_pos += enemy_speed

    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0,screen_width - enemy_width)

    #4. 충돌처리
    
    #충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos #top of the grid (left, top)

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #충돌 체크
    if character_rect.colliderect(enemy_rect): #사각형 기준으로 충돌이 있었는지 확인
        print('충돌!')
        running = False

    #5. 화면에 그리기
    screen.blit(background, (0,0)) #top right is 0, 0 배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) #적 그리기

    pygame.display.update() # as while True loops, 계속 화면 update해줌 frame by frame

#Delay before exiting game
# pygame.time.delay(2000) #2 seconds

#pygame done
pygame.quit()