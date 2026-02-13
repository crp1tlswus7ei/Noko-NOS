import discord # ?
from discord import app_commands
from discord.ext import commands
from misc.Buttons import *
from misc.Messages import *
from misc.Exceptions import *

class SetMute(commands.Cog):
   import asyncio
   from misc.Roles import (
      CreateMuteRole,
      CreateHardMuteRole,
      m_over
   )
   def __init__(self, core):
      self.core = core
      self.docs = Forbidden()
      self.interactionb = InteractionB()
      self.delete = Delete()

   @app_commands.command(
      name = 'set_mute',
      description = 'Create Mute role and HardMute role.',
      nsfw = False
   )
   @app_commands.default_permissions(
      administrator = True,
      manage_roles = True
   )
   async def set_mute(
           self,
           interaction: discord.Interaction,
   ):
      # primary
      view = Advice(interaction)
      await interaction.response.send_message(
         embed = settingmr_(interaction),
         ephemeral = False,
         view = view
      )

      await view.wait()
      if not view.confirmed:
         await interaction.edit_original_response(
            embed = setmcancel_(interaction),
            view = None
         )
         return

      await interaction.edit_original_response(
         embed = stinprocess_(interaction),
         view = None
      )

      # secondary
      m_r = discord.utils.get( # mute
         interaction.guild.roles,
         name = 'Mute'
      )

      hm_r = discord.utils.get( # hard mute
         interaction.guild.roles,
         name = 'Hard Mute'
      )

      if not m_r:
         await self.CreateMuteRole(interaction) # ignore unfilled
         m_r = discord.utils.get(
            interaction.guild.roles, # re
            name = 'Mute'
         )
         # Channel permissions
         for channel in interaction.guild.channels:
            try:
               await channel.set_permissions(
                  target = m_r,
                  overwrite = self.m_over
               )
            # handler Channel
            except discord.Forbidden:
               await interaction.followup.send(
                  embed = channelerror_(interaction),
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
               print(f'd-set_mute: (ChannelPermissions-MuteRole); {e}')
               return

      if not hm_r:
         await self.CreateHardMuteRole(interaction) # ignore unfilled
         hm_r = discord.utils.get(
            interaction.guild.roles, # re
            name = 'Hard Mute'
         )
         # Channel permissions
         for channel in interaction.guild.channels:
            try:
               await channel.set_permissions(
                  target = hm_r,
                  overwrite = self.m_over
               )
            # handler Channel
            except discord.Forbidden:
               await interaction.followup.send(
                  embed = channelerror_(interaction),
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
               print(f'd-set_mute: (ChannelPermissions-HardMuteRole); {e}')
               return

      # hierarchy
      guild = interaction.guild
      bot_role = guild.me.top_role
      roles = list(reversed(guild.roles))
      bot_idx = roles.index(bot_role)
      newroles = (
         roles[:bot_idx + 1] + [m_r, hm_r] +
         [r for r in roles[bot_idx + 1:] if r not in (m_r, hm_r)]
      )
      positions = {}
      for i, role in enumerate(reversed(newroles)):
         positions[role] = i

      await guild.edit_role_positions(positions)

      # primary
      await self.asyncio.sleep(2)
      await interaction.edit_original_response(
         embed = stdone_(interaction),
         view = self.delete
      )

# Cog
async def setup(core):
   await core.add_cog(SetMute(core))
