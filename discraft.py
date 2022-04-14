# Coded By: Tom Sumner
# Date: 13-04-2022
# Github: Tom-Sumner / https://github.com/Tom-Sumner
# Discord: TSumner#5215
# License: MIT
# Note: If you use this code, you MUST credit me in your project.



from typing import Iterable
import nextcord, time, os, random
from random import choice
from nextcord.ext import commands
from nextcord import Interaction
from nextcord import SlashOption
from dotenv import load_dotenv
load_dotenv()


def stringify(item: Iterable):
	return ''.join(item)

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
	for i in range(0, 19):
		block = choice(GrassAndSky)
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
	world = f"{stringify(y6)}\n{stringify(y5)}\n{stringify(y4)}\n{stringify(y3)}\n{stringify(y2)}"
	return world

# Class that represents the world
class World:
	def __init__(self):
		self.world = gen_world()
		self.x = 0

# Function to generate a preset embed message according to the user name
def embed(player):
	embed = nextcord.Embed(title="Minecraft", description=f"{player.user.name}'s World", color=0x00ff00)
	embed.add_field(name="Game", value=player.world)
	return embed


# Class that represents the player
class Player:
	""".. versionadded:: 2.0\nRepresents a Discraft player.\n-----------"""
	def __init__(self, user) -> None:
		self.user: nextcord.Member = user
		self.world = World().world

	def move(self, dir):
		"""Moves the player in the given direction

		Args:
			dir (`str`): The direction to move in
		"""
		if dir == "up":
			self.y += 1
		elif dir == "down":
			self.y -= 1
		elif dir == "left":
			self.x -= 1
		elif dir == "right":
			self.x += 1

class Controls(nextcord.ui.View):
	def __init__(self, user):
		super().__init__(timeout=None)
		self.user = user

	@nextcord.ui.button(label="Left", style=nextcord.ButtonStyle.blurple, row=2)
	async def left(self, button, ctx: Interaction):
		pass

	@nextcord.ui.button(label="*", style=nextcord.ButtonStyle.grey, row=2, disabled=True)
	async def placeholder1(self, button, ctx: Interaction):
		pass

	@nextcord.ui.button(label="Right", style=nextcord.ButtonStyle.blurple, row=2)
	async def right(self, button, ctx: Interaction):
		pass

	@nextcord.ui.button(label="*", style=nextcord.ButtonStyle.grey, row=1, disabled=True)
	async def placeholder2(self, button, ctx: Interaction):
		pass

	@nextcord.ui.button(label="Jump", style=nextcord.ButtonStyle.green, row=1)
	async def up(self, button, ctx: Interaction):
		pass

	@nextcord.ui.button(label="*", style=nextcord.ButtonStyle.grey, row=1, disabled=True)
	async def placeholder3(self, button, ctx: Interaction):
		pass

	@nextcord.ui.button(label="*", style=nextcord.ButtonStyle.grey, row=3, disabled=True)
	async def placeholder4(self, button, ctx: Interaction):
		pass

	@nextcord.ui.button(label="Dig", style=nextcord.ButtonStyle.green, row=3)
	async def down(self, button, ctx: Interaction):
		pass

	@nextcord.ui.button(label="*", style=nextcord.ButtonStyle.grey, row=3, disabled=True)
	async def placeholder5(self, button, ctx: Interaction):
		pass


class Game:
	def __init__(self, player):
		self.world = Player.world
		self.player = Player
		self.controls = Controls(self.player)
		self.playerX = self.player.x
		self.playerY = self.player.y



client: nextcord.Client = commands.Bot(command_prefix=";", intents=nextcord.Intents.all())


@client.event
async def on_ready():
	os.system("cls")
	print("Bot is ready!")
	time.sleep(1)
	print("\r")
	print(f"Logged in as {client.user}")



@client.slash_command(name="play", description="Play a game of minecraft in Discord!", guild_ids=[932374983001378898, 936999558565744640])
async def play(ctx: Interaction):
	await ctx.send(ephemeral=True, content="Your game is being generated now! please wait...")
	
	
@client.slash_command("gen-world", description="Generate a world of minecraft in Discord!", guild_ids=[932374983001378898, 936999558565744640])
async def gen(ctx: Interaction):
	await ctx.send(ephemeral=True, content="Generating a world now! please wait...")
	await ctx.channel.send(embed=embed(Player(ctx.user)), view=Controls(ctx.user))

client.run(os.getenv("TOKEN"))
