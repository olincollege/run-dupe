"""Pytests for model."""

import pygame
from run_model import Game
from run_controller import AlienController, PitController
from run_view import GameView

# Initialize Pygame once for testing
pygame.init()


def test_initial_level():
    """Test first level for properties."""
    game = Game()
    assert game.properties["level"] == 1
    assert game.properties["pit_speed"] == 3.5


def test_update_level():
    """Test that level changes and so does speed."""
    game = Game()
    game.update_level()
    assert game.properties["level"] == 2
    assert game.properties["pit_speed"] > 3.5


def test_pit_update_and_reset():
    """Test that the pits update."""
    pit = PitController(300, 0, 200, 10, 3.5, 1)
    original_y = pit.y_pos
    pit.update()
    assert pit.y_pos > original_y

    pit.y_pos = 600
    pit.update()
    assert pit.y_pos == 0


def test_character_jump():
    """Tests that character can jump."""
    controller = AlienController(375, 375, 50, 50)
    controller.state["jumping"] = True
    controller.velocity_y = -20
    controller.update()
    assert controller.rect.bottom < 425


def test_reset_game():
    """Tests that the game resets after death."""
    controller = Game()
    controller.reset_game()
    assert controller.properties["level"] == 1
    assert controller.properties["pit_speed"] == 3.5
    assert controller.alien_controller.rect.topleft == (375, 375)
    assert controller.alien_controller.velocity_x == 0
    assert controller.alien_controller.velocity_y == 0
    assert controller.alien_controller.state == {
        "jumping": False,
        "on_ground": True,
    }
    assert controller.alien_controller.alive is True


def test_jump_alive():
    """Tests that when character is jumping it is alive."""
    controller = AlienController(375, 300, 50, 50)
    assert controller.alive is True


def test_death():
    """Tests that character dies when touching the color of the pits."""
    controller = AlienController(375, 300, 50, 50)
    surface = pygame.Surface((600, 800))
    surface.fill((1, 1, 1))
    controller.check_pitfall(surface)
    assert controller.alive is False


def test_animation_jump():
    """Tests tha character displays the correct image when jumping."""
    view = GameView()
    view.jumping = True
    view.alive = True
    assert view.image == view.images["both"]


def test_animation_death():
    """Tests tha character displays the correct image when jumping."""
    controller = AlienController(375, 375, 50, 50)
    controller.alive = False
    view = GameView()
    assert view.image == view.images["both"]


def test_alien_horizontal_movement():
    """Test that alien can move in x direction."""
    controller = AlienController(375, 375, 50, 50)
    controller.velocity_x = 5
    initial_x = controller.rect.x
    controller.update()
    assert controller.rect.x > initial_x


def test_alien_lands_after_jump():
    """Test that alien stops jumping after it lands."""
    controller = AlienController(375, 375, 50, 50)
    controller.state["jumping"] = True
    controller.state["on_ground"] = False
    controller.velocity_y = 0
    controller.rect.y = 750
    controller.update()
    assert controller.state["on_ground"] is True
    assert controller.state["jumping"] is False
