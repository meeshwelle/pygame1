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

#Event Loop - is game running?
running = True
while running:
    for event in pygame.event.get(): #this line is mandatory when using a pygame (어떤 이벤트가 발생하면)
        if event.type == pygame.QUIT: #When the tab closes
            running = False

    # screen.fill((0, 0, 255)) #r, g, b ->blue
    screen.blit(background, (0,0)) #top right is 0, 0 배경 그리기

    pygame.display.update() # as while True loops, 계속 화면 update해줌 frame by frame

#pygame done
pygame.quit()