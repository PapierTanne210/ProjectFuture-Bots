import asyncio
import discord
import keep_alive
from discord.ext import commands

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@client.event
async def on_ready():
    print('ONLINE {}'.format(client.user.name))
    client.loop.create_task(status_task())

async def status_task():
    while True:
        await client.change_presence(activity=discord.Game('discord.gg/projectfuture'), status=discord.Status.online)
        await asyncio.sleep(50)
        await client.change_presence(activity=discord.Game('The official Bot!'), status=discord.Status.online)
        await asyncio.sleep(3)
        await client.change_presence(activity=discord.Game('V1 SOON!'), status=discord.Status.online)
        await asyncio.sleep(50)
        await client.change_presence(activity=discord.Game('!help for help'), status=discord.Status.online)
        await asyncio.sleep(200)



@client.event
@commands.is_owner()
async def on_message(message):
    if message.author.bot:
        return
    if 'test' in message.content:
        await message.channel.send('test done')


@client.event
async def on_message(message):
    if message.author.bot:
        return
    if 'Who asked' in message.content:
        await message.channel.send('I asked!')
    if 'Who cares' in message.content:
        await message.channel.send('I care!')
    if '!help' in message.content:
        await message.channel.send('Nothing exept Who asked and Who cares')


@client.event
async def on_member_join(member):
    guild = client.get_guild(945357715037904977)
    welcome_channel = guild.get_channel(945357715671240757)
    embed = discord.Embed(title="👋 | Welcome to **Project Future**!",
                          description=f"Welcome {member.mention}! Have fun!")
    embed.add_field(name=f"We are happy to see you here {member}",
                    value=f"Now we are {len(set(client.users))} User!")
    embed.set_image(
        url="https://cdn.discordapp.com/attachments/883805723807588423/901580387950686259/zerotwo_ist_scheie.gif")
    await welcome_channel.send(embed=embed)

@client.event
async def on_member_remove(member):
    guild = client.get_guild(945357715037904977)
    bye_channel = guild.get_channel(945357715671240757)
    await bye_channel.send(f"{member} has left!")































client.run('OTc5MzA5NTcwNTYyMzU5MzM2.GVA73-.FKBibaqaFgS7TOuBKnjedDQdK44WpppyquE3sw')