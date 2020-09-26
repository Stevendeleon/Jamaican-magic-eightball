import discord
from discord.ext import commands
import random
import os

# URL for A Learner’s Glossary of Jamaican: Part of the Open Grammar Project
# Work on Generating Phrases based on key words here: https://opengrammar.github.io/jam/glossary/

BOT_TOKEN = os.enviorn('BOT_TOKEN')

client = commands.Bot(command_prefix='$')


@client.event
async def on_ready():
    print('Brejren me ready Come Tru')


@client.event
async def on_member_join(member):
    print(f'{member} aneda yuut wahn romp wid mi')


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong!')


@client.command()
async def q(ctx, *, question):
    responses = [
        "It is certain",
        "Without a doubt",
        "Definitely",
        "Most likely",
        "Outlook good",
        "Yes!",
        "Try again",
        "Reply hazy",
        "Can't predict",
        "No!",
        "Unlikely",
        "Sources say no",
        "Very doubtful"
    ]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


client.run(BOT_TOKEN)
