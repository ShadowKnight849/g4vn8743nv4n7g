import discord
from discord.ext import commands

class userCommands():
    def __init__(self, bot):
        self.bot = bot

    #This is a basic example of a call and response command. You tell it do "this" and it does it.
    @commands.command()
    async def ping(self):
        await self.bot.say(":ping_pong: Pong!")

    @commands.command(help="| Set your role | Required Permissions: None", pass_context=True)
    async def role(self, status: discord.Message):
        await self.bot.add_reaction(status.message, "✅")
        for role in status.message.author.roles:
            await self.bot.say(str(role.name))

        #await asyncio.sleep(1)

    #Command error handler
    @role.error
    async def role_handler(self, error, cxt):

        #The Poster is missing some arguments
        if "required" in str(error).lower():
            await self.bot.say("You are missing some arguments!")

        #We can't find the error
        else:
            await self.bot.say("<@345910953822388226> Weird error alert! " + str(error))



def setup(bot):
    bot.add_cog(userCommands(bot))
