import nextcord
from nextcord.ext import commands
import config

class Warnings(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["w"])
  @commands.has_permissions(manage_messages=True)
  async def warn(self, ctx, member: nextcord.Member = None, *, reason="No reason provided."):
    embed = nextcord.Embed(
        title="Warn",
        description=
        f"Successfully warned user ``{member.name}#{member.discriminator}``.",
        color=nextcord.Color.green())
    embed.add_field(name="Reason", value=f"{reason}")
    await ctx.send(embed=embed)

    embed = nextcord.Embed(
        title="You were warned",
        description=
        "⚠️ You have been warned in a guild. More information below.",
        color=nextcord.Color.red())
    embed.add_field(name="Guild", value=f"{ctx.guild.name}", inline=False)
    embed.add_field(name="Moderator",
                    value=f"{ctx.author.mention}",
                    inline=False)
    embed.add_field(name="Reason", value=f"{reason}", inline=False)
    await member.send(embed=embed)


  @warn.error
  async def warn_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = nextcord.Embed(title="Invalid Syntax",
                               description="``<> Required, [] Optional``",
                               color=nextcord.Color.red())
        embed.add_field(name="Usage",
                        value=f"-warn @<user> [reason]``",
                        inline=False)
        embed.add_field(name="Example",
                        value="``-warn BestGamer pinging mods for no reason``",
                        inline=False)
        await ctx.send(embed=embed)

    elif isinstance(error, commands.MissingPermissions):
        embed = nextcord.Embed(
            title="No Permissions",
            description="You are missing the ``MANAGE_MESSAGES`` permission.",
            color=nextcord.Color.red())
        await ctx.send(embed=embed)

    elif isinstance(error, commands.MemberNotFound):
        embed = nextcord.Embed(
            title="Member Not Found",
            description=
            f"No member named ``{ctx.member.name}#{ctx.member.discriminator}`` found.",
            color=nextcord.Color.red())
        await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Warnings(client))