import discord # ?
from discord import app_commands
from discord.ext import commands
from misc.Buttons import ForbiddenButton
from misc.Exceptions import *
from misc.Messages import *

class Ban(commands.Cog):
   def __init__(self, core):
      self.core = core
      self.docs_button = ForbiddenButton()

   @app_commands.command(
      name = 'ban',
      description = 'Permanent expulsion to a user.',
      nsfw = False
   )
   @app_commands.describe(
      user = 'User to be sanctioned.',
      reason = 'The reason for sanction.'
   )
   async def ban(
           self,
           interaction: discord.Interaction,
           user: discord.Member,
           *,
           reason: str
   ):
      # permissions
      try:
         if interaction.user.id == user.id:
            await interaction.response.send_message(
               embed = banys_(interaction),
               ephemeral = True
            )
            return

         if not interaction.user.guild_permissions.ban_members:
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
         print(f'a-ban: (permissions); {e}')
         return

      # primary
      try:
         await user.ban(reason = reason)
         await interaction.response.send_message(
            embed = ban_(interaction, user),
            ephemeral = False
         )
      # handler primary
      except discord.Forbidden:
         await interaction.response.send_message(
            embed = corexcepctions(interaction),
            view = self.docs_button,
            ephemeral = True
         )
      except Exception as e:
         print(f'a-ban: (primary); {e}')

# Cog
async def setup(core):
   await core.add_cog(Ban(core))

# Solved