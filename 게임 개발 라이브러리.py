import pygame
import os
import random
import sys

import pygame.tests
#파이게임 초기화
pygame.init()

#게임이름 정하기
pygame.display.set_caption("pygame_prototype")

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
random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

#주사율
clock = pygame.time.Clock()

#게임 종료 전까지 반복]
screen_state = 'start'
done = False
left = 1
right = 0
#assets경로 설정
current_path = os.path.dirname(__file__)
#오디오경로설정
assests_path = os.path.join(current_path, 'pyaudio')
#이미지경로설정
assests_image = os.path.join(current_path, 'pyimage')

#텍스트 폰트 설정
font = pygame.font.SysFont("D2Coding", 30, True, False)

texts = font.render("press space key", True, blue)

print(texts.get_size())
texts_x = 255/2
texts_y = 33/2



#이미지 설정
start_image = pygame.image.load((os.path.join(assests_image, 'start_butten.png')))
start_image_s = pygame.transform.scale(start_image, (200, 100))
start_image_rect =start_image_s.get_rect()
width = start_image_s.get_width()
height = start_image_s.get_height()

image = pygame.image.load((os.path.join(assests_image, 'pygame.backimage.png')))

empty_image = pygame.Surface((width, height))
empty_image.fill(white) 
#배경음악
music = pygame.mixer.music.load(os.path.join(assests_path, 'prototype_background music.wav'))
startmusic = pygame.mixer.Sound("start.wav")
background = screen.fill(white)
current_screen = 1
#게임반복구간

while not done:
    #이벤트 반복구간 
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            current_screen = 2
        if current_screen == 2:
            screen.blit(image, [0, 0])
            pygame.display.flip()
            pygame.mixer.music.stop()
            pygame.mixer.music.load(os.path.join(assests_path, 'start.wav'))
            pygame.mixer.music.play(-1)
            pygame.tests
            screen.blit(texts, (400-texts_x, 299-texts_y))
        else:
            width = start_image_s.get_width()
            height = start_image_s.get_height()
            screen.fill(black) 
            screen.blit(start_image_s, [300, 300])
            pygame.mixer.music.play(-1)#배경음악 재생
    #화면 업데이트
    pygame.display.flip()
    
    #주사율 결정
    clock.tick(60)

#게임종료
pygame.quit()