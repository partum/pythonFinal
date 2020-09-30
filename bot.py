# from https://realpython.com/how-to-make-a-discord-bot-python/
import os

import discord
from dotenv import load_dotenv

load_dotenv() # this is the stuff in the .env file
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD') # guild = server

client = discord.Client()

@client.event
async def on_ready(): # this makes the Client wait untill it is ready for action
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    print('Guild Members:')
    async for member in guild.fetch_members(limit=50): #This works while guild.members does not. I'm guessing it's a cache issue.
        print(f'- {member.name}')



client.run(TOKEN)
