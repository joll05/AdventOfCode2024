import re
import pygame
from dataclasses import dataclass
from math import sqrt

with open("input.txt") as f:
    raw_input = f.read().rstrip()

WIDTH = 101
HEIGHT = 103
STEPS = 100

SCALE = 6

PATTERN = r"^p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)$"

@dataclass
class Robot:
    x: int
    y: int
    vx: int
    vy: int
    
    def screen_pos_at_time(self, time):
        new_x = (self.x + self.vx * time) % WIDTH
        new_y = (self.y + self.vy * time) % HEIGHT
        return pygame.Vector2(new_x * SCALE + SCALE / 2, new_y * SCALE + SCALE / 2)

robots: list[Robot] = []

for line in raw_input.splitlines():
    match = re.match(PATTERN, line)
    x, y, vx, vy = map(int, [match[i] for i in range(1, 5)])
    
    robots.append(Robot(x, y, vx, vy))

# PYGAME:

pygame.init()
screen = pygame.display.set_mode((WIDTH * SCALE, HEIGHT * SCALE))
clock = pygame.time.Clock()
running = True
font = pygame.font.Font(size=30)

paused = True
current_time = 0
speed = 3

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
            if event.key == pygame.K_LEFT:
                current_time -= 1
            if event.key == pygame.K_RIGHT:
                current_time += 1
            if event.key == pygame.K_UP:
                speed += 1
            if event.key == pygame.K_DOWN:
                speed -= 1

    if not paused:
        current_time += speed / 60
    
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    for robot in robots:
        pygame.draw.circle(screen, "dark green", robot.screen_pos_at_time(int(current_time)), SCALE / 2)
    
    text = font.render(f"{current_time}", True, "black")

    screen.blit(text, text.get_rect())
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()