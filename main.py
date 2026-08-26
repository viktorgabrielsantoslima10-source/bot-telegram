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

# 1 - AMISTOSO - VERMELHO - SEM LINK
@bot.tree.command(name="amistoso", description="Chamar time")
async def amistoso(interaction: discord.Interaction):
    await interaction.response.defer()
    embed = discord.Embed(
        title="🔴⚫⚪ AMISTOSO AGORA ??? ⚪⚫🔴",
        description="""
━━━━━━━━━━━━━━━━━━━━━
🔥🔥🔥 **ATENÇÃO TIME TCS!** 🔥🔥🔥
━━━━━━━━━━━━━━━━━━━━━

⚽ **ALGUÉM QUER JOGAR AMISTOSO AGORA ???** ⚽

🏴 **Amis agora??!** 🏴
        """,
        color=0xFF0000
    )
    embed.add_field(name="📋 SITUAÇÃO ATUAL DO TIME", value=">>> ```\n✅ LINE: 100% OK E PRONTA\n🧤 GK: 100% OK E PRONTO\n⏰ HORÁRIO: AGORA MESMO\n📶 PING: VERDE / BOM\n🎙️ CALL: TODO MUNDO ON\n```", inline=False)
    embed.add_field(name="👇 FAÇA ISSO AGORA", value="> 1️⃣ **ENTRA NA CALL IMEDIATAMENTE**\n> 2️⃣ **CONFIRMA PRESENÇA**\n> 3️⃣ **BORA AMASSAR!**", inline=False)
    embed.set_footer(text="🔴⚫ TCS - AMISTOSO - SEM DESCULPA! ⚫🔴")
    await interaction.followup.send(content="# @everyone @here\n## 🔴⚫⚪ AMISTOSO AGORA ??? ⚪⚫🔴", embed=embed)

# 2 - AMISTOSOHOST - PRETO - COM NICK E LINK
@bot.tree.command(name="amistosohost", description="Host gigante")
async def amistosohost(interaction: discord.Interaction):
    await interaction.response.defer()
    embed = discord.Embed(
        title="⚫🔴 AMISTOSO NA NOSSA CASA - TCS! 🔴⚫",
        description="""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🏠🔥 **AMISTOSO NA NOSSA CASA!** 🔥🏠
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🏴 **AMISTOSO EM!** 🏴
👑 **O TIME MAIS BRABO!** 👑
        """,
        color=0x000000
    )
    embed.add_field(name="👤 NICK DO HOST OFICIAL", value="```\n🌟 Creigh_Tps1 🌟\n```", inline=False)
    embed.add_field(name="🔗 LINK DO SERVER OFICIAL", value=">>> `https://www.roblox.com/share?code=1e38b417aac9264cb206a7e46b5d657d&type=Server`\n\n[🔴 CLIQUE AQUI PARA ENTRAR 🔴](https://www.roblox.com/share?code=1e38b417aac9264cb206a7e46b5d657d&type=Server)", inline=False)
    embed.add_field(name="📋 INFO DA PARTIDA", value=">>> ```\n✅ LINE: COMPLETA\n🧤 GK: PRONTO\n🗺️ MAPA: PADRÃO\n⚙️ MODO: 11x11\n🎙️ CALL: ON\n```", inline=False)
    embed.set_footer(text="⚫ TCS HOST OFICIAL | Host: Creigh_Tps1 ⚫")
    await interaction.followup.send(content="# @everyone @here\n## ⚫🏠 AMISTOSO NA NOSSA CASA TCS! 🏠⚫", embed=embed)

# 3 - PENEIRA - BRANCO
@bot.tree.command(name="peneira", description="Peneira gigante")
async def peneira(interaction: discord.Interaction):
    await interaction.response.defer()
    embed = discord.Embed(
        title="⚪🔴⚫ PENEIRA ABERTA TCS - SUA CHANCE! ⚫🔴⚪",
        description="""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🌟🏆 **PENEIRA OFICIAL TCS E-SPORTS ABERTA!** 🏆🌟
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔥 **QUER FAZER PARTE DO TCS?** 🔥
👑 **SUA OPORTUNIDADE!** 👑
        """,
        color=0xFFFFFF
    )
    embed.add_field(name="👤 NICK", value="```\n👑 Creigh_Tps1 👑\n```", inline=False)
    embed.add_field(name="🔗 LINK DA PENEIRA", value=">>> `https://www.roblox.com/share?code=1e38b417aac9264cb206a7e46b5d657d&type=Server`\n\n[⚪ CLIQUE AQUI ⚪](https://www.roblox.com/share?code=1e38b417aac9264cb206a7e46b5d657d&type=Server)", inline=False)
    embed.add_field(name="📋 REQUISITOS", value=">>> ```\n🗣️ CALL: OBRIGATÓRIA\n🎧 MIC: OBRIGATÓRIO\n⚽ POSIÇÕES: TODAS\n🏆 NÍVEL: INTER+\n```", inline=False)
    embed.set_footer(text="⚪ TCS PENEIRA OFICIAL ⚪")
    await interaction.followup.send(content="# @everyone @here\n## 🌟⚪ PENEIRA ABERTA TCS! ⚪🌟", embed=embed)

# 4 - TREINO - VERMELHO
@bot.tree.command(name="treino", description="Treino gigante")
async def treino(interaction: discord.Interaction):
    await interaction.response.defer()
    embed = discord.Embed(
        title="🔴💪 TREINO OBRIGATÓRIO TCS! 💪🔴",
        description="""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💪⚽ **ATENÇÃO TIME TCS!** ⚽💪
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔥🔥🔥 **TREINO OBRIGATÓRIO AGORA!** 🔥🔥🔥
        """,
        color=0xFF0000
    )
    embed.add_field(name="👤 NICK", value="```\n🔴 Creigh_Tps1 🔴\n```", inline=False)
    embed.add_field(name="🔗 LINK DO TREINO", value=">>> `https://www.roblox.com/share?code=1e38b417aac9264cb206a7e46b5d657d&type=Server`\n\n[🔴 CLIQUE AQUI 🔴](https://www.roblox.com/share?code=1e38b417aac9264cb206a7e46b5d657d&type=Server)", inline=False)
    embed.add_field(name="📋 INFO", value=">>> ```\n✅ LINE: TODOS\n🧤 GK: TODOS\n🎙️ CALL: OBRIGATÓRIA\n📝 PRESENÇA: COBRADA\n```", inline=False)
    embed.set_footer(text="🔴 TCS TREINO OFICIAL 🔴")
    await interaction.followup.send(content="# @everyone @here\n## 🔴💪 TREINO TCS AGORA! 💪🔴", embed=embed)

bot.run(os.getenv("DISCORD_TOKEN"))
