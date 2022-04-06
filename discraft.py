# Coded By: Tom Sumner
# Date: 2020-04-24
# Github: Tom-Sumner
# Discord: TSumner#5215
# License: MIT
# Note: If you use this code, you MUST credit me in your project.


import nextcord, time, os, random
from random import randint
from nextcord.ext import commands
from nextcord import Interaction
from nextcord import slash_command, SlashOption
from dotenv import load_dotenv
load_dotenv()

def gen_y4():
	g = "🟩"
	s = "🟦"
	result = []
	for i in range(0, 19):
		i = randint(0, 1)
		if i == 0:
			b = s
		else:
			b = g
		result.append(b)
	return result

def gen_y3():
	g = "🟩"
	d = "🟫"
	result = []
	y4 = gen_y4()
	for i in y4:
		if i == g:
			result.append(d)
		else:
			result.append(g)
	return y4, result


def gen_world():
	y4, y3 = gen_y3()
	y6 = ["🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦"]
	y5 = ["🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦","🟦"]
	y2 = ["🟫","🟫","🟫","🟫","🟫","🟫","🟫","🟫","🟫","🟫","🟫","🟫","🟫","🟫","🟫","🟫","🟫","🟫","🟫"]
	world = f"{''.join(y6)}\n{''.join(y5)}\n{''.join(y4)}\n{''.join(y3)}\n{''.join(y2)}"
	return world


class World:
	def __init__(self):
		self.world = gen_world()
		self.x = 0
		self.y = 3

	def move(self, x, y):
		g = "🟩"
		d = "🟫"
		lvls = []
		for lvl in range(0, 19):
			lvls.append(self.world[lvl])
		nextblock = lvls[y][x]
		if x < 19 and x > -1:
			pass
		else:
			raise Exception("Out of bounds")
		if nextblock != g:
			lvls[y][x] = "h"
		self.world = f"{''.join(lvls[5])}\n{''.join(lvls[4])}\n{''.join(lvls[3])}\n{''.join(lvls[2])}\n{''.join(lvls[1])}\n{''.join(lvls[0])}"
		return self.world

class game:
	world = World()
	embed = nextcord.Embed(title="Minecraft", description="You can play minecraft in Discord with this bot!")
	embed.add_field(name="Game", value=world.world.replace("h", "<:steve:960580473699057694>"))

	class controls(nextcord.ui.View):
		def __init__(self, user):
			super().__init__(timeout=None)
			self.user = user

		@nextcord.ui.button(label="Backward", style=nextcord.ButtonStyle.green)
		async def backward(self, button, ctx: Interaction):
			if ctx.user != self.user:
				await ctx.send(ephemeral=True, content="This is not your game to play!")
			else:
				pass
			try:
				world = game.world.move(game.world.x-1, 3)
				embed = nextcord.Embed(title="Minecraft", description=f"{self.user.name}'s world")
				embed.add_field(name="Game", value=world.replace("h", "<:steve:960580473699057694>"))
				await ctx.message.edit(embed=embed)
			except Exception("Out of bounds") as e:
				await ctx.send(ephemeral=True, content="You can't go back!")

		@nextcord.ui.button(label="Forward", style=nextcord.ButtonStyle.blurple)
		async def forward(self, button, ctx: Interaction):
			if ctx.user != self.user:
				await ctx.send(ephemeral=True, content="This is not your game to play!")
			else:
				pass
			try:
				world = game.world.move(game.world.x+1, 3)
				embed = nextcord.Embed(title="Minecraft", description=f"{self.user.name}'s world")
				embed.add_field(name="Game", value=world.replace("h", "<:steve:960580473699057694>"))
				await ctx.message.edit(embed=embed)
			except Exception("Out of bounds") as e:
				await ctx.send(ephemeral=True, content="You can't go forward!")



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
	await ctx.channel.send(embed=game.embed, view=game.controls(user=ctx.user))
	
@client.slash_command("gen-world", description="Generate a world of minecraft in Discord!", guild_ids=[932374983001378898, 936999558565744640])
async def gen(ctx: Interaction):
	await ctx.send(ephemeral=True, content="Generating a world now! please wait...")
	embed = nextcord.Embed(title="Minecraft", description="Generating a world...")
	embed.add_field(name="Game", value=gen_world())
	await ctx.channel.send(embed=embed)

client.run(os.getenv("TOKEN"))
