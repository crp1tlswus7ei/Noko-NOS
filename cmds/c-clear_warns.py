import discord # ?
from discord import app_commands
from discord.ext import commands
from misc.Buttons import ForbiddenButton
from misc.Exceptions import *
from misc.Messages import *

class ClearWarns(commands.Cog):
   from misc.SysWarn import (
      get_warns,
      c_warns
   )
   def __init__(self, core):
      self.core = core
      self.docs_button = ForbiddenButton()

   @app_commands.command(
      name = 'clear_warns',
      description = 'Clear all warnings from a user.',
      nsfw = False
   )
   @app_commands.describe(
      user = 'User to clean warns.'
   )
   async def clear_warns(
           self,
           interaction: discord.Interaction,
           user: discord.Member
   ):
      # permissions
      try:
         if interaction.user.id == user.id:
            await interaction.response.send_message(
               embed = clearys_(interaction),
               ephemeral = True
            )
            return

         if not interaction.user.guild_permissions.manage_roles:
            await interaction.response.send_message(
               embed = noperms_(interaction),
               ephemeral = True
            )
            return

         if user is None:
            await interaction.response.send_message(
               embed = nouser_(interaction),
               ephemeral = True
            )
            return

         if interaction.user.top_role <= user.top_role:
            await interaction.response.send_message(
               embed = usrtop_(interaction),
               ephemeral = True
            )
            return

      # handler permissions
      except discord.Forbidden:
         await interaction.response.send_message(
            embed = corexcepctions(interaction),
            ephemeral = True,
            view = self.docs_button
         )
      except Exception as e:
         print(f'c-clear_warns: (permissions); {e}')
         return

      # secondary
      user_id = str(user.id)
      warns_ = self.get_warns(user_id) # ignore unfilled

      if not warns_:
         await interaction.response.send_message(
            embed = nowarns_(interaction, user),
            ephemeral = True
         )
         return

      # primary
      try:
         self.c_warns(user_id) # ignore unfilled
         await interaction.response.send_message(
            embed = clearw_(interaction, user),
            ephemeral = False
         )
      # handler primary
      except discord.Forbidden:
         await interaction.response.send_message(
            embed = corexcepctions(interaction),
            ephemeral = True,
            view = self.docs_button
         )
      except Exception as e:
         print(f'c-clear_warns: (primary); {e}')

# Cog
async def setup(core):
   await core.add_cog(ClearWarns(core))