import json

class GameStats():
	""" Track statistics for alien Invasion."""

	def __init__(self, ai_settings):
		"""Initialize statistics."""
		self.ai_settings = ai_settings
		self.reset_stats()
		self.game_active = False
		# High score should never be reset.
		filename = 'highscore.json'
		with open(filename) as file_object:
			self.high_score = json.load(file_object)

	def reset_stats(self):
		""" Initialize statistics that can change during the game. """
		self.ships_left = self.ai_settings.ships_limit
		self.score = 0
		self.level = 1