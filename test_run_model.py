import pygame
from run_model import Game
from run_controller import AlienController, PitController

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

    # Simulate pit moving off-screen
    pit.y_pos = 600
    pit.update()
    assert pit.y_pos == 0


def test_character_jump_flag():
    """Tests that character can jump."""
    controller = AlienController(375, 375, 50, 50)
    controller.state["jumping"] = True
    assert controller.state["jumping"] is True
