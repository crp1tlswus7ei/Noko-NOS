import discord # ?
from discord.ext import commands
from systems.SysPrefix import get_prefix, getactual_prefix, update_prefix # ignore weak
from misc.Buttons import *
from misc.Exceptions import *
from misc.Messages import *

class Prefix(commands.Cog):
   def __init__(self, core):
      self.core = core
      self.interactionb = InteractionB()
      self.docs = Forbidden()

   @commands.hybrid_command(
      name = 'set_prefix',
      aliases = ['prefix'],
      nsfw = False
   )
   async def set_prefix(
           self,
           ctx,
           *,
           new_prefix: str | None = None
   ):
      # misc
      guild_id = ctx.guild.id
      actual_prefix = await getactual_prefix(guild_id)

      # permissions
      try:
         if not ctx.author.guild_permissions.administrator:
            await ctx.send(
               embed = noperms(ctx),
               ephemeral = True
            )
            return

         if new_prefix is None:
            await ctx.send(
               embed = actualprefix_(ctx, actual_prefix)
            )
            return

         if len(new_prefix) > 2:
            await ctx.send(
               embed = lenprefix(ctx),
               ephemeral = True
            )
            return

      # handler permissions
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
         print(f'z-set_prefix: (permissions); {e}')
         return

      # primary
      try:
         await update_prefix(ctx, new_prefix) # ignore unfilled and weak
         await ctx.send(
            embed = setprefix_(ctx, new_prefix)
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
         print(f'z-set_prefix: (primary); {e}')
         return

# Cog
async def setup(core):
   await core.add_cog(Prefix(core))