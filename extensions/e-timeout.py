import discord # ?
from datetime import timedelta
from discord import app_commands
from discord.ext import commands
from misc.Buttons import *
from misc.Exceptions import *
from misc.Messages import *

class Timeout(commands.Cog):
   def __init__(self, core):
      self.core = core
      self.delete = Delete()
      self.interactionb = InteractionB()
      self.docs = Forbidden()

   @app_commands.command(
      name = 'timeout',
      description = 'Mutes a user for certain period of time.',
      nsfw = False
   )
   @app_commands.describe(
      user = 'User to be santioned.',
      duration = 'Minutes of sanction, 10 minutes by default.',
      reason = 'Reason for sanction.',
   )
   @app_commands.default_permissions(
      manage_roles = True,
      mute_members = True
   )
   async def timeout(
           self,
           interaction: discord.Interaction,
           user: discord.Member,
           duration: int = 10,
           *,
           reason: str
   ):
      # permissions
      try:
         if user == self.core.user:
            await interaction.response.send_message(
               embed = selftimeout_(interaction),
               ephemeral = True
            )
            return

         if interaction.user.id == user.id: #
            await interaction.response.send_message(
               embed = hardmuteys_(interaction),
               ephemeral = True
            )
            return

         if not interaction.user.guild_permissions.mute_members: #
            await interaction.response.send_message(
               embed = noperms_(interaction),
               ephemeral = True
            )
            return

         if duration <= 0 or duration >= 10080:
            await interaction.response.send_message(
               embed = noduration_(interaction),
               ephemeral = True
            )
            return

         if user is None: #
            await interaction.response.send_message(
               embed = nouser_(interaction),
               ephemeral = True
            )
            return

         if interaction.user.top_role <= user.top_role: #
            await interaction.response.send_message(
               embed = usrtop_(interaction),
               ephemeral = True
            )
            return

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
         print(f'e-timeout: (permissions); {e}')
         return

      ## primary
      try:
         await user.timeout(
            timedelta(minutes = duration),
            reason = reason
         )
         await interaction.response.send_message(
            embed = timeout_(interaction, user, duration),
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
            embed=corexcepctions(interaction),
            ephemeral = True,
            view = self.interactionb
         )
      except Exception as e:
         print(f'e-timeout: (primary); {e}')
         return

# Cog
async def setup(core):
   await core.add_cog(Timeout(core))