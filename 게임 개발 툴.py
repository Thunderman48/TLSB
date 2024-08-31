import pygame
import random
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
#주사율 정의
clock = pygame.time.Clock()
#창 닫을떄까지 반복
done = False
#반복문
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    #화면 색 정하기
    screen.fill(white)
    #화면 업데이트
    pygame.display.flip()
    #주사율 60
    clock.tick(60)
#게임종료
pygame.quit()
