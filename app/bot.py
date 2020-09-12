from dotenv import load_dotenv
import os
import random

import discord

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
USERID = os.getenv('DISCORD_USER')

client = discord.Client()
BOT_MODE = True
SELECTED_CHANNEL_INDEX = 0
SELECTED_CHANNEL = None

client_1 = commands.Bot(command_prefix= "!")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    # print('Available Channels: {}'.format(client.guilds[0].channels[-1]))
    
    print("Available Guilds: ")
    for index, guild in enumerate(client.guilds):
        print("[{}] - {}".format(index , guild))

    selected_index = int(input("Input Your Selected Guild To Implant Bot."))

    print("Available Channels")
    for index, channel in enumerate(client.guilds[selected_index].channels):
        print("[{}] - {}".format(index , channel))

    selected_channel_index = int(input("Input Your Selected Channel To Implant Bot."))

    SELECTED_CHANNEL = client.guilds[selected_index].channels[selected_channel_index]
    await client.guilds[0].channels[-2].send("Discord Bot Online.")

    print(SELECTED_CHANNEL)

 #for loading and unloading cog extensions
@client_1.command()
@commands.has_permissions(administrator = True)
async def load(ctx, *, extension):
    client.load_extension(f'cogs.{extension}')

@client_1.command()
@commands.has_permissions(administrator = True)
async def unload(ctx, *, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(TOKEN)
