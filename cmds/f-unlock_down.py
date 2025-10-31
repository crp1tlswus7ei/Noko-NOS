import discord # ?
from discord import app_commands
from discord.ext import commands
from misc.Buttons import ForbiddenButton
from misc.Exceptions import *
from misc.Messages import *

class UnlockC(commands.Cog):
   from misc.Roles import f_overUnlock
   def __init__(self, core):
      self.core = core
      self.docs_button = ForbiddenButton()

   @app_commands.command(
      name = 'unlock_channel',
      description = 'Unlock actual channel',
      nsfw = False
   )
   @app_commands.describe(
      channel = 'Channel to unlock.'
   )
   async def unlock_channel(
           self,
           interaction: discord.Interaction,
           user: discord.Member,
           channel: discord.TextChannel = None
   ):
      # permissions
      try:
         if not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message(
               embed = noperms_(interaction),
               ephemeral = True
            )
            return

         if channel is None:
            pass

      # handler permissions
      except discord.Forbidden:
         await interactionr.response.send_message(
            embed = corexcepctions(interaction),
            ephemeral = True,
            view = self.docs_button
         )
      except Exception as e:
         print(f'd-unlock_down: (permissions); {e}')

      # re channel
      channel = channel or interaction.channel # Actual channel

      # primary
      try:
         await channel.set_permissions(
            interaction.guild.default_role, # everyone
            overwrite = self.f_overUnlock
         )
         await interaction.response.send_message(
            embed = unlockdown_(interaction, user, channel),
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
         print(f'f-unlock_down: (primary); {e}')

# Cog
async def setup(core):
   await core.add_cog(UnlockC(core))