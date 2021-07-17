import discord
from discord.ext import commands
import random
import os
# from scrape import word_of_day

# URL: https://jamaicanpatwah.com/

BOT_TOKEN = os.environ.get('BOT_TOKEN')

client = commands.Bot(command_prefix='.')


# Turn bot on
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Mi deh yah'))
    print('Bot ready')


# Member Joined Server
@client.event
async def on_member_join(member):
    print(f'{member} aneda yuut wahn ramp wid mi')


# Member Left Server
@client.event
async def on_member_remove(member):
    print(f'{member} mon gaaaaaaaan')


"""
# Kick
@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
# Ban
@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned: {member.mention}')
# Unban
@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'unbanned {user.mention}')
            return
"""


# Response list
@client.command()
async def q(ctx, *, question):
    responses = [
        "Eh a certain",
        "Widout a doubt",
        "di outlook criss",
        "Mi throw mi corn but me neva call no fowl",
        "Yuh cyaah sidung pan cow back an cuss cow",
        "yeh fah sure",
        "mi nuh know bredren",
        "Yuh too baddasum, kiss mi back side and galang",
        "Wah bout yuh, Wah deh gwaan",
        "Yuh sure yuh waah try mi, mi nuh kin teet",
        "Yuh afi know seh mi run tings yah.",
        "Nuh ebery ting dat ave sugar sweet",
        "mi nuh biznizz",
        "Tun up dah chune deh selectah, booyaka! booyaka!",
        "Yah mi tink suh",
        "Scornful dawg nyam dutty pudding",
        "Yuh affi stay trang, yuh si wah mi a seh",
        "If di fish come fram deep sea and teel yuh seh it deep, yuh cyaah seh a lie",
        "Every hoe ha tem stick a bush",
        "Wah mek yuh haffi nyam off alla di food? mi neva know seh yuh a bong belly pickney",
        "Wah sweet nanny goat ago run him belly",
        "Mek I tell yuh sum'n, nuh evry mon weh kin teet pon yuh weh love yuh.",
        "Chicken merry, hawk deh near",
        "Shot a buss round deh suh right now!",
        "Mi yeye a mi market yuh a mi coco basket",
        "Di gyal faada just drop a yard, weh we a go do now?",
        "Mon tink he eh at steppa",
        "di don Dada sen fi yuh, gwan wid it",
        "PRISS mon a ball head, look ah di shine head man de out dea",
        "A weh yuh wuk bredda",
        "Yuh undestan wah mi a seh??",
        "*clicks* Mek I tell yuh sum'n, nuh evry mon weh kin teet pon yuh weh love yuh.",
        "*Clicks* dis nanny raas...",
        "BloOoOoOdseeed a wah ye ax me dat fah?",
        "Mi naw deal wid nutten",
        "a walk good bredda... walk good",
        "Sorry fi mawga dawg, mawga dawg tun roun bite you",
        "Og seh di foss waata im kech im walla",
        "One, one coco full basket",
        "Quashie come a town",
    ]
    answer = random.choice(responses)
    await ctx.send(f'Q: {question}\nA: {answer}')
    print(answer)


client.run(BOT_TOKEN)


# word_of_day()

