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

# 1 - AMISTOSO = CHAMAR SEU TIME (SEM NICK E SEM LINK)
@bot.tree.command(name="amistoso", description="Chamar nosso time pro amistoso")
async def amistoso(interaction: discord.Interaction):
    await interaction.response.defer()
    embed = discord.Embed(
        title="⚽ AMISTOSO AGORA ??? 🏴",
        description="🔥 **BORA TIME ??? ALGUÉM QUER JOGAR AMISTOSO AGORA ???** 🔥\n\n📢 Reage aqui e entra na call!",
        color=0xFF0000
    )
    embed.add_field(name="📋 SITUAÇÃO", value="> ✅ **LINE:** OK\n> 🧤 **GK:** OK\n> ⏰ **HORÁRIO:** AGORA\n> 🎙️ **CALL:** ENTRA AE", inline=False)
    embed.add_field(name="👇 O QUE FAZER", value="> 1️⃣ Entra na call\n> 2️⃣ Confirma presença\n> 3️⃣ Bora procurar jogo!", inline=False)
    embed.set_footer(text="🏆 TPS E-SPORTS | Chamando o time!")
    await interaction.followup.send(content="@everyone @here", embed=embed)

# 2 - AMISTOSOHOST = CHAMAR OUTRO TIME PRO SEU HOST (COM NICK E LINK)
@bot.tree.command(name="amistosohost", description="Chamar time pra nossa casa")
async def amistosohost(interaction: discord.Interaction):
    await interaction.response.defer()
    embed = discord.Embed(
        title="🏠⚽ AMISTOSO NA NOSSA CASA! 🏴🔥",
        description="🔥 **QUER JOGAR CONTRA O TPS? VEM PRA NOSSA CASA!** 🔥",
        color=0x00FF00
    )
    embed.add_field(name="👤 NICK DO HOST", value="`Creigh_Tps1`", inline=False)
    embed.add_field(name="🔗 LINK DO SERVER", value="https://www.roblox.com/share?code=1e38b417aac9264cb206a7e46b5d657d&type=Server", inline=False)
    embed.add_field(name="📋 INFO DA PARTIDA", value="> ✅ **LINE:** COMPLETA\n> 🧤 **GK:** PRONTO\n> 🗺️ **MAPA:** PADRÃO\n> ⚙️ **MODO:** 11x11\n> 🎙️ **CALL:** ON", inline=False)
    embed.set_footer(text="🏆 TPS E-SPORTS | Host: Creigh_Tps1")
    await interaction.followup.send(content="@everyone @here", embed=embed)

# 3 - PENEIRA
@bot.tree.command(name="peneira", description="Peneira aberta")
async def peneira(interaction: discord.Interaction):
    await interaction.response.defer()
    embed = discord.Embed(
        title="🌟🏆 PENEIRA ABERTA - TPS! 🏆🌟",
        description="🔥 **QUER FAZER PARTE DO TPS?** 🔥",
        color=0xFFD700
    )
    embed.add_field(name="👤 NICK", value="`Creigh_Tps1`", inline=True)
    embed.add_field(name="🔗 LINK", value="https://www.roblox.com/share?code=1e38b417aac9264cb206a7e46b5d657d&type=Server", inline=False)
    await interaction.followup.send(content="@everyone @here", embed=embed)

# 4 - TREINO
@bot.tree.command(name="treino", description="Treino do time")
async def treino(interaction: discord.Interaction):
    await interaction.response.defer()
    embed = discord.Embed(
        title="💪⚽ TREINO TPS - BORA TIME! ⚽💪",
        description="🔥 **TREINO AGORA! ENTRA AE TIME!** 🔥",
        color=0x0099FF
    )
    embed.add_field(name="👤 NICK", value="`Creigh_Tps1`", inline=True)
    embed.add_field(name="🔗 LINK", value="https://www.roblox.com/share?code=1e38b417aac9264cb206a7e46b5d657d&type=Server", inline=False)
    await interaction.followup.send(content="@everyone @here", embed=embed)

bot.run(os.getenv("DISCORD_TOKEN"))
