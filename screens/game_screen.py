import pygame
import math
import settings as cfg
from game.entities import Ball, Paddle

def ApplyBonus(bonus_type: str, paddle: Paddle, balls: list[Ball]) -> None:
    if bonus_type == "paddle_shrink":
        center = paddle.rect.centerx
        paddle.rect.width = max(cfg.PADDLE_WIDTH // 2, int(paddle.rect.width * 0.8))
        paddle.rect.centerx = center
        paddle.rect.clamp_ip(pygame.Rect(
            cfg.FIELD_LEFT,
            0,
            cfg.FIELD_RIGHT - cfg.FIELD_LEFT,
            cfg.HEIGHT,
        ))
    elif bonus_type == "ball_speed_up":
        for ball in balls:
            _scale_ball_speed(ball, 1.2, 3, 12)
    elif bonus_type == "ball_speed_down":
        for ball in balls:
            _scale_ball_speed(ball, 0.8, 3, 12)

def _scale_ball_speed(ball: Ball, multiplier: float, minimum: float, maximum: float) -> None:
    speed = math.hypot(ball.vx, ball.vy)
    if speed == 0:
        return
    new_speed = max(minimum, min(maximum, speed * multiplier))
    scale = new_speed / speed
    ball.vx *= scale
    ball.vy *= scale

def run(screen: pygame.Surface, clock: pygame.time.Clock, level: int) -> None:
    paddle = Paddle()

    keys = pygame.key.get_pressed()
    paddle.move(keys)

    paddle.draw(screen)
