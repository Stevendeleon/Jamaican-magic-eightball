import discord
from discord.ext import commands
import random
import os

# URL for A Learner’s Glossary of Jamaican: Part of the Open Grammar Project
# Work on Generating Phrases based on key words here: https://opengrammar.github.io/jam/glossary/

BOT_TOKEN = os.environ.get('BOT_TOKEN')

client = commands.Bot(command_prefix='$')


@client.event
async def on_ready():
    print('Di botmon rrrready')


@client.event
async def on_member_join(member):
    print(f'{member} aneda yuut wahn ramp wid mi')


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong!')


@client.command()
async def q(ctx, *, question):
    responses = [
        "Eh a certain",
        "Widout a doubt",
        "di outlook criss",
        "yeh fah sure",
        "mi nuh know bredren",
        "mi nuh biznizz",
        "Yah mi tink suh",
        "If di fish come fram deep sea and teel yuh seh it deep, yuh cyaah seh a lie",
        "Every hoe ha tem stick a bush",
        "Wah sweet nanny goat ago run him belly",
        "Chicken merry, hawk deh near",
        "Mon tink he eh at steppa",
        "di don Dada sen fi yuh, gwan wid it",
        "PRISS mon a ball head, look ah di shine head man de out dea",
        "A weh yuh wuk bredda",
        "Yuh undestan wah mi a seh??",
        "*Clicks* dis nanny raas..",
        "BloOoOoOdseeed a wah ye ax me dat fah?",
        "a walk good bredda... walk good"
    ]
    await ctx.send(f'Q: {question}\nA: {random.choice(responses)}')


client.run(BOT_TOKEN)
