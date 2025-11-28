import discord # ?
from discord import app_commands
from discord.ext import commands
from misc.Buttons import *
from misc.Exceptions import *
from misc.Messages import *

class HardMute(commands.Cog):
   import asyncio
   from misc.Roles import (
      CreateHardMuteRole,
      hm_over
   )
   def __init__(self, core):
      self.core = core
      self.delete = Delete()
      self.interactionb = InteractionB()
      self.docs = Forbidden()

   @app_commands.command(
      name = 'hard_mute',
      description = 'Remove all roles from user and applies mute.',
      nsfw = False
   )
   @app_commands.describe(
      user = 'User to be sanctioned.',
      reason = 'Reason for sanction.'
   )
   @app_commands.default_permissions(
      manage_roles = True,
      mute_members = True
   )
   async def hardmute(
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
               embed = hardmuteys_(interaction),
               ephemeral = True
            )
            return

         if interaction.user.guild_permissions.manage_roles:
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
            view = self.docs
         )
      except discord.InteractionResponded:
         await interaction.response.send_message(
            embed = corexcepctions(interaction),
            ephemeral = True,
            view = self.interactionb
         )
      except Exception as e:
         print(f'd-hard_mute: (permissions); {e}')
         return

      # secondary
      rm_ = [ # to remove
         r for r in user.roles if r != interaction.guild.default_role # everyone
      ]

      m_r = discord.utils.get( # mute role
         interaction.guild.roles,
         name = 'Mute'
      )
      hm_r = discord.utils.get( # hard_mute role
         interaction.guild.roles,
         name = 'Hard Mute'
      )

      if m_r in user.roles:
         await interaction.response.send_message(
            embed = alrmute_(interaction, user),
            ephemeral = True
         )
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
            # channel permissions
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
                     view = self.docs
                  )
               except discord.InteractionResponded:
                  await interaction.response.send_message(
                     embed = corexcepctions(interaction),
                     ephemeral = True,
                     view = self.interactionb
                  )
               except Exception as e:
                  print(f'd-hard_mute: (ChannelPermissions); {e}')
                  return

         # handler HardMuteRole
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
            print(f'd-hard_mute: (HardMuteRole); {e}')
            return

      # primary
      try:
         if hm_r not in user.roles:
            await user.remove_roles(*rm_, reason = reason)
            await self.asyncio.sleep(1) # 1-second sleep
            await user.add_roles(hm_r, reason = 'Hard Mute')
            await interaction.response.send_message(
               embed = hardmute_(interaction, user),
               ephemeral = False,
               view = self.delete
            )
         else:
            await interaction.response.send_message(
               embed = alrmute_(interaction, user),
               ephemeral = True
            )
            return

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
         print(f'd-hard_mute: (primary); {e}')
         return

# Cog
async def setup(core):
   await core.add_cog(HardMute(core))