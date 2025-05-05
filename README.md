# run-dupe

**ENGR2510-02.25SP**

**Project By: Mira Epstein & Kuhu Jayaswal**

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg)](https://github.com/prettier/prettier)
![pylint status: passing](https://img.shields.io/badge/pylint-passing-green)


### Project Overview

**To run the game run the file `run_model.py`**

In this project, we recreated the popular 3d platformer game run. We made the project our own by removing the rotating tunnel to make it easier. This is useful to people who are not used to playing computer games or have less dexterity in their hands.

To begin playing the game press the start button displayed on the screen, the game with then immediately start going so you better focus.

The goal of the game is to make it to the highest level you can. Your character is an alien that is running on a platform, with pits quickly approaching your character, if your character falls into the pit or off the platform, it dies. To avoid this happening, you can move your character using the arrow keys or wasd (the space bar will make the character jump too). When the character dies, the game resets to the home screen so you can try again! The levels are displayed in the upper left corner of the screen when playing. You will level up after passing 5 platforms in a single run. When you level up for the first 8 levels, the speed increases. When your character dies your level resets.


### Getting Started

#### Required Software Packages

To run our project on your device, you will need the following libraries (excluding the standard python library).

- `pygame`==2.6.1
- `pytest`==8.3.5

To install these libraries, run the following command in your terminal:

```bash
pip install -r requirements.txt
```

### Program Overview

This project was built using the Model-View-Controller pattern.

The controller classes can be found in `run_controller.py`. This file contains three classes: `AlienController`, `PitController`, and `StartScreenController`. Each one controls the character, the pits approaching the character, and the button on the start screen respectively.

The view classes can be found in `run_view.py`. This file contains two classes: `GameView` and `StartScreenView`. `GameView` draws the character, the pits approaching the character, the background, and the level counter. `StartScreenView` draws the starting screen background, the start button, and the image displayed when you open the game.

The model class can be found in `run_model.py` and it imports all the classes from `run_controller.py` and `run_view.py` and puts them together into a model class that runs the game (that's why this is the file you run to open the game window).


### Documentation

Documentation and more information about our program can be found on our website [insert link here]
