import nextcord
from nextcord.ext import commands
import aiohttp
import asyncio

class CatAndDog(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def cat(self, ctx):
    async with aiohttp.ClientSession() as cs:
      async with cs.get("https://aws.random.cat/meow") as r:
        data = await r.json()

        message = await ctx.send("Finding a cat...")
        await asyncio.sleep(0.5)
        await message.edit(f"Found a cat!")
        embed = nextcord.Embed(
          title = "🐱 Meowww...",
          color = nextcord.Color.random()
        )
        embed.set_image(url = data['file'])
        await ctx.send(embed=embed)

  @commands.command()
  async def dog(self, ctx):
    async with aiohttp.ClientSession() as cs:
      async with cs.get("https://random.dog/woof.json") as r:
        data = await r.json()


        message = await ctx.send("Finding a dog...")
        await asyncio.sleep(0.5)
        await message.edit(f"Found a dog!")
        embed = nextcord.Embed(
          title = "🐕 Woof, woof!",
          color = nextcord.Color.random()
        )
        embed.set_image(url = data['url'])
        await ctx.send(embed=embed)

def setup(client):
  client.add_cog(CatAndDog(client))