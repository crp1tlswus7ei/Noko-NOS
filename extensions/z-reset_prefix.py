import discord
from discord.ext import commands
from misc.SysPrefix import get_prefix, delete_prefix # ignore weak
from misc.Buttons import *
from misc.Exceptions import *
from misc.Messages import *

class ResetPrefix(commands.Cog):
   def __init__(self, core):
      self.core = core
      self.interactionb = InteractionB()
      self.docs = Forbidden()

   @commands.hybrid_command(
      name = 'reset_prefix',
      nsfw = False
   )
   async def reset_prefix(
           self,
           ctx
   ):
      # permissions
      try:
         if not ctx.author.guild_permissions.administrator:
            await ctx.send(
               embed = noperms(ctx),
               ephemeral = True
            )
            return

      # hancler permissions
      except discord.Forbidden:
         await ctx.send(
            embed = exceptioncore(ctx),
            view = self.docs
         )
      except discord.InteractionResponded:
         await ctx.send(
            embed = inteexception(ctx),
            view = self.interactionb
         )
      except Exception as e:
         print(f'z-reset_prefix: (permissions); {e}')
         return

      # primary
      try:
         await delete_prefix(ctx)
         await ctx.send(
            embed = resetprefix_(ctx)
         )

      # handler primary
      except discord.Forbidden:
         await ctx.send(
            embed = exceptioncore(ctx),
            view = self.docs
         )
      except discord.InteractionResponded:
         await ctx.send(
            embed = inteexception(ctx),
            view = self.interactionb
         )
      except Exception as e:
         print(f'z-reset_prefix: (permissions); {e}')

# Cog
async def setup(core):
   await core.add_cog(ResetPrefix(core))