import discord # ?
from discord import app_commands
from discord.ext import commands
from misc.Buttons import ForbiddenButton
from misc.Exceptions import *
from misc.Messages import *

class Unmute(commands.Cog):
   from misc.Roles import (
      CreateMuteRole,
      CreateHardMuteRole,
      m_over,
      hm_over
   )
   def __init__(self, core):
      self.core = core
      self.docs_button = ForbiddenButton()

   @app_commands.command(
      name = 'unmute',
      description = 'Remove mute from a user.',
      nsfw = False
   )
   @app_commands.describe(
      user = 'User to remove mute.',
      reason = 'Reason for remove mute.'
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
         if interaction.user.id == user.id:
            await interaction.response.send_message(
               embed = unmuteys_(interaction),
               ephemeral = True
            )
            return

         if interaction.user.guild_permissions.manage_permissions:
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
            ephemeral = True
         )
      except Exception as e:
         print(f'd-unmute: (permissions); {e}')

      # secondary
      m_r = discord.utils.get(  # mute role
         interaction.guild.roles,
         name = 'Mute'
      )
      hm_r = discord.utils.get(  # hard_mute role
         interaction.guild.roles,
         name = 'Hard Mute'
      )

      # MuteRole
      if not m_r:
         try:
            await self.CreateMuteRole(interaction)
            m_r = discord.utils.get(
               interaction.guild.roles, # re
               name = 'Mute'
            )
            await interaction.response.send_message(
               embed = autmrole_(interaction),
               ephemeral = True
            )
            # channel permissions
            for channel in interaction.guild.channels:
               try:
                  await channel.set_permissions(
                     target = m_r,
                     overwrite = self.m_over
                  )
               # handler channel
               except discord.Forbidden:
                  await interaction.response.send_message(
                     embed = channelerror_(interaction),
                     ephemeral = True
                  )
               except Exception as e:
                  print(f'd-unmute: (ChannelPermissions-Mute); {e}')
                  return

         # handler MuteRole
         except discord.Forbidden:
            await interaction.response.send_message(
               embed = corexcepctions(interaction),
               ephemeral = True
            )
         except Exception as e:
            print(f'd-unmute: (MuteRole); {e}')
            return

      # HardMuteRole
      if not hm_r:
         try:
            await self.CreateHardMuteRole(interaction)
            hm_r = discord.utils.get(
               interaction.guild.roles, # re
               name = 'Hard Mute'
            )
            await interaction.response.send_message(
               embed = authmrole_(interaction),
               ephemeral = True
            )
            # Channel permissions
            for channel in interaction.guild.channels:
               try:
                  await channel.set_permissions(
                     target = hm_r,
                     overwrite = self.hm_over
                  )
               # handler channel
               except discord.Forbidden:
                  await interaction.response.send_message(
                     embed = channelerror_(interaction),
                     ephemeral = True,
                     view = self.docs_button
                  )
               except Exception as e:
                  print(f'd-unmute: (ChannelPermissions-HardMute); {e}')

         # handler HardMuteRole
         except discord.Forbidden:
            await interaction.response.send_message(
               embed = corexcepctions(interaction),
               ephemeral = True,
               view = self.docs_button
            )
         except Exception as e:
            print(f'd-unmute: (HardMuteRole); {e}')

      # primary
      try:
         if m_r in user.roles:
            await user.remove_roles(m_r, reason = reason)
            await interaction.response.send_message(
               embed = unmute_(interaction, user),
               ephemeral = False
            )
         else:
            if hm_r in user.roles:
               await user.remove_roles(hm_r, reason = reason)
               await interaction.response.send_message(
                  embed = unmute_(interaction, user),
                  ephemeral = False
               )
            else:
               await interaction.response.send_message(
                  embed = nomute_(interaction, user),
                  ephemeral = True
               )
               return

      # handler primary
      except discord.Forbidden:
         await interaction.response.send_message(
            embed = corexcepctions(interaction),
            ephemeral = True,
            view = self.docs_button
         )
      except Exception as e:
         print(f'd-unmute: (primary); {e}')

# Cog
async def setup(core):
   await core.add_cog(Unmute(core))