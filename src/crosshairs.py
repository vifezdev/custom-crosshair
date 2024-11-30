import pygame
import math

class Crosshairs:
    def __init__(self):
        self.crosshair_methods = {
            "Circle": self.draw_circle,
            "Small Plus": self.draw_small_plus,
            "Plus": self.draw_plus,
            "X": self.draw_x,
            "Diamond": self.draw_diamond,
            "Square": self.draw_square,
            "Dot": self.draw_dot,
            "Double Cross": self.draw_double_cross,
            "Hollow Square": self.draw_hollow_square,
            "Bullseye": self.draw_bullseye,
            "Concentric Circles": self.draw_concentric_circles,
            "Triangle": self.draw_triangle,
            "Vertical Line": self.draw_vertical_line,
            "Horizontal Line": self.draw_horizontal_line,
            "Asterisk": self.draw_asterisk,
            "Hexagon": self.draw_hexagon,
            "Star": self.draw_star,
            "Chevron": self.draw_chevron,
            "Arrow": self.draw_arrow,
            "Target": self.draw_target,
            "Dashed Circle": self.draw_dashed_circle,
            "Tilted Square": self.draw_tilted_square,
        }

    def get_available_crosshairs(self):
        return list(self.crosshair_methods.keys())

    def draw_crosshair(self, screen, crosshair_type, screen_width, screen_height, color, size):
        method = self.crosshair_methods.get(crosshair_type)
        if method:
            method(screen, screen_width, screen_height, color, size)

    def draw_circle(self, screen, screen_width, screen_height, color, size):
        center_x, center_y = screen_width // 2, screen_height // 2
        pygame.draw.circle(screen, color, (center_x, center_y), size, 2)

    def draw_small_plus(self, screen, screen_width, screen_height, color, size):
        center_x, center_y = screen_width // 2, screen_height // 2
        pygame.draw.line(screen, color, (center_x - 5, center_y), (center_x + 5, center_y), 2)
        pygame.draw.line(screen, color, (center_x, center_y - 5), (center_x, center_y + 5), 2)

    def draw_plus(self, screen, screen_width, screen_height, color, size):
        center_x, center_y = screen_width // 2, screen_height // 2
        pygame.draw.line(screen, color, (center_x - size, center_y), (center_x + size, center_y), 2)
        pygame.draw.line(screen, color, (center_x, center_y - size), (center_x, center_y + size), 2)

    def draw_x(self, screen, screen_width, screen_height, color, size):
        center_x, center_y = screen_width // 2, screen_height // 2
        pygame.draw.line(screen, color, (center_x - size, center_y - size), (center_x + size, center_y + size), 2)
        pygame.draw.line(screen, color, (center_x - size, center_y + size), (center_x + size, center_y - size), 2)

    def draw_diamond(self, screen, screen_width, screen_height, color, size):
        center_x, center_y = screen_width // 2, screen_height // 2
        points = [
            (center_x, center_y - size),
            (center_x + size, center_y),
            (center_x, center_y + size),
            (center_x - size, center_y),
        ]
        pygame.draw.polygon(screen, color, points, 2)

    def draw_square(self, screen, screen_width, screen_height, color, size):
        center_x, center_y = screen_width // 2, screen_height // 2
        rect = pygame.Rect(center_x - size, center_y - size, size * 2, size * 2)
        pygame.draw.rect(screen, color, rect, 2)

    def draw_dot(self, screen, screen_width, screen_height, color, size):
        center_x, center_y = screen_width // 2, screen_height // 2
        pygame.draw.circle(screen, color, (center_x, center_y), 3)

    def draw_double_cross(self, screen, screen_width, screen_height, color, size):
        center_x, center_y = screen_width // 2, screen_height // 2
        gap = size // 4
        pygame.draw.line(screen, color, (center_x - size, center_y), (center_x + size, center_y), 2)
        pygame.draw.line(screen, color, (center_x, center_y - size), (center_x, center_y + size), 2)
        pygame.draw.line(screen, color, (center_x - gap, center_y), (center_x + gap, center_y), 2)
        pygame.draw.line(screen, color, (center_x, center_y - gap), (center_x, center_y + gap), 2)

    def draw_hollow_square(self, screen, screen_width, screen_height, color, size):
        center_x, center_y = screen_width // 2, screen_height // 2
        rect = pygame.Rect(center_x - size, center_y - size, size * 2, size * 2)
        pygame.draw.rect(screen, color, rect, 2)

    def draw_bullseye(self, screen, screen_width, screen_height, color, size):
        center_x, center_y = screen_width // 2, screen_height // 2
        for i in range(3):
            pygame.draw.circle(screen, color, (center_x, center_y), size - i * 5, 2)

    def draw_concentric_circles(self, screen, screen_width, screen_height, color, size):
        center_x, center_y = screen_width // 2, screen_height // 2
        for i in range(1, 4):
            pygame.draw.circle(screen, color, (center_x, center_y), size // i, 2)

    def draw_triangle(self, screen, screen_width, screen_height, color, size):
        center_x, center_y = screen_width // 2, screen_height // 2
        points = [
            (center_x, center_y - size),
            (center_x - size, center_y + size),
            (center_x + size, center_y + size),
        ]
        pygame.draw.polygon(screen, color, points, 2)

    def draw_vertical_line(self, screen, screen_width, screen_height, color, size):
        center_x, center_y = screen_width // 2, screen_height // 2
        pygame.draw.line(screen, color, (center_x, center_y - size), (center_x, center_y + size), 2)

    def draw_horizontal_line(self, screen, screen_width, screen_height, color, size):
        center_x, center_y = screen_width // 2, screen_height // 2
        pygame.draw.line(screen, color, (center_x - size, center_y), (center_x + size, center_y), 2)

    def draw_asterisk(self, screen, screen_width, screen_height, color, size):
        self.draw_plus(screen, screen_width, screen_height, color, size)
        self.draw_x(screen, screen_width, screen_height, color, size)

    def draw_hexagon(self, screen, screen_width, screen_height, color, size):
        center_x, center_y = screen_width // 2, screen_height // 2
        points = [
            (center_x + size, center_y),
            (center_x + size // 2, center_y - size),
            (center_x - size // 2, center_y - size),
            (center_x - size, center_y),
            (center_x - size // 2, center_y + size),
            (center_x + size // 2, center_y + size),
        ]
        pygame.draw.polygon(screen, color, points, 2)

    def draw_star(self, screen, screen_width, screen_height, color, size):
        self.draw_asterisk(screen, screen_width, screen_height, color, size)
        self.draw_double_cross(screen, screen_width, screen_height, color, size)

    def draw_chevron(self, screen, screen_width, screen_height, color, size):
        center_x, center_y = screen_width // 2, screen_height // 2
        points = [
            (center_x, center_y - size),
            (center_x + size, center_y),
            (center_x, center_y + size),
            (center_x - size, center_y),
        ]
        pygame.draw.lines(screen, color, False, points, 2)

    def draw_arrow(self, screen, screen_width, screen_height, color, size):
        center_x, center_y = screen_width // 2, screen_height // 2
        points = [
            (center_x, center_y - size),
            (center_x + size, center_y),
            (center_x + size // 2, center_y),
            (center_x + size // 2, center_y + size),
            (center_x - size // 2, center_y + size),
            (center_x - size // 2, center_y),
            (center_x - size, center_y),
        ]
        pygame.draw.polygon(screen, color, points, 2)

    def draw_target(self, screen, screen_width, screen_height, color, size):
        self.draw_circle(screen, screen_width, screen_height, color, size)
        self.draw_dot(screen, screen_width, screen_height, color, size)

    def draw_dashed_circle(self, screen, screen_width, screen_height, color, size):
        center_x, center_y = screen_width // 2, screen_height // 2
        for i in range(0, 360, 15):
            x = center_x + int(size * math.cos(math.radians(i)))
            y = center_y + int(size * math.sin(math.radians(i)))
        pygame.draw.circle(screen, color, (x, y), 2)

    def draw_tilted_square(self, screen, screen_width, screen_height, color, size):
        center_x, center_y = screen_width // 2, screen_height // 2
        points = [
            (center_x, center_y - size),
            (center_x + size, center_y),
            (center_x, center_y + size),
            (center_x - size, center_y),
        ]
        pygame.draw.polygon(screen, color, points, 2)