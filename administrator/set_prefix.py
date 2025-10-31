import discord # ?
from discord.ext import commands
from misc.Buttons import ForbiddenButton
from misc.Exceptions import *
from misc.Messages import *

class Prefix(commands.Cog):
   from misc.SysPrefix import (
      get_prefix, # ignore weak
      update_prefix
   )
   def __init(self, core):
      self.core = core
      self.docs_button = ForbiddenButton()

   @commands.hybrid_command(
      name = 'set_prefix',
      aliases = ['prefix'],
      nsfw = False
   )
   async def set_prefix(
           self,
           ctx,
           new_prefix: str
   ):
      # permisisons
      try:
         if not ctx.author.guild_permissions.administrator:
            await ctx.send(
               embed = noperms(ctx)
            )
            return

         if new_prefix is None:
            await ctx.send(
               embed = noprefix(ctx)
            )
            return

         if len(new_prefix) > 4:
            await ctx.send(
               embed = lenprefix(ctx)
            )
            return

      # handler permissions
      except discord.Forbidden:
         await ctx.send(
            embed = exceptioncore(ctx),
            view = self.docs_button
         )
      except Exception as e:
         print(f'z-set_prefix: (permissions); {e}')

      # primary
      try:
         await self.update_prefix(ctx, new_prefix) # ignore unfilled and weak
         await ctx.send(
            embed = setprefix_(ctx, new_prefix)

         )
      # handler primary
      except discord.Forbidden:
         await ctx.send(
            embed = exceptioncore(ctx),
            view = self.docs_button
         )
      except Exception as e:
         print(f'z-set_prefix: (primary); {e}')

async def setup(core):
   await core.add_cog(Prefix(core))