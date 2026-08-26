import discord
import os
from discord.ext import commands
import datetime

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

@bot.event
async def on_ready():
    await bot.tree.sync()
    await bot.change_presence(activity=discord.Game(name="🔥 ROBLOX | Creigh_Tps1 24HRS"), status=discord.Status.online)
    print(f"🔥 {bot.user} ONLINE!")

# 1 - AMISTOSO SEM NICK/LINK (só perguntando)
@bot.tree.command(name="amistoso", description="⚽ Marcar amistoso simples")
async def amistoso(interaction: discord.Interaction, adversario: str, data: str, horario: str):
    embed = discord.Embed(
        title="━━━━━ ⚽🔥 AMISTOSO OFICIAL 🔥⚽ ━━━━━",
        description=f"🏆 **CONFRONTO CONFIRMADO** 🏆\n\n⚫ **VS:** {adversario.upper()}\n📅 **DATA:** {data}\n⏰ **HORA:** {horario}\n\n⚠️ TODOS UNIFORMIZADOS!",
        color=0xFF0000, timestamp=datetime.datetime.now()
    )
    embed.set_footer(text=f"Marcado por {interaction.user.display_name}", icon_url=interaction.user.display_avatar.url)
    view = discord.ui.View()
    view.add_item(discord.ui.Button(label="✅ VOU JOGAR", style=discord.ButtonStyle.success, emoji="⚽"))
    view.add_item(discord.ui.Button(label="❌ NÃO VOU", style=discord.ButtonStyle.danger, emoji="😭"))
    await interaction.response.send_message(content="@everyone 📢 **AMISTOSO MARCADO!**", embed=embed, view=view)

# 2 - AMISTOSO HOST COM NICK E LINK
@bot.tree.command(name="amistosohost", description="👑 Amistoso host Creigh_Tps1 com link")
async def amistosohost(interaction: discord.Interaction, adversario: str, data: str, horario: str):
    embed = discord.Embed(
        title="━━━━━ 👑🔥 AMISTOSO HOST CREIGH_TPS1 🔥👑 ━━━━━",
        description=f"🏆 **CONFRONTO CONFIRMADO** 🏆\n\n🔴 **TIME:** SPFC da Creigh_Tps1\n⚫ **VS:** {adversario.upper()}\n📅 **DATA:** {data}\n⏰ **HORA:** {horario}\n\n👑 **HOST:** Creigh_Tps1\n🔗 **LINK SERVER:** [CLIQUE AQUI](https://www.roblox.com/share?code=1e38b417aac9264cb206a7e46b5d657d&type=Server)\n🎮 **NICK:** Creigh_Tps1",
        color=0xFF0000, timestamp=datetime.datetime.now()
    )
    embed.set_footer(text=f"Host: Creigh_Tps1 | Por {interaction.user.display_name}", icon_url=interaction.user.display_avatar.url)
    view = discord.ui.View()
    view.add_item(discord.ui.Button(label="✅ VOU JOGAR", style=discord.ButtonStyle.success, emoji="⚽"))
    view.add_item(discord.ui.Button(label="🔗 ENTRAR NO SERVER", style=discord.ButtonStyle.link, url="https://www.roblox.com/share?code=1e38b417aac9264cb206a7e46b5d657d&type=Server", emoji="🚀"))
    await interaction.response.send_message(content="@everyone 👑 **AMISTOSO HOST DA Creigh_Tps1!**", embed=embed, view=view)

# 3 - TREINO COM NICK E LINK
@bot.tree.command(name="treino", description="💪 Treino Creigh_Tps1 com link")
async def treino(interaction: discord.Interaction, dia: str, horario: str):
    embed = discord.Embed(
        title="━━━━━ 💪🔥 TREINÃO CREIGH_TPS1 🔥💪 ━━━━━",
        description=f"🏋️ **PREPARAÇÃO TOTAL**\n\n📅 **DIA:** {dia}\n⏰ **HORA:** {horario}\n👑 **HOST:** Creigh_Tps1\n🔗 **LINK:** [SERVER DA Creigh_Tps1](https://www.roblox.com/share?code=1e38b417aac9264cb206a7e46b5d657d&type=Server)\n🎮 **NICK:** Creigh_Tps1",
        color=0x00FF00
    )
    await interaction.response.send_message(content="@everyone ⚠️ **TREINO DA Creigh_Tps1!**", embed=embed)

# 4 - PENEIRA COM NICK E LINK
@bot.tree.command(name="peneira", description="🔥 Peneira Creigh_Tps1 com link")
async def peneira(interaction: discord.Interaction, data: str, horario: str):
    embed = discord.Embed(
        title="━━━━━ 🔥💜 PENEIRA CREIGH_TPS1 💜🔥 ━━━━━",
        description=f"💎 **CHANCE DE SER PRO**\n\n📅 **DATA:** {data}\n⏰ **HORA:** {horario}\n👑 **DONO:** Creigh_Tps1\n🔗 **LINK:** [ENTRAR NA PENEIRA](https://www.roblox.com/share?code=1e38b417aac9264cb206a7e46b5d657d&type=Server)\n🎮 **NICK:** Creigh_Tps1",
        color=0x9B59B6
    )
    await interaction.response.send_message(content="@everyone 🔥 **PENEIRA DA Creigh_Tps1!**", embed=embed)

bot.run(os.getenv("DISCORD_TOKEN"))
