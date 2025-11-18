import discord # ?
from discord import app_commands
from discord.ext import commands
from misc.Buttons import ForbiddenButton, InteractionButton
from misc.Exceptions import *
from misc.Messages import *

class Warnings(commands.Cog):
   from misc.SysWarn import get_warns
   def __init__(self, core):
      self.core = core
      self.int_button = InteractionButton()
      self.docs_button = ForbiddenButton()

   @app_commands.command(
      name = 'warnings',
      description = 'List of user warnings.',
      nsfw = False
   )
   @app_commands.describe(
      user = 'User to review warnings.'
   )
   async def warnings(
           self,
           interaction: discord.Interaction,
           user: discord.Member
   ):
      # permissions
      try:
         if interaction.user.id == user.id:
            await interaction.response.send_message(
               embed = nocore_(interaction),
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

      # handler permissions
      except discord.Forbidden:
         await interaction.response.send_message(
            embed = corexcepctions(interaction),
            ephemeral = True,
            view = self.docs_button
         )
      except discord.InteractionResponded:
         await interaction.response.send_message(
            embed = corexcepctions(interaction),
            ephemeral = True,
            view = self.int_button
         )
      except Exception as e:
         print(f'c-warnings: (permissions); {e}')
         return

      # primary
      user_id = str(user.id)
      try:
         user_warns = self.get_warns(user_id) # ignore unfilled
         if user_warns:
            await interaction.response.send_message(
               embed = warnings_(
                  interaction,
                  f'{user.display_name} warns:\n' + '\n'.join(user_warns)
               ),
               ephemeral = False
            )
         else:
            await interaction.response.send_message(
               embed = nowarnings_(interaction, user),
               ephemeral = False
            )

      # handler primary
      except discord.Forbidden:
         await interaction.response.send_message(
            embed = corexcepctions(interaction),
            ephemeral = True,
            view = self.docs_button
         )
      except discord.InteractionResponded:
         await interaction.response.send_message(
            embed = corexcepctions(interaction),
            ephemeral = True,
            view = self.int_button
         )
      except Exception as e:
         print(f'c-warnings: (primary); {e}')
         return

# Cog
async def setup(core):
   await core.add_cog(Warnings(core))