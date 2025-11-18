import discord # ?
from discord import app_commands
from discord.ext import commands
from misc.Buttons import ForbiddenButton, InteractionButton
from misc.Exceptions import *
from misc.Messages import *

class CloneR(commands.Cog):
   def __init__(self, core):
      self.core = core
      self.int_button = InteractionButton()
      self.docs_button = ForbiddenButton()

   @app_commands.command(
      name = 'clone_role',
      description = 'Clone a existing role.',
      nsfw = False
   )
   @app_commands.describe(
      role = 'Role to clone.'
   )
   async def clone_role(
           self,
           interaction: discord.Interaction,
           *,
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
            view = self.docs_button
         )
      except discord.InteractionResponded:
         await interaction.response.send_message(
            embed = corexcepctions(interaction),
            ephemeral = True,
            view = self.int_button
         )
      except Exception as e:
         print(f'g-clone_role: (permissions); {e}')
         return

      # primary
      try:
         cloner_ = await interaction.guild.create_role(
            name = f'{role.name} (clone)',
            permissions = role.permissions,
            colour = role.colour,
            hoist = role.hoist,
            mentionable = role.mentionable,
            reason = f'Role cloned by: {interaction.user.display_name}'
         )

         # set
         await cloner_.edit(
            position = role.position - 1
         )

         # embed
         clone_ = embed_(
            interaction,
            f'Clone: {role.name}'
         )
         clone_.set_footer(
            text = f'Clone by {interaction.user.display_name}',
            icon_url = interaction.user.avatar
         )
         await interaction.response.send_message(
            embed = clone_,
            ephemeral = False
         )

      # hancler primary
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
         print(f'g-clone_role: (primary); {e}')
         return

# Cog
async def setup(core):
   await core.add_cog(CloneR(core))