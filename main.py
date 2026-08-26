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

# 1 - AMISTOSO SEM NICK E SEM LINK (SÓ CONVITE)
@bot.tree.command(name="amistoso", description="Procurando amistoso")
async def amistoso(interaction: discord.Interaction):
    await interaction.response.defer()
    embed = discord.Embed(
        title="⚽🔍 AMISTOSO AGORA? 🏴",
        description="🔥 **ESTAMOS PROCURANDO AMISTOSO!** 🔥\n\n📢 **ALGUÉM QUER JOGAR CONTRA NÓS?**",
        color=0xFF0000
    )
    embed.add_field(name="📊 NOSSO TIME", value="> ✅ **LINE:** PRONTA\n> 🧤 **GK:** PRONTO\n> ⏰ **HORÁRIO:** AGORA\n> 📶 **PING:** BOM\n> 🎙️ **CALL:** ON", inline=False)
    embed.add_field(name="📩 COMO MARCAR", value="> 💬 Responde aqui no chat\n> 📩 Chama na DM\n> 🎙️ Entra na call e bora!", inline=False)
    embed.set_footer(text="🏆 TPS E-SPORTS - Estamos ON para jogo!")
    await interaction.followup.send(content="@everyone", embed=embed)

# 2 - AMISTOSO HOST COM NICK E LINK GRANDÃO
@bot.tree.command(name="amistosohost", description="Amistoso na nossa casa")
async def amistosohost(interaction: discord.Interaction):
    await interaction.response.defer()
    embed = discord.Embed(
        title="🏠⚽ AMISTOSO NA NOSSA CASA! 🏴🔥",
        description="🔥 **VENHAM JOGAR AQUI NO NOSSO HOST!** 🔥",
        color=0x00FF00
    )
    embed.add_field(name="👤 NICK DO HOST", value="`Creigh_Tps1`", inline=False)
    embed.add_field(name="🔗 LINK DO SERVER", value="https://www.roblox.com/share?code=1e38b417aac9264cb206a7e46b5d657d&type=Server", inline=False)
    embed.add_field(name="📋 INFORMAÇÕES", value="> ✅ **LINE:** COMPLETA\n> 🧤 **GK:** PRONTO\n> 🗺️ **MAPA:** PADRÃO\n> ⚙️ **MODO:** 11x11\n> 🎙️ **CALL:** OBRIGATÓRIA", inline=False)
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
    embed.add_field(name="📋 REQUISITOS", value="> 🗣️ CALL OBRIGATÓRIA\n> 🎧 MIC OBRIGATÓRIO\n> ⚽ TODAS POSIÇÕES", inline=False)
    await interaction.followup.send(content="@everyone @here", embed=embed)

# 4 - TREINO
@bot.tree.command(name="treino", description="Treino do time")
async def treino(interaction: discord.Interaction):
    await interaction.response.defer()
    embed = discord.Embed(
        title="💪⚽ TREINO TPS - COMPAREÇA! ⚽💪",
        description="🔥 **TREINO OBRIGATÓRIO AGORA!** 🔥",
        color=0x0099FF
    )
    embed.add_field(name="👤 NICK", value="`Creigh_Tps1`", inline=True)
    embed.add_field(name="🔗 LINK", value="https://www.roblox.com/share?code=1e38b417aac9264cb206a7e46b5d657d&type=Server", inline=False)
    embed.add_field(name="📋 INFO", value="> ✅ LINE: TODOS\n> 🧤 GK: TODOS\n> 🎙️ CALL OBRIGATÓRIA", inline=False)
    await interaction.followup.send(content="@everyone @here", embed=embed)

bot.run(os.getenv("DISCORD_TOKEN"))
