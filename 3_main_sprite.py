import pygame

pygame.init() #mandatory to initialize

#화면 크키 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Mich Game") #Game Name

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


#Event Loop - is game running?
running = True
while running:
    for event in pygame.event.get(): #this line is mandatory when using a pygame (어떤 이벤트가 발생하면)
        if event.type == pygame.QUIT: #When the tab closes
            running = False

    screen.blit(background, (0,0)) #top right is 0, 0 배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() # as while True loops, 계속 화면 update해줌 frame by frame

#pygame done
pygame.quit()