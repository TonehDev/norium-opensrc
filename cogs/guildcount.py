import nextcord
from nextcord.ext import commands
import asyncio

class GuildCount(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["gc", "servercount", "sc"])
  async def guildcount(self, ctx):
    message = await ctx.send("Loading server count...")
    await asyncio.sleep(0.5)
    await message.edit(f"Loaded")
    embed = nextcord.Embed(
      title = "Server Count", 
      description = f"Norium Bot is in **{len(self.client.guilds)}** servers!", 
      color = nextcord.Color.blurple()
    )
    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(GuildCount(client))