import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logado como {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Sincronizado {len(synced)}")
    except Exception as e:
        print(e)

# /amistoso simples
@bot.tree.command(name="amistoso", description="Chamar amistoso agora")
async def amistoso(interaction: discord.Interaction):
    await interaction.response.defer()
    embed = discord.Embed(
        title="⚽ AMISTOSO AGORA? 🏴",
        description="🔥 **ESTAMOS PROCURANDO JOGO!** 🔥\n\n✅ **LINE:** PRONTA\n🧤 **GK:** PRONTO\n⏰ **HORÁRIO:** AGORA\n\n📢 Entra na call e bora jogar!",
        color=0xFF0000
    )
    embed.set_footer(text="TPS - Time Pro")
    await interaction.followup.send(content="@everyone @here", embed=embed)

# /amistosohost O GRANDÃO QUE VOCÊ QUER
@bot.tree.command(name="amistosohost", description="Amistoso na nossa casa")
async def amistosohost(interaction: discord.Interaction):
    await interaction.response.defer()
    embed = discord.Embed(
        title="🏠 AMISTOSO NA NOSSA CASA! 🏴",
        description="🔥 **VAMOS JOGAR EM CASA!** 🔥",
        color=0x00FF00
    )
    embed.add_field(name="👤 NICK", value="`Creigh_Tps1`", inline=True)
    embed.add_field(name="🔗 LINK", value="[Clique para entrar](https://www.roblox.com/share?code=1e38b417aac9264cb206a7e46b5d657d&type=Server)", inline=True)
    embed.add_field(name="📋 INFO", value="> ✅ **LINE:** OK\n> 🧤 **GK:** OK\n> 🗺️ **MAPA:** Padrão\n> ⚙️ **TIPO:** 11x11", inline=False)
    embed.add_field(name="📢 AVISO", value="> ⏰ Entra rápido!\n> 🎙️ Entra na call!\n> 🚀 Vem pro jogo!", inline=False)
    embed.set_footer(text="TPS E-SPORTS | Host: Creigh_Tps1")
    await interaction.followup.send(content="@everyone @here", embed=embed)

@bot.tree.command(name="ip-amistosohost", description="Amistoso com IP")
async def ip_host(interaction: discord.Interaction, ip: str):
    await interaction.response.defer()
    embed = discord.Embed(title="🌐 AMISTOSO - IP HOST", color=0x0099FF)
    embed.add_field(name="👤 NICK", value="`Creigh_Tps1`", inline=True)
    embed.add_field(name="💻 IP", value=f"`{ip}`", inline=True)
    embed.add_field(name="🔗 LINK", value="[Entrar no Server](https://www.roblox.com/share?code=1e38b417aac9264cb206a7e46b5d657d&type=Server)", inline=False)
    embed.add_field(name="📋 REQUISITOS", value="> ✅ LINE\n> 🧤 GK\n> 🎙️ CALL ON", inline=False)
    await interaction.followup.send(content="@everyone @here", embed=embed)

@bot.tree.command(name="vps-amistosohost", description="Amistoso com VPS")
async def vps_host(interaction: discord.Interaction, vps: str):
    await interaction.response.defer()
    embed = discord.Embed(title="⚡ AMISTOSO - VPS HOST", color=0xFFD700)
    embed.add_field(name="👤 NICK", value="`Creigh_Tps1`", inline=True)
    embed.add_field(name="⚡ VPS", value=f"`{vps}`", inline=True)
    embed.add_field(name="🔗 LINK", value="[Entrar no Server](https://www.roblox.com/share?code=1e38b417aac9264cb206a7e46b5d657d&type=Server)", inline=False)
    await interaction.followup.send(content="@everyone @here", embed=embed)

@bot.tree.command(name="gamemode", description="Definir modo de jogo")
async def gamemode(interaction: discord.Interaction, modo: str):
    await interaction.response.defer()
    embed = discord.Embed(title="🎮 GAMEMODE", description=f"**Modo selecionado:** `{modo}`", color=0x9900FF)
    await interaction.followup.send(embed=embed)

bot.run(os.getenv("DISCORD_TOKEN"))
