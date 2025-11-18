import asyncio
import discord # ?
from discord import app_commands
from discord.ext import commands
from misc.Buttons import ForbiddenButton, InteractionButton
from misc.Exceptions import *
from misc.Messages import *

class SoftBan(commands.Cog):
   def __init__(self, core):
      self.core = core
      self.int_button = InteractionButton()
      self.docs_button = ForbiddenButton()

   @app_commands.command(
      name = 'soft-ban',
      description = 'Temporary sanction. Useful for deleting messages from a user.',
      nsfw = False
   )
   @app_commands.describe(
      user = 'User to be sanctioned.',
      reason = 'Reason for sanction.'
   )
   async def softban(
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
      except discord.InteractionResponded:
         await interaction.response.send_message(
            embed = corexcepctions(interaction),
            ephemeral = True,
            view = self.int_button
         )
      except Exception as e:
         print(f'a-soft_ban: (permissions); {e}')
         return

      # primary
      try:
         await user.ban(reason = reason)
         await asyncio.sleep(1) # 1 second sleep
         await user.unban()
         await interaction.response.send_message(
            embed = softban_(interaction, user),
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
         print(f's-soft_ban: (primary); {e}')
         return

# Cog
async def setup(core):
   await core.add_cog(SoftBan(core))

# Solved