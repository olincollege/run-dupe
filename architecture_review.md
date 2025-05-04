# Run Dupe!
The goal: \
![image dsc](images\run3screen.jpeg)
```
File: main.py
	def main
```
```
File: game.py
	class game (moves the tunnel)
		init
			frame_rate
			level 
	def move_tunnel
		left/right arrow key + space bar moves to the opposite side of the tunnel
				ORRRR
		holding down arrow key orients the angle of turning of the tunnel
		changes orientation of the tunnel such that the alien upright
		space bar = screen shifts down and then back up
		left arrow = right
		right arrow = left
	def update_level
		alien crosses previous level, update to next
	def progress_tunnel
		move tunnel forward at a constant speed
		view gets larger when approaching part of the tunnel
```
```
File alien.py
	class alien (just the player)
		init
			alien_state (dead or alive, running or stopped)
		def update_alien
			while not dead
			animate legs moving: every second it switched between two images, pause when jumping
			alien stays upright at all times
			Animate legs for jump
			else
			stop moving
		def jump
			alien_go_up: when space bar is clicked, alien goes up first and then down (original pos) along the y-axis
```

Topic: What is your project? If it is a game, what is the genre and objective? If it is an interactive visualization, what are you visualizing? If it is a tool/application, what does it do?
We are recreating Run 3, which is a platformer game with an objective of getting to the end of the level without falling. We plan to have a few levels of varying difficulty.

Interactivity: How does a user interact with the project?
The user interacts with our game by playing it, obviously. It’s simple and uses arrow keys/space bar to navigate the character through all levels. The purpose is to move the character through all the levels and have fun!

Ethics: Who do you envision as a user of this project? What kind of information/inputs are being collected from users? What malicious user behavior, if any, might you need to protect against?
Any person can play this game. The inputs are just the arrow keys and space bar that the player is clicking at the given time. The only malicious user behavior we might need to protect against is input spamming, which could cause the game to bug out.

Model: What information represents the “state” of your visualization, game, or tool? How are you storing this information in the relevant class(es)?
The model consists of the level, game paused or playing, music on or off, the velocity of the character running, and the position of the character.


View: What information are you displaying to the user at any given time? What attributes/methods will you use to compute and/or display this information?
The view would consist of the level itself, the player moving through the level, frame rate.

Controller: How is the user providing input? What inputs translate to which methods in the model class(es)?
The left/right arrow keys and spacebar translates to the moves of the character throughout the pathway of the level. 

Extra Features (if we have time):
Music, name your alien, more levels, different shaped tunnels, multiple players, number of deaths
