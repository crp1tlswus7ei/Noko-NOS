import discord # ?
# from discord import app_commands
from discord.ext import commands
from misc.Buttons import ForbiddenButton
from misc.Exceptions import *
from misc.Messages import *

class AutoRole(commands.Cog):
   def __init__(self, core):
      self.core = core
      self.a_role = {}
      self.docs_button = ForbiddenButton()

   @commands.Cog.listener(
      name = 'auto-role'
   )
   async def on_member_join(
           self,
           user: discord.Member
   ):
      role_id = self.a_role.get(user.guild.id)

      # primary cog
      if role_id:
         role = user.guild.get_role(role_id)
         if role:
            try:
               await user.add_roles(
                  role,
                  reason = 'AutoRole'
               )
               print('g-auto_role: on')

            # handler primary
            except Exception as e:
               print(f'g-auto_role: (primary cog); {e}')

   @commands.command(
      name = 'set_autorole'
   )
   async def set_autorole(
           self,
           interaction: discord.Interaction,
           *,
           role: discord.Role
   ):
      # permissions
      try:
         if interaction.user.guild_permissions.administrator:
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

      # handler permissions
      except discord.Forbidden:
         await interaction.response.send_message(
            embed = corexcepctions(interaction),
            ephemeral = True,
            view = self.docs_button
         )
      except Exception as e:
         print(f'g-auto_role: (permissions); {e}')

      # primary
      try:
         self.a_role[interaction.guild.id] = role.id

         # embed
         autorole_ = embed_(
            interaction,
            f'AutoRole: {role.name}'
         )
         autorole_.set_footer(
            text = f'Automatization set by: {interaction.user.display_name}',
            icon_url = interaction.user.avatar
         )
         await interaction.response.send_message(
            embed = autorole_,
            ephemeral = False
         )

      # handler primary
      except discord.Forbidden:
         await interaction.response.send_message(
            embed = corexcepctions(interaction),
            ephemeral = True,
            view = self.docs_button
         )
      except Exception as e:
         print(f'g-auto_role: (primary); {e}')

# Cog
async def setup(core):
   await core.add_cog(AutoRole(core))