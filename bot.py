# from https://realpython.com/how-to-make-a-discord-bot-python/
import os
import discord, random
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

# so this doesn't work. I'm not sure if it's a permission error or what.
"""@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )"""


#from https://www.devdungeon.com/content/make-discord-bot-python
@client.event
async def on_message(message): #any action that is a respose to a message should go under here
    '''# we do not want the bot to reply to itself
    if message.author == client.user:
        return'''

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention} :grinning:'.format(message)
        await message.channel.send(msg)

    #there is probably a way to do this from a file, if it gets too long
    funFacts = [
        'Cherophobia is an irrational fear of fun or happiness.',
        'During your lifetime, you will produce enough saliva to fill two swimming pools.',
        'Polar bears could eat as many as 86 penguins in a single sitting…',
        'The “Windy City” name has nothing to do with Chicago weather',
        'Armadillo shells are bulletproof',
    ]

    if message.content == 'funfact!':
        response = random.choice(funFacts)
        await message.channel.send(response)

    #random image
    my_file = open("pictures.txt", "r")
    content = my_file.read()
    doggies = content.split("\n")
    my_file.close()

    if message.content == '!dogo':
        response = random.choice(doggies)
        await message.channel.send(response) 

    # create a poll
    if message.content.startswith("!poll"):
        # await client.send_message(message.channel, message.content[3:])
        userInput = message.content[5:]
        splitQuestion = userInput.split('?')
        splitAnswers = splitQuestion[1].split( )
        await message.channel.send(splitQuestion[0]+'?\n')
        j = 1
        for i in splitAnswers:
            if j == 1:
                msg = await message.channel.send(":one: " + splitAnswers[j-1])
                j += 1
            elif j == 2:
                msg = await message.channel.send(":two: "+ splitAnswers[j-1])
                j += 1
            elif j == 3:
                msg = await message.channel.send(":three: "+ splitAnswers[j-1])
                j += 1
            elif j == 4:
                msg = await message.channel.send(":four: "+ splitAnswers[j-1])
                j += 1
            elif j == 5:
                msg = await message.channel.send(":five: "+ splitAnswers[j-1])
                j += 1
            elif j == 6:
                msg = await message.channel.send(":six: "+ splitAnswers[j-1])
                j += 1
            elif j == 7:
                msg = await message.channel.send(":seven: "+ splitAnswers[j-1])
                j += 1
            elif j == 8:
                msg = await message.channel.send(":eight: "+ splitAnswers[j-1])
                j += 1
            elif j == 9:
                msg = await message.channel.send(":nine: "+ splitAnswers[j-1])
                j += 1
            elif j == 10:
                msg = await message.channel.send(":keycap_ten: "+ splitAnswers[j-1])
                j += 1
            else:
                quit() 

        j = 1
        for i in splitAnswers:
            if j == 1:
                await msg.add_reaction('1️⃣')
                j += 1
            elif j == 2:
                await msg.add_reaction('2️⃣')
                j += 1
            elif j == 3:
                await msg.add_reaction('3️⃣')
                j += 1
            elif j == 4:
                await msg.add_reaction('4️⃣')
                j += 1
            elif j == 5:
                await msg.add_reaction('5️⃣')
                j += 1
            elif j == 6:
                await msg.add_reaction('6️⃣')
                j += 1
            elif j == 7:
                await msg.add_reaction('7️⃣')
                j += 1
            elif j == 8:
                await msg.add_reaction('8️⃣')
                j += 1
            elif j == 9:
                await msg.add_reaction('9️⃣')
                j += 1
            elif j == 10:
                await msg.add_reaction('🔟')
                j += 1
            else:
                quit()
       

client.run(TOKEN)
