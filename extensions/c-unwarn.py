import discord # ?
from discord import app_commands
from discord.ext import commands
from misc.Buttons import *
from misc.Exceptions import *
from misc.Messages import *

class Unwarn(commands.Cog):
   from systems.SysWarn import (
      get_warns,
      remove_warn
   )
   def __init__(self, core):
      self.core = core
      self.delete = Delete()
      self.interactionb = InteractionB()
      self.docs = Forbidden()

   @app_commands.command(
      name = 'unwarn',
      description = 'Removes only one warn from a user.'
   )
   @app_commands.describe(
      user = 'User to clean warns.'
   )
   @app_commands.default_permissions(
      manage_roles = True,
      mute_members = True
   )
   async def unwarn(
           self,
           interaction: discord.Interaction,
           user: discord.Member,
           *,
           amount: int
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

         if amount is None or amount <= 0:
            await interaction.response.send_message(
               embed = noamount_(interaction),
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
            view = self.docs
         )
      except discord.InteractionResponded:
         await interaction.response.send_message(
            embed = corexcepctions(interaction),
            ephemeral = True,
            view = self.interactionb
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
         if 1 <= amount <= len(warns_):
            self.remove_warn(user_id, amount - 1) # ignore unfilled
            await interaction.response.send_message(
               embed = unwarn_(interaction, user),
               ephemeral = False,
               view = self.delete
            )
         else:
            await interaction.response.send_message(
               embed = nullwarn_(interaction),
               ephemeral = False
            )

      # handler primary
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
         print(f'c-unwarn: (primary); {e}')
         return

# Cog
async def setup(core):
   await core.add_cog(Unwarn(core))