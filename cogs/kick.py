import nextcord
from nextcord.ext import commands

class Kick(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["k"])
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member : nextcord.Member, *, reason="No reason provided."):
    await member.kick(reason=reason)
    embed = nextcord.Embed(
      title = "Kick", 
      description = f"Successfully kicked user ``{member.name}#{member.discriminator}``", 
      color = nextcord.Color.green()
    )
    embed.add_field(name = "Reason", value = f"{reason}")
    await ctx.send(embed=embed)

    embed = nextcord.Embed(
      title = "You were kicked",
      description = "⚠️ You were kicked from a guild. More information below.",
      color = nextcord.Color.red()
    )
    embed.add_field(
        name = "Guild",
        value = f"{ctx.guild.name}",
        inline = False
    )
    embed.add_field(
        name = "Moderator",
        value = f"{ctx.author.mention}",
        inline = False
    )
    embed.add_field(
        name = "Reason",
        value = f"{reason}",
        inline = False
    )
    await member.send(embed=embed)
    await member.kick(reason=reason)

  # Error Handling

  @kick.error
  async def kick_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      embed = nextcord.Embed(
          title = "Invalid Syntax",
          description = "``<> Required, [] Optional``",
          color = nextcord.Color.red()
      )
      embed.add_field(name = "Usage", value = "``-kick @<user> [reason]``", inline = False)
      embed.add_field(name = "Example", value = "``-kick @BestGamer being too toxic``", inline = False)
      await ctx.send(embed=embed)

    elif isinstance(error, commands.MissingPermissions):
      embed = nextcord.Embed(
        title = "No Permissions",
        description = "You are missing the ``KICK_MEMBERS`` permission.",
        color = nextcord.Color.red()
      )
      await ctx.send(embed=embed)

    elif isinstance(error, commands.MemberNotFound):
      embed = nextcord.Embed(
        title = "Member Not Found",
        description = f"No member named ``{ctx.member.name}#{ctx.member.discriminator}`` found.",
        color = nextcord.Color.red()
      )
      await ctx.send(embed=embed)

    elif isinstance(error, commands.BotMissingPermissions):
            embed = nextcord.Embed(
              title="I'm missing permissions",
              description=
              f"I am missing the ``KICK_MEMBERS`` permission.",
              color=nextcord.Color.red()
            )
            await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Kick(client))