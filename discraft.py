# Coded By: Tom Sumner
# Date: 13-04-2022
# Github: Tom-Sumner / https://github.com/Tom-Sumner
# Discord: TSumner#5215
# License: MIT
# Note: If you use this code, you MUST credit me in your project.

import worldgen
from worldgen import world as World, gen_world, layout
from typing import Iterable
import nextcord, time, os, random
from random import choice
from nextcord.ext import commands
from nextcord import Interaction
from nextcord import SlashOption
from dotenv import load_dotenv
load_dotenv()




# Class that represents the player
class Player:
	def __init__(self, user) -> None:
		self.user: nextcord.Member = user
		self.world = World(layout)
		self.y = 2

	def move(self, dir):
		if dir == "up":
			self.y += 1
		elif dir == "down":
			self.y -= 1

class Controls(nextcord.ui.View):
	def __init__(self, user):
		super().__init__(timeout=None)
		self.user = user
		self.view = super()

	@nextcord.ui.button(label="Left", style=nextcord.ButtonStyle.blurple, row=2)
	async def left(self, button, ctx: Interaction):
		self.user.world.left()
		await ctx.message.edit(embed=embed(self.user))

	@nextcord.ui.button(label="*", style=nextcord.ButtonStyle.grey, row=2, disabled=True)
	async def placeholder1(self, button, ctx: Interaction):
		pass

	@nextcord.ui.button(label="Right", style=nextcord.ButtonStyle.blurple, row=2)
	async def right(self, button, ctx: Interaction):
		self.user.world.right()
		await ctx.message.edit(embed=embed(self.user))

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
		self.world = player.world
		self.player = player
		self.world = self.world.x
		self.controls = Controls(self.player)
		self.playerY = self.player.y

# Function to generate a preset embed message according to the user name
def embed(player):
	embed = nextcord.Embed(title="Minecraft", description=f"{player.user.name}'s World", color=0x00ff00)
	embed.add_field(name="Game", value=player.world.print())
	return embed

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
	player = Player(ctx.user)
	controls = Controls(player)
	await ctx.channel.send(embed=embed(player), view=controls)

client.run(os.getenv("TOKEN"))
