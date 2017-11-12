try:
    import discord
    import asyncio
    from discord.ext.commands import Bot
    from discord.ext import commands
    import platform
except:
    print("You need to install the discord.py api")
    sys.exit(-1)

botVersion = 0.1
prefix = "!"
startup_extensions = ["modCommands", "userCommands"]

# Here you can modify the bot's prefix and description and wether it sends help in direct messages or not.
client = Bot(description="Here are some commands for you to try!", command_prefix=prefix, pm_help = True)

#Test Code
@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('Current Discord.py Version: {} | Current Python Version: {} |Current Bot Version: {}'.format(discord.__version__, platform.python_version(), str(botVersion)))
    print('--------')
    print('Use this link to invite {}:'.format(client.user.name))
    print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
    print('--------')

@client.command()
async def reloadCodeBase():
    for extension in startup_extensions:
        try:
            client.unload_extension(extension)
            
            await client.say("Reloading: {}".format(extension))
            await asyncio.sleep(0.5)
            
            client.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

#Add our modules.
if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            
            client.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

    #We can't have the token public now can we?
    tokenFile = open("../Token.txt")
    client.run(tokenFile.read())
    tokenFile.close()
