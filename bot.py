# from https://realpython.com/how-to-make-a-discord-bot-python/
import os
import discord, random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv() # this is the stuff in the .env file
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD') # guild = server

bot = commands.Bot(command_prefix='!')

# confirmation that the bot has connected (not a command)
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# creates the image list


# return random image of dog (from list)
@bot.command(name='dogo', help='Returns a random picture of a dog')
async def dog_pic(ctx):
    # it would be better if I could figure out how to pass doggies to the command instead of creating the list everytime
    my_file = open("pictures.txt", "r")
    content = my_file.read()
    doggies = content.split("\n")
    my_file.close()
    response = random.choice(doggies)
    await ctx.send(response) 

# example command. Delete later.
@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

# reply hello [name] 
@bot.command(name='hello', help='Responds with a greeting')
async def hello(ctx):
    response = 'Hello ' + str(ctx.author.mention) + ' :wave:'
    await ctx.send(response)

#return a fun fact
@bot.command(name='funfact', help='Returns a "fun" fact')
async def fun_fact(ctx):
    # this can be done from a file as well if the list gets too long
    funFacts = [
        'Cherophobia is an irrational fear of fun or happiness.',
        'During your lifetime, you will produce enough saliva to fill two swimming pools.',
        'Polar bears could eat as many as 86 penguins in a single sitting...',
        'The “Windy City” name has nothing to do with Chicago weather',
        'Armadillo shells are bulletproof',
    ]
    response = random.choice(funFacts)
    await ctx.send(response)

'''#from https://www.devdungeon.com/content/make-discord-bot-python
@client.event
async def on_message(message): #any action that is a respose to a message should go under here
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return


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
        for a in splitAnswers:
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
                quit()'''
       

bot.run(TOKEN)
