import pygame

from settings import Settings
from ship import Ship 
import game_functions as gf
from game_stats import GameStats
from pygame.sprite import Group
from button import Button 
from scoreboard import Scoreboard 


def run_game():
	#Initialize pygame, settings and create a screen object.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	# Make the Play button.
	play_button = Button(ai_settings, screen, "Press P to play")

	# Create an instance to store game statistics and create a scoreboard.
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)

	# Make a Ship, a group of bullets and a group of aliens
	ship = Ship(ai_settings, screen)
	aliens = Group()
	bullets = Group()

	# Create a fleet of aliens
	gf.create_fleet(ai_settings, screen, ship, aliens)

	#Start the main loop for the game
	while True:
		gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
			gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
				 bullets, play_button)


		#Make the most recently drawn screen visible
		#pygame.display.flip()

run_game()
