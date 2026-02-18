import discord # ?
import asyncio
from discord import app_commands
from discord.ext import commands
from misc.Buttons import *
from misc.Exceptions import *
from misc.Messages import *

class Clear(commands.Cog):
   def __init__(self, core):
      self.core = core

   @commands.hybrid_command(
      name = 'clear',
      nsfw = False
   )
   @app_commands.describe(
      amount = 'Amount of messages to clear, 10 by default.',
   )
   async def clear(
           self,
           ctx,
           *,
           amount: int = 10
   ):
      # permissions
      try:
         if not ctx.author.guild_permissions.manage_messages: #
            await ctx.send(
               embed = noperms(ctx),
               ephemeral = True
            )
            return

         if amount <= 0 or amount >= 9999: #
            await ctx.send(
               embed = noamount(ctx),
               ephemeral = True
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

      # loading
      if ctx.interaction:
         await ctx.interaction.response.defer(
            thinking = True,
            ephemeral = True
         )

      msg = await ctx.send(
         embed = loadingclear(ctx),
         ephemeral = True
      )
      await asyncio.sleep(2)

      # primary
      delete_ = DeleteCtx(ctx.author)
      try:
         deleted = await ctx.channel.purge(
            limit = amount
         )
         real_deleted = len(deleted)

         if ctx.interaction:
            await msg.edit(
               embed = clear(
                  ctx,
                  amount = real_deleted
               )
            )
         else:
            await ctx.send(
               embed = clear(
                  ctx,
                  amount = real_deleted
               ),
               view = delete_
            )

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