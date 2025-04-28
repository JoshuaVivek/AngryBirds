import pygame
import math

GRAVITY = 500  # some random value for gravity (i think its ok)
RESTITUTION = 0.6  # coefficient of restitution for bouncing
STOP_THRESHOLD = 30  #min velocity to stop the bird(below this value, the bird stops moving)(to ensure the bird stops moving after bouncing on the ground)

class SlingShot:
    def __init__(self, sling_pos, side):
        self.sling_x, self.sling_y = sling_pos
        self.bird = None
        self.dragging = False
        self.launched = False
        self.vx = 0
        self.vy = 0
        self.max_pull_length = 100
        self.side = side  # "left" or "right"

    def attach_bird(self, bird):
        self.bird = bird
        self.bird.x = self.sling_x
        self.bird.y = self.sling_y

    def handle_event(self, event):
        if not self.bird:
            return
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.Rect(self.bird.x, self.bird.y, 40, 40).collidepoint(event.pos) and not self.launched:
                self.dragging = True

        if event.type == pygame.MOUSEBUTTONUP:
            if self.dragging:
                self.dragging = False
                self.launched = True
                dx = self.sling_x - self.bird.x
                dy = self.sling_y - self.bird.y
                distance = math.hypot(dx, dy)
                angle = math.atan2(dy, dx)
                power = min(distance, self.max_pull_length) * 5
                self.vx = math.cos(angle) * power
                self.vy = math.sin(angle) * power

    def update(self, dt, screen_height):
        if not self.bird:
            return

        if self.dragging:
            mx, my = pygame.mouse.get_pos()
            dx = mx - self.sling_x
            dy = my - self.sling_y
            distance = math.hypot(dx, dy)
            if distance > self.max_pull_length:
                angle = math.atan2(dy, dx)
                mx = self.sling_x + self.max_pull_length * math.cos(angle)
                my = self.sling_y + self.max_pull_length * math.sin(angle)
            self.bird.x = mx
            self.bird.y = my

        if self.launched:
            self.vy += GRAVITY * dt
            self.bird.x += self.vx * dt
            self.bird.y += self.vy * dt

            # Bounce on ground
            if self.bird.y + 40 >= screen_height:
                self.bird.y = screen_height - 40
                self.vy = -self.vy * RESTITUTION
                self.vx = self.vx * RESTITUTION

            # Stop when speed very low
            speed = math.hypot(self.vx, self.vy)
            if speed < STOP_THRESHOLD:
                self.vx = 0
                self.vy = 0
                self.launched = False

    def draw_sling_lines(self, screen):
        if self.dragging:
            pygame.draw.line(screen, (0, 0, 0), (self.sling_x - 10, self.sling_y), (self.bird.x, self.bird.y), 4)
            pygame.draw.line(screen, (0, 0, 0), (self.sling_x + 10, self.sling_y), (self.bird.x, self.bird.y), 4)
