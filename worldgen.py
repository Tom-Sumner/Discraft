# Coded By: Tom Sumner
# Date: 2020-04-24
# Github: Tom-Sumner
# Discord: TSumner#5215
# License: MIT
# Note: If you use this code, you MUST credit me in your project.

import random
from random import randint
from tokenize import tabsize


def stringify(world: tuple):
	result = f"{''.join(world[4])}\n{''.join(world[3])}\n{''.join(world[2])}\n{''.join(world[1])}\n{''.join(world[0])}"
	return result

# Block Types abd Player
player = "<:steve:960580473699057694>"
grass = "🟩"
sky = "🟦"
dirt = "🟫"
GrassAndSky = [grass, sky]
GrassAndDirt = [grass, dirt]

# Generate a random list of 2 colors with a lengh of 19
# These are the colors that will be used to generate the world
# This function generates the Y level 4
def gen_y4():
	result = []
	for i in range(19):
		block = random.choice(GrassAndSky)
		result.append(block)
	return result

# Use the gen_y4() function to make sure there are no floating blocks in the generation of Y 3
# By checking if the block is a floating block, we can make sure that the block is not floating
def gen_y3():
	result = []
	y4 = gen_y4()
	for i in y4:
		if i == grass:
			result.append(dirt)
		else:
			result.append(grass)
	return y4, result




# This function uses a preset sky and ground and then adds Y3 and Y4 in the middle of the world
def gen_world():
	y4, y3 = gen_y3()
	y6 = [sky] * 19
	y5 = [sky] * 19
	y2 = [dirt] * 19
	layout = y2, y3, y4, y5, y6
	return layout


class world:
	def __init__(self, layout) -> None:
		self.layout = layout
		self.scroll_x = 0
	
	# Generate the next X column of the world.
	# Delete the first X of the world.
	# Append the new X to the end.
	def right(self, count = 1):
		for i in range(count):
			y4 = random.choice(GrassAndSky)
			if y4 == grass:
				y3 = dirt
			else:
				y3 = grass
			del self.layout[1][0]
			del self.layout[2][0]
			self.layout[1].append(y3)
			self.layout[2].append(y4)
		return self.layout

	def left(self, count = 1):
		"""Move the world one to the right"""
		for i in range(count):
			y4 = random.choice(GrassAndSky)
			if y4 == grass:
				y3 = dirt
			else:
				y3 = grass
			del self.layout[1][18]
			del self.layout[2][18]
			self.layout[1].insert(0, y3)
			self.layout[2].insert(0, y4)
		return self.layout

	def print(self):
		return stringify(self.layout)

	


layout = (
	['🟫', '🟫', '🟫', '🟫', '🟫', '🟫', '🟫', '🟫', '🟫', '🟫', '🟫', '🟫', '🟫', '🟫', '🟫', '🟫', '🟫', '🟫', '🟫'], 
	['🟫', '🟫', '🟫', '🟫', '🟫', '🟩', '🟩', '🟫', '🟫', '🟫', '🟩', '🟩', '🟩', '🟩', '🟩', '🟩', '🟩', '🟫', '🟩'],
	['🟩', '🟩', '🟩', '🟩', '🟩', '🟦', '🟦', '🟩', '🟩', '🟩', '🟦', '🟦', '🟦', '🟦', '🟦', '🟦', '🟦', '🟩', '🟦'], 
	['🟦', '🟦', '🟦', '🟦', '🟦', '🟦', '🟦', '🟦', '🟦', '🟦', '🟦', '🟦', '🟦', '🟦', '🟦', '🟦', '🟦', '🟦', '🟦'], 
	['🟦', '🟦', '🟦', '🟦', '🟦', '🟦', '🟦', '🟦', '🟦', '🟦', '🟦', '🟦', '🟦', '🟦', '🟦', '🟦', '🟦', '🟦', '🟦']
)