import pygame
import math
from datetime import datetime

pygame.init()
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Analog Clock")

bg = (255, 255, 255)
hour_minute_hand = (0, 0, 0)
second_hand = (255, 0, 0)  # Red color

radius = 150
center = (width // 2, height // 2)
thickness = 4
hour_len = 80
minute_len = 120
second_len = 140

font = pygame.font.Font(None, 30)  # Font for hour numbers

def draw_hand(length, angle, color):
    x = center[0] + length * math.cos(math.radians(angle - 90))
    y = center[1] + length * math.sin(math.radians(angle - 90))
    pygame.draw.line(screen, color, center, (x, y), thickness)

def draw_clock():
    screen.fill(bg)
    pygame.draw.circle(screen, hour_minute_hand, center, radius, 3)

    for i in range(1, 13):  # Draw hour numbers
        angle = math.radians(i * 30 - 90)
        x = center[0] + (radius - 20) * math.cos(angle) - 10
        y = center[1] + (radius - 20) * math.sin(angle) - 10
        text = font.render(str(i), True, hour_minute_hand)
        screen.blit(text, (x, y))

    now = datetime.now().time()
    hour_angle = (now.hour % 12) * 30 + now.minute / 2
    minute_angle = now.minute * 6 + now.second / 10
    second_angle = now.second * 6

    draw_hand(hour_len, hour_angle, hour_minute_hand)
    draw_hand(minute_len, minute_angle, hour_minute_hand)
    draw_hand(second_len, second_angle, second_hand)  # Red color

    pygame.draw.circle(screen, hour_minute_hand, center, 5)

    pygame.display.flip()

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_clock()
    clock.tick(60)

pygame.quit()


