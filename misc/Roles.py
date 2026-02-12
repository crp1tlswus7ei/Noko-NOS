import discord

f_overLockdown = discord.PermissionOverwrite(send_messages = False)
f_overUnlock = discord.PermissionOverwrite(send_messages = True)

# Roles (hard and mute)
async def CreateMuteRole(
        self, # ignore weak
        interaction: discord.Interaction
):
   guild = interaction.guild
   mr = await interaction.guild.create_role(
      name = 'Mute',
      permissions = discord.Permissions(66560),
      colour = discord.Color.dark_red(),
      hoist = False,
      mentionable = False,
      reason = 'Mute role (keep all roles).'
   )

async def CreateHardMuteRole(
        self, # ignore weak
        interaction: discord.Interaction
):
   guild = interaction.guild
   hmr = await interaction.guild.create_role(
      name = 'Hard Mute',
      permissions = discord.Permissions(66560),
      colour = discord.Color.dark_red(),
      hoist = False,
      mentionable = False,
      reason = 'Hard mute role (remove all roles).'
   )

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