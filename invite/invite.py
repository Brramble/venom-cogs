from redbot.core import commands

class Invite:
    """Invite Cog"""


@commands.command()
async def join(self, ctx):
    embed = discord.Embed(color=0xEE2222, title='Invite Link')
    embed.add_field(name='title 1', value='value 1')
    embed.set_footer(text='I am the footer!')
    await ctx.send(embed=embed)
