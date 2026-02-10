import discord

async def CreateSpamRole(guild):
   await guild.create_role(
      name = 'Mute',
      permissions = discord.Permissions(4296082432),
      colour = discord.Colour.dark_red(),
      hoist = False,
      mentionable = False,
      reason = 'Spam Role.'
   )

async def CreateMuteRole(self, interaction: discord.Interaction): # ignore weak warning
   guild = interaction.guild
   top_ = guild.me.top_role
   muterole = await interaction.guild.create_role(
      name = 'Mute',
      permissions = discord.Permissions(66560),
      colour = discord.Color.dark_red(),
      hoist = False,
      mentionable = False,
      reason = 'Mute role (keep all roles).'
   )
   await muterole.edit(position = top_.position - 1)

async def CreateHardMuteRole(self, interaction: discord.Interaction): # ignore weak warning
   guild = interaction.guild
   top_ = guild.me.top_role
   hardmuterole = await interaction.guild.create_role(
      name = 'Hard Mute',
      permissions = discord.Permissions(66560),
      colour = discord.Colour.dark_red(),
      hoist = False,
      mentionable = False,
      reason = 'Hard mute role (remove all roles).'
   )
   await hardmuterole.edit(position = top_.position - 1)

m_over = discord.PermissionOverwrite(
   # text
   send_messages = False,
   add_reactions = False,
   create_public_threads = False,
   create_private_threads = False,
   send_messages_in_threads = False,
   embed_links = False,
   attach_files = False,
   # vc
   speak = False,
   connect = False,
   stream = False,
   use_voice_activation = False
)

f_overLockdown = discord.PermissionOverwrite(
   send_messages = False
)

f_overUnlock = discord.PermissionOverwrite(
   send_messages = True
)