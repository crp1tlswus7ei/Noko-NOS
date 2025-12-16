import discord # ?
from discord import app_commands
from discord.ext import commands
from systems.SysAutoRole import *
from misc.Buttons import *
from misc.Exceptions import *
from misc.Messages import *

class AutoRole(commands.Cog):
   def __init__(self, core):
      self.core = core
      self.delete = Delete()
      self.interactionb = InteractionB()
      self.docs = Forbidden()

   @app_commands.command(
      name = 'set_autorole',
      description = 'Configure a role to automatically add new users.',
      nsfw = False
   )
   @app_commands.describe(
      status = 'Enable or disale Auto role.',
      role = 'Role to automatically add new users.',
   )
   @app_commands.default_permissions(
      administrator = True
   )
   async def set_autorole(
           self,
           interaction: discord.Interaction,
           status: bool,
           role: discord.Role
   ):
      # permissions
      try:
         if not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message(
               embed = noperms_(interaction),
               ephemeral = True
            )
            return

         # Disabled
         if not status:
            await toggle(interaction.guild.id, False)
            await interaction.response.send_message(
               embed = autoff_(interaction),
               ephemeral = True
            )

         if role is None:
            await interaction.response.send_message(
               embed = norole_(interaction),
               ephemeral = True
            )
            return

         if role >= interaction.user.top_role and interaction.user:
            await interaction.response.send_message(
               embed = roletop_(interaction),
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
         print(f'z-auto_role: (permissions); {e}')
         return

      # primary
      try:
         await set_role(interaction.guild.id, role.id)
         await interaction.response.send_message(
            embed = autorole_(interaction, role),
            ephemeral = False,
            view = self.delete
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
         print(f'z-auto_role: (primary); {e}')

# Cog
async def setup(core):
   await core.add_cog(AutoRole(core))