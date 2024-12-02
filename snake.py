import pygame
import time
import random

pygame.init()

color1 = (255,255,255)
color2 = (255,255,102)
color3 = (0,255,0)
color4 = (0,0,0)
color5 = (102,255,255)
color6 = (255,0,255)

game_len = 500
game_height = 360


add_cap = pygame.display.set_mode((game_len, game_height))
pygame.display.set_caption("Snake Game")

timer = pygame.time.Clock()

snake_block = 10
snake_speed = 10

display_style = pygame.font.SysFont("arial",20,"bold")
score_font = pygame.font.SysFont("arial",15,"bold")

def final_score(score):
    value = score_font.render("Enjoy the Snake Game ------ Your Score is : " + str(score), True, color2)
    add_cap.blit(value, [0,0])

def make_snake(snake_block, list_snake):
    for x in list_snake:
        pygame.draw.rect(add_cap, color3, [x[0], x[1], snake_block, snake_block])

def display_msg(msg, color):
    mssg = display_style.render(msg, True, color)
    add_cap.blit(mssg, [game_len/6, game_height/3])

def game_start():
    game_over = False
    game_close = False

    value_x1 = game_len/2
    value_y1 = game_height/2

    new_x1 = 0
    new_y1 = 0

    list_snake = []
    snake_len = 1

    foodx_pos = round(random.randrange(0, game_len-snake_block)/10.0) * 10.0
    foody_pos = round(random.randrange(0, game_height-snake_block)/10.0) * 10.0

    while not game_over:

        while game_close == True:
            add_cap.fill(color6)
            display_msg("You lost! wanna play again, Press C. To Quit, Press Q", color4)
            final_score(snake_len-1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_start()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and new_x1 != snake_block:
                    new_x1 = -snake_block
                    new_y1 = 0
                elif event.key == pygame.K_RIGHT and new_x1 != -snake_block:
                    new_x1 = snake_block
                    new_y1 = 0
                elif event.key == pygame.K_UP and new_y1 != snake_block:
                    new_y1 = -snake_block
                    new_x1 = 0
                elif event.key == pygame.K_DOWN and new_y1 != -snake_block:
                    new_y1 = snake_block
                    new_x1 = 0

        if value_x1>=game_len or value_x1<0 or value_y1>=game_height or value_y1<0:
            game_close = True

        value_x1 = value_x1+new_x1
        value_y1 = value_y1+new_y1
        add_cap.fill(color6)
        pygame.draw.rect(add_cap, color5, [foodx_pos, foody_pos, snake_block, snake_block])
        snake_head = []
        snake_head.append(value_x1)
        snake_head.append(value_y1)
        list_snake.append(snake_head)
        if len(list_snake) > snake_len:
            del list_snake[0]

        for x in list_snake[:-1]:
            if x == snake_head:
                game_close =True

        make_snake(snake_block, list_snake)
        final_score(snake_len-1)

        pygame.display.update()

        if value_x1 == foodx_pos and value_y1 == foody_pos:
            foodx_pos = round(random.randrange(0, game_len-snake_block)/10.0) * 10.0
            foody_pos = round(random.randrange(0, game_height-snake_block)/10.0) * 10.0
            snake_len += 1

        timer.tick(snake_speed)
    pygame.quit()
    quit()

game_start()