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
    await bot.change_presence(
        activity=discord.Game(name="🔥 ROBLOX | Creigh_Tps1 ONLINE 24HRS 🔥"),
        status=discord.Status.online
    )
    print(f"🔥 {bot.user} ONLINE!")

# ===== /AMISTOSO =====
@bot.tree.command(name="amistoso", description="⚽💥 MARCAR AMISTOSO BRABO")
async def amistoso(interaction: discord.Interaction, adversario: str, data: str, horario: str):
    embed = discord.Embed(
        title="━━━━━━━━━ ⚽🔥💥 AMISTOSO OFICIAL 💥🔥⚽ ━━━━━━━━━",
        description=f"""
```diff
+ 🏆🏆🏆 CONFRONTO CONFIRMADO 🏆🏆🏆
