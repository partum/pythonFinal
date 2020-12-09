# from https://realpython.com/how-to-make-a-discord-bot-python/
import os
import discord, random, asyncio
from dotenv import load_dotenv
from discord.ext import commands, tasks
from discord.utils import get
import urllib.parse, urllib.request, re

#intents are a 1.5 thing that have to be enabled so the bot can listen for events other than commands (or wait for on ready)
intents = discord.Intents.default() 
intents.typing = False
intents.presences = False
intents.members = True # this is a privileged intent (must be enabled in dev portal as well as here) that allows the bot to check for users joining, leaving, and updating their info

client = commands.Bot(command_prefix=',', intents=intents)

load_dotenv() # this is the stuff in the .env file
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD') # guild = server

bot = commands.Bot(command_prefix='!', intents=intents)

# confirmation that the bot has connected (not a command)
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# modified from https://github.com/jcreek/discord.py-welcome-bot/blob/master/welcome-bot.py
# send a welcome dm to new users
newUserMessage = "Welcome!!!!1 Don't break any rules!"
@bot.event
async def on_member_join(member): # this is an API specific name
    print("Recognised that a member called " + member.name + " joined") 
    try: 
        await member.send(newUserMessage) 
        print("Sent message to " + member.name)
    except:
        print("Couldn't message " + member.name)

# return random image of dog (from list)
my_file = open("pictures.txt", "r")
content = my_file.read()
doggies = content.split("\n")
my_file.close()
@bot.command(name='dogo', help='Returns a random picture of a dog')
async def dog_pic(ctx):
    response = random.choice(doggies)
    await ctx.send(response) 

# reply hello @[name] 
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

# poll
@bot.command(name='poll', help='Create a poll. End you question with a "?" and put a " " between options (up to 10.)')
async def poll(ctx):
    emojiList = [
       '1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟',
    ]
    userInput = ctx.message.content[5:]
    splitQuestion = userInput.split('?')
    splitAnswers = splitQuestion[1].split( )
    response = str(splitQuestion[0]) + '?\n'
    await ctx.send(response)
    j = 0
    for i in splitAnswers:
        msg = await ctx.send(emojiList[j] + " " + i)
        j += 1
    j = 0
    for i in splitAnswers:
        await msg.add_reaction(emojiList[j])
        j+= 1

#set a reminder (it's really more like an alarm)
@bot.command(name='remind', help='Set an alert fot yourself in x seconds.')
async def remind(ctx):
    x = int(ctx.message.content[8:])
    await asyncio.sleep(x)
    await ctx.send(str(ctx.author.mention) + " 🔔 Times up! 🔔")

# Time zone converter
# Get the time Now
@bot.command(name='time', help='Tells the time of the specified locations')
async def timeNow(): #formerly printCurrentTime
    fmt = "%Y-%m-%d %H:%M:%S %Z%z"

    # Current time in UTC
    now_utc = datetime.now(timezone('UTC'))
    await bot.say (now_utc.strftime(fmt) + " (UTC)")

    # Convert to Europe/London time zone
    now_london = now_utc.astimezone(timezone('Europe/London'))
    await bot.say (now_london.strftime(fmt) + " (London)")

    # Convert to Europe/Berlin time zone
    now_berlin = now_utc.astimezone(timezone('Europe/Berlin'))
    await bot.say (now_berlin.strftime(fmt) + " (Berlin)")

    # Convert to CET time zone
    now_cet = now_utc.astimezone(timezone('CET'))
    await bot.say (now_cet.strftime(fmt) + " (CET)")

    # Convert to Israel time zone
    now_israel = now_utc.astimezone(timezone('Israel'))
    await bot.say (now_israel.strftime(fmt) + " (Israel)")

    # Convert to Canada/Eastern time zone
    now_canada_east = now_utc.astimezone(timezone('Canada/Eastern'))
    await bot.say (now_canada_east.strftime(fmt) + " (Canada/Eastern)")

    # Convert to US/Central time zone
    now_central = now_utc.astimezone(timezone('US/Central'))
    await bot.say (now_central.strftime(fmt) + " (US/Central)")

    # Convert to US/Pacific time zone
    now_pacific = now_utc.astimezone(timezone('US/Pacific'))
    await bot.say (now_pacific.strftime(fmt) + " (US/Pacific)")

    # convert the time
@bot.command(name='Time convert', help='Converts the users inputed time to a time that they specify')
async def convertTime(date_str): #formerly printFutureTime #this will only work with a UTC time, so work this out in advance
    #date_str = "2009-05-05+22:28"
    datetime_obj = datetime.strptime(date_str, "%Y-%m-%d+%H:%M")

    fmt = "%Y-%m-%d %H:%M %Z%z"

    # Current time in UTC
    now_utc = datetime_obj.replace(tzinfo=timezone('UTC'))
    await bot.say (now_utc.strftime(fmt) + " (UTC)")

    # Convert to Europe/London time zone
    now_london = now_utc.astimezone(timezone('Europe/London'))
    await bot.say (now_london.strftime(fmt) + " (London)")

    # Convert to Europe/Berlin time zone
    now_berlin = now_utc.astimezone(timezone('Europe/Berlin'))
    await bot.say (now_berlin.strftime(fmt) + " (Berlin)")

    # Convert to CET time zone
    now_cet = now_utc.astimezone(timezone('CET'))
    await bot.say (now_cet.strftime(fmt) + " (CET)")

    # Convert to Israel time zone
    now_israel = now_utc.astimezone(timezone('Israel'))
    await bot.say (now_israel.strftime(fmt) + " (Israel)")

    # Convert to Canada/Eastern time zone
    now_canada_east = now_utc.astimezone(timezone('Canada/Eastern'))
    await bot.say (now_canada_east.strftime(fmt) + " (Canada/Eastern)")

    # Convert to US/Central time zone
    now_central = now_utc.astimezone(timezone('US/Central'))
    await bot.say (now_central.strftime(fmt) + " (US/Central)")

    # Convert to US/Pacific time zone
    now_pacific = now_utc.astimezone(timezone('US/Pacific'))
    await bot.say (now_pacific.strftime(fmt) + " (US/Pacific)")

    #Cool command the user is cool
@bot.group(name='cool', help='Just says someone is cool')
async def cool(ctx):
    #Says if a user is cool.
    #In reality this just checks if a subcommand is being invoked.
    if ctx.invoked_subcommand is None:
        await ctx.send('No, {0.subcommand_passed} is not cool'.format(ctx))

  # Fun command to say our bot is cool
@cool.command(name='bot')
async def _bot(ctx):
    #Is the bot cool?
    await ctx.send('Yes, the bot is cool.')

#Change a users nickname. Blocks changing nickname to the same thing.
@bot.command(pass_context=True,name='Change nickname', help='Change a users nickname' )
async def chnick(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.send(f'Nickname was changed for {member.mention} ')


# Searches for a youtube video off of the website from the users input
# Return the link to the video that was found
@bot.command(name='Youtube', help='Search for youtube video')
async def yt(self, ctx, *, search):
    query_string = urllib.parse.urlencode({'search_query': search})
    htm_content = urllib.request.urlopen(
        'http://www.youtube.com/results?' + query_string)
    search_results = re.findall(r'/watch\?v=(.{11})', htm_content.read().decode())
    await ctx.send('http://www.youtube.com/watch?v=' + search_results[0])

    # not sure if this is important, but I'll keep it for now

'''#from https://www.devdungeon.com/content/make-discord-bot-python
@client.event
async def on_message(message): #any action that is a respose to a message should go under here
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return'''

bot.run(TOKEN)
