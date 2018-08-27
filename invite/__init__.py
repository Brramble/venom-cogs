from .invite import Invite

def setup(bot):
    bot.add_cog(Invite())
    bot.remove_command("invite")
