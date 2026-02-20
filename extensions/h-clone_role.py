import discord # ?
import asyncio
from discord import app_commands
from discord.ext import commands
from misc.Buttons import *
from misc.Exceptions import *
from misc.Messages import *

class CloneR(commands.Cog):
   def __init__(self, core):
      self.core = core
      self.delete = Delete()
      self.interactionb = InteractionB()
      self.docs = Forbidden()

   @app_commands.command(
      name = 'clone_role',
      description = 'Clone a existing role.',
      nsfw = False
   )
   @app_commands.describe(
      role = 'Role to clone.'
   )
   @app_commands.default_permissions(
      administrator = True
   )
   async def clone_role(
           self,
           interaction: discord.Interaction,
           *,
           role: discord.Role
   ):
      # permissions
      try:
         if not interaction.user.guild_permissions.administrator: #
            await interaction.response.send_message(
               embed = noperms_(interaction),
               ephemeral = True
            )
            return

         if role >= interaction.user.top_role and interaction.user: #
             await interaction.response.send_message(
                 embed = roletop_(interaction),
                 ephemeral = True
             )
             return

         if role == interaction.guild.me.top_role: #
            await interaction.response.send_message(
               embed = rolecore_(interaction),
               ephemeral = True
            )
            return

         if role == interaction.guild.default_role: #
            await interaction.response.send_message(
               embed = defaultclone_(interaction),
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
         print(f'g-clone_role: (permissions); {e}')
         return

      # defer
      await interaction.response.send_message(
         embed = loadingclone_(interaction),
         ephemeral = False
      )

      ## primary
      try:
         cloner_ = await interaction.guild.create_role(
            name = f'{role.name} (clone)',
            permissions = role.permissions,
            colour = role.colour,
            hoist = role.hoist,
            mentionable = role.mentionable,
            reason = f'Role cloned by: {interaction.user.display_name}'
         )

         # hierarchy
         await cloner_.edit(
            position = role.position - 1
         )

         # embed
         clone_ = embed_(
            interaction,
            f'Clone: {role.name}'
         )
         clone_.set_footer(
            text = f'Clone by: {interaction.user.display_name}',
            icon_url = interaction.user.avatar
         )
         await asyncio.sleep(2)
         await interaction.edit_original_response(
            embed = clone_,
            view = self.delete
         )

      ## handler primary
      except discord.Forbidden:
         await interaction.followup.send(
            embed = corexcepctions(interaction),
            ephemeral = True,
            view = self.docs
         )
      except discord.InteractionResponded:
         await interaction.followup.send(
            embed = corexcepctions(interaction),
            ephemeral = True,
            view = self.interactionb
         )
      except Exception as e:
         print(f'g-clone_role: (primary); {e}')
         return

# Cog
async def setup(core):
   await core.add_cog(CloneR(core))