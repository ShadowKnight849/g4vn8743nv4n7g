import discord
from discord.ext import commands

class modCommands():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="| Set bot status | Required Permissions: Manage_Channels", pass_context=True)
    #Does the poster have permissions?
    @commands.has_permissions(manage_channels=True)
    async def status(self, status: discord.Message):
        await self.bot.add_reaction(status.message, "✅")

        await self.bot.say("Changing my status to: {}".format(str(str(status.message.content).replace("!status ", ""))))
        await self.bot.change_presence(game=discord.Game(name=str(str(status.message.content).replace("!status ", ""))))

    #Command error handler
    @status.error
    async def status_handler(self, error, cxt):
        #The Poster doesn't have permissions
        if "check functions" in str(error).lower():
            await self.bot.say("You are missing the required permissions to run this command!")

        #The Poster is missing some arguments
        elif "required" in str(error).lower():
            await self.bot.say("You are missing some arguments!")

        #We can't find the error
        else:
            await self.bot.say("<@345910953822388226> Weird error alert! " + str(error))


def setup(bot):
    bot.add_cog(modCommands(bot))
