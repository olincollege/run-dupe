import pytest
import pygame
from alien import Alien


@pytest.fixture
def setup_alien():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    alien = Alien(x=100, y=100)
    yield screen, alien
    pygame.quit()


def test_alien_move_left(setup_alien):
    _, alien = setup_alien
    keys = pygame.key.get_pressed()
    keys[pygame.K_LEFT] = 1
    alien.press_keys(keys)
    assert alien.velocity.x == -5


def test_alien_move_right(setup_alien):
    _, alien = setup_alien
    keys = pygame.key.get_pressed()
    keys[pygame.K_RIGHT] = 1
    alien.press_keys(keys)
    assert alien.velocity.x == 5


def test_alien_jump(setup_alien):
    _, alien = setup_alien
    keys = pygame.key.get_pressed()
    keys[pygame.K_SPACE] = 1
    alien.jump()
    assert alien.velocity.y > 0
