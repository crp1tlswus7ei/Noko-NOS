import discord # ?
from discord.ext import commands
from misc.Exceptions import *
from misc.Messages import *

class Clear(commands.Cog):
   import asyncio
   def __init__(self, core):
      self.core = core

   @commands.hybrid_command(
      name = 'clear',
      nsfw = False
   )
   async def clear(
           self,
           ctx,
         # user: discord.Member,
           *,
           amount: int
   ):
      # permissions
      try:
         if ctx.author.guild_permissions.manage_messages:
            await ctx.send(
               embed = noperms(ctx)
            )
            return

         if amount is None or amount <= 0:
            await ctx.send(
               embed = noamount(ctx)
            )
            return

      # handler permissions
      except discord.Forbidden:
         await ctx.send(
            embed = exceptioncore(ctx)
         )
      except Exception as e:
         print(f'x-clear: (permissions); {e}')
         return

      # primary
      try:
         await ctx.channel.purge(
            limit = amount + 1
         )
         mclear = clear(ctx, amount)
         await ctx.send(
            embed = mclear
         )
         await self.asyncio.sleep(3) # sleep 3-seconds
         await mclear.delete()

      # handler primary
      except discord.Forbidden:
         await ctx.send(
            embed = exceptioncore(ctx)
         )
      except Exception as e:
         print(f'x-clear: (primary); {e}')
         return

# Cog
async def setup(core):
   await core.add_cog(Clear(core))