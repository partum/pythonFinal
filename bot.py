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


#from https://www.devdungeon.com/content/make-discord-bot-python
@client.event # reply to !hello with hello @thatPerson
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention} :grinning:'.format(message)
        await message.channel.send(msg)

client.run(TOKEN)
