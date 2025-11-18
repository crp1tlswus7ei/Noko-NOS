import discord # ?
from discord import app_commands
from discord.ext import commands
from misc.Buttons import ForbiddenButton, InteractionButton
from misc.Exceptions import *
from misc.Messages import *

class MassRole(commands.Cog):
   def __init__(self, core):
      self.core = core
      self.count = 0
      self.int_button = InteractionButton()
      self.docs_button = ForbiddenButton()

   @app_commands.command(
      name = 'mass_role',
      description = 'Add a role to the entire server.',
      nsfw = False
   )
   @app_commands.describe(
      role = 'Role to add globally.'
   )
   async def mass_role(
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
         print(f'mass_role: (permissions); {e}')
         return

      # primary
      try:
         members = interaction.guild.members

         await interaction.response.send_message(
            embed = inprocessrole_(interaction),
            ephemeral = False
         )

         # secondary
         for member in members:
            try:
               await member.add_roles(
                  role,
                  reason = 'Auto mass_role by Noko.'
               )
               self.count += 1

            # handler secondary
            except discord.Forbidden:
               await interaction.followup.send(
                  embed = corexcepctions(interaction),
                  ephemeral = True, # check
                  view = self.docs_button
               )
            except discord.InteractionResponded:
               await interaction.response.send_message(
                  embed = corexcepctions(interaction),
                  ephemeral = True,
                  view = self.int_button
               )
            except Exception as e:
               print(f'mass_role: (secondary); {e}')
               return

         # success
         msg = await interaction.original_response()
         await msg.edit(
            embed = massrole_(interaction, role)
         )

      # handler primary
      except discord.Forbidden:
         await interaction.followup.send(
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
         print(f'mass_role: (primary); {e}')
         return

# Cog
async def setup(core):
   await core.add_cog(MassRole(core))