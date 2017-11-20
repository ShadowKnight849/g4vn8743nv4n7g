import discord
import asyncio
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
        Factions = ["Mr.House", "NCR",  "Legion", "BoS", "RailRoad", "Minutemen", "Institute", "Vault Dweller"]

        if str(status.message.content).replace("!role ", "") not in str(Factions).lower():
            await self.bot.add_reaction(status.message, "❎")
            await self.bot.say("Role not found!")

        else:
            await self.bot.add_reaction(status.message, "✅")
            for role in status.message.author.roles:
                if str(role.name) in Factions:
                    await self.bot.remove_roles(status.message.author, discord.utils.get(status.message.server.roles, id=role.id)) #status.message.author, discord.Role(role.id)

            await self.bot.add_roles(status.message.author, discord.utils.get(status.message.server.roles, name=str(status.message.content).replace("!role ", "")))

        await asyncio.sleep(1)
        await self.bot.delete_message(status.message)

        deleted = await self.bot.purge_from(status.message.channel, limit=1)

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
