import discord # ?
from discord import app_commands
from discord.ext import commands
from misc.Buttons import *
from misc.Exceptions import *
from misc.Messages import *

class LockC(commands.Cog):
   from misc.Roles import f_overLockdown
   def __init__(self, core):
      self.core = core
      self.delete = Delete()
      self.interactionb = InteractionB()
      self.docs = Forbidden()

   @app_commands.command(
      name = 'lock_channel',
      description = 'Lock actual channel',
      nsfw = False
   )
   @app_commands.describe(
      channel = 'Channel to lock messages, actual channel by default.'
   )
   @app_commands.default_permissions(
      administrator = True
   )
   async def lock_channel(
           self,
           interaction: discord.Interaction,
           *,
           channel: discord.TextChannel = None
   ):
      # permissions
      try:
         if not interaction.user.guild_permissions.administrator: #
            await interaction.response.send_message(
               embed = noperms_(interaction),
               ephemeral = True
            )
            return

         if channel is None:
            pass

      ## handler permissions
      except discord.Forbidden:
         await interaction.response.send_message(
            embed = corexcepctions(interaction),
            ephemeral = True,
            view = self.docs
         )
      except discord.InteractionResponded:
         await interaction.response.send_message(
            embed = corexcepctions(interaction),
            ephemeral = True,
            view = self.interactionb
         )
      except Exception as e:
         print(f'f-lock_down: (permissions); {e}')
         return

      # re channel
      user = interaction.user
      channel = channel or interaction.channel # Actual channel

      ## primary
      try:
         await channel.set_permissions(
            interaction.guild.default_role, # everyone
            overwrite = self.f_overLockdown
         )
         await interaction.response.send_message(
            embed = lockdown_(interaction, user, channel),
            ephemeral = False,
            view = self.delete
         )

      ## handler primary
      except discord.Forbidden:
         await interaction.response.send_message(
            embed = corexcepctions(interaction),
            ephemeral = True,
            view = self.docs
         )
      except discord.InteractionResponded:
         await interaction.response.send_message(
            embed = corexcepctions(interaction),
            ephemeral = True,
            view = self.interactionb
         )
      except Exception as e:
         print(f'f-lock_down: (primary); {e}')
         return

# Cog
async def setup(core):
   await core.add_cog(LockC(core))