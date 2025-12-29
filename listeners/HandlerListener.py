import discord # ?
import traceback
from discord.ext import commands
from systems.SysHandler import *

class HandlerGlobal(commands.Cog):
   def __init__(self, core):
      self.core = core

   # prefix listener
   @commands.Cog.listener()
   async def on_command_error(
           self,
           ctx,
           error
   ):
      await logsave_(
         self,
         log_type = 'Command Error (ctx).',
         message = f'!!!: ({ctx.command}); {error}',
      )

   # interaction listener
   @commands.Cog.listener()
   async def on_app_command_error(
           self,
           interaction,
           error
   ):
      cmd = interaction.command.name if interaction.command else 'unknown'
      await logsave_(
         self,
         log_type = 'Command Error (int).',
         message = f'!!!: ({cmd}); {error}',
      )

   # global listener
   @commands.Cog.listener()
   async def on_error(
           self,
           event_method,
           *args,
           **kwargs
   ):
      tb = traceback.format_exc()
      await logsave_(
         self,
         log_type = 'Event Error.',
         message = f'!!!: ({event_method}); {tb}',
      )

# Cog
async def setup(core):
   await core.add_cog(HandlerGlobal(core))