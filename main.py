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
        print(f"Sincronizado {len(synced)} comandos")
    except Exception as e:
        print(e)

@bot.tree.command(name="amistoso", description="Chamar amistoso agora")
async def amistoso(interaction: discord.Interaction):
    await interaction.response.defer()
    embed = discord.Embed(
        title="AMISTOSO AGORA? 🏴",
        description="TO: ✅ LINE\nTO: 🧤 GK\n\n@everyone @here",
        color=0xff0000
    )
    await interaction.followup.send(content="@everyone @here", embed=embed)

@bot.tree.command(name="amistosohost", description="Amistoso host")
async def amistosohost(interaction: discord.Interaction):
    await interaction.response.defer()
    embed = discord.Embed(title="AMISTOSO AGORA? 🏴", description="TO: ✅ LINE\nTO: 🧤 GK", color=0xff0000)
    await interaction.followup.send(content="@everyone @here", embed=embed)

@bot.tree.command(name="ip-amistosohost", description="IP do host")
async def ip_host(interaction: discord.Interaction, ip: str):
    await interaction.response.defer()
    await interaction.followup.send(f"@everyone @here\n\n**IP HOST:** `{ip}`\nTO: ✅ LINE\nTO: 🧤 GK")

@bot.tree.command(name="vps-amistosohost", description="VPS host")
async def vps_host(interaction: discord.Interaction, vps: str):
    await interaction.response.defer()
    await interaction.followup.send(f"@everyone @here\n\n**VPS:** `{vps}`\nTO: ✅ LINE\nTO: 🧤 GK")

@bot.tree.command(name="gamemode", description="Modo de jogo")
async def gamemode(interaction: discord.Interaction, modo: str):
    await interaction.response.defer()
    await interaction.followup.send(f"**GAMEMODE:** {modo} @everyone")

bot.run(os.getenv("DISCORD_TOKEN"))
