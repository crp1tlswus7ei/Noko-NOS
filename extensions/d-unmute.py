import discord # ?
from discord import app_commands
from discord.ext import commands
from misc.Buttons import *
from misc.Exceptions import *
from misc.Messages import *

class Unmute(commands.Cog):
   def __init__(self, core):
      self.core = core
      self.delete = Delete()
      self.interactionb = InteractionB()
      self.docs = Forbidden()

   @app_commands.command(
      name = 'unmute',
      description = 'Remove mute from a user.',
      nsfw = False
   )
   @app_commands.describe(
      user = 'User to remove mute.',
      reason = 'Reason for remove mute.'
   )
   @app_commands.default_permissions(
      manage_roles = True,
      mute_members = True
   )
   async def unmute(
           self,
           interaction: discord.Interaction,
           user: discord.Member,
           *,
           reason: str
   ):
      # permissions
      try:
         if user == self.core.user: #
            await interaction.response.send_message(
               embed = selfunmute_(interaction),
               ephemeral = True
            )
            return

         if interaction.user.id == user.id: #
            await interaction.response.send_message(
               embed = unmuteys_(interaction),
               ephemeral = True
            )
            return

         if not interaction.user.guild_permissions.manage_roles: #
            await interaction.response.send_message(
               embed = noperms_(interaction),
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
         print(f'd-unmute: (permissions); {e}')
         return

      # secondary
      m_r = discord.utils.get(  # mute role
         interaction.guild.roles,
         name = 'Mute'
      )
      hm_r = discord.utils.get(  # hard_mute role
         interaction.guild.roles,
         name = 'Hard Mute'
      )

      if not (m_r and hm_r): #
         await interaction.response.send_message(
            embed = nomuterole_(interaction),
            ephemeral = True
         )
         return

      ## primary
      try:
         if m_r in user.roles:
            await user.remove_roles(m_r, reason = reason)
            await interaction.response.send_message(
               embed = unmute_(interaction, user),
               ephemeral = False,
               view = self.delete
            )
         else:
            if hm_r in user.roles:
               await user.remove_roles(hm_r, reason = reason)
               await interaction.response.send_message(
                  embed = unmute_(interaction, user),
                  ephemeral = False,
                  view = self.delete
               )
            else:
               await interaction.response.send_message(
                  embed = nomute_(interaction, user),
                  ephemeral = True
               )
               return

      ## handler primary
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
         print(f'd-unmute: (primary); {e}')
         return

# Cog
async def setup(core):
   await core.add_cog(Unmute(core))