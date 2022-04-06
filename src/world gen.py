# Coded By: Tom Sumner
# Date: 2020-04-24
# Github: Tom-Sumner
# Discord: TSumner#5215
# License: MIT
# Note: If you use this code, you MUST credit me in your project.


import random
from random import randint

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

if __name__ == "__main__":
    gen_world()