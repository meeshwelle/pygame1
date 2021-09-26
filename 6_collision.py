import pygame

pygame.init() #mandatory to initialize

#화면 크키 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Mich Game") #Game Name

#FPS
clock = pygame.time.Clock()

#배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\miche\\OneDrive\\Document\\Personal\\Python\\intermediate\\pygame_basic\\background.png")

#캐릭터 불러오기
character = pygame.image.load("C:\\Users\\miche\\OneDrive\\Document\\Personal\\Python\\intermediate\\pygame_basic\\character.png")
character_size = character.get_rect().size #gets image's size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width/2) #화면 가로의 가운데 위치
character_y_pos = screen_height - character_height #화면 세로 아래 위치
#위: 왜냐면 top left corner에서 grid가 시작하듯이 캐릭터도 가운데 아래에 똑같이 시작하는 grid가 있음

#이동할 좌표
to_x = 0
to_y = 0

#이동 속도
character_speed = 0.6

#Enemy
enemy = pygame.image.load("C:\\Users\\miche\\OneDrive\\Document\\Personal\\Python\\intermediate\\pygame_basic\\enemy.png")
enemy_size = enemy.get_rect().size #gets image's size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width / 2) - (enemy_width/2) #화면 가로의 가운데 위치
enemy_y_pos = (screen_height/2) - (enemy_height/2) #화면 세로 아래 위치

#Event Loop - is game running?
running = True
while running:
    dt = clock.tick(30) #화면의 초당 프레임 수
    # print("fps: " + str(clock.get_fps()))
    
    for event in pygame.event.get(): #this line is mandatory when using a pygame (어떤 이벤트가 발생하면)
        if event.type == pygame.QUIT: #When the tab closes
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed #to_x = to_x - 5
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP: #방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    #가로 경계값 처리
    if character_x_pos < 0: #grid starts from left top - so this is for left wall
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width: # screen_width would be the end of the right wall
        character_x_pos = screen_width - character_width

    #세로 경계값 처리
    if character_y_pos < 0: #grid starts from left top - so this is for left wall
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height: # screen_width would be the end of the right wall
        character_y_pos = screen_height - character_height

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
    

    screen.blit(background, (0,0)) #top right is 0, 0 배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) #적 그리기

    pygame.display.update() # as while True loops, 계속 화면 update해줌 frame by frame

#pygame done
pygame.quit()