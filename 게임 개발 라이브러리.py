import pygame
import os
#파이게임 초기화
pygame.init()

#게임이름 정하기
pygame.display.set_caption("pygame")

#스크린 사이즈 정하기
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#스크린 정의
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#색 정의
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

#주사율
clock = pygame.time.Clock()

#게임 종료 전까지 반복]
done = False

#assets경로 설정
current_path = os.path.dirname(__file__)
#오디오경로설정
assests_path = os.path.join(current_path, 'pyaudio')
#이미지경로설정
assests_image = os.path.join(current_path, 'pyimage')

#이미지 설정
start_image = pygame.image.load((os.path.join(assests_image, 'start.png')))

#배경음악
pygame.mixer.music.load(os.path.join(assests_path, 'prototype_background music.wav'))
pygame.mixer.music.play(-1)#배경음악 무한반복

#게임반복구간
while not done:
    #이벤트 반복구간 
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            done = True

    #스크린 색 정의
    screen.fill(blue)

    #이미지 업로드

    screen.blit(start_image, [390, 300])
    #화면 업데이트
    pygame.display.flip()
    
    #주사율 결정
    clock.tick(60)

#게임종료
pygame.quit()