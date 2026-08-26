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
🔥🔥🔥 **ATENÇÃO TIME TPS!** 🔥🔥🔥
━━━━━━━━━━━━━━━━━━━━━

⚽ **ALGUÉM QUER JOGAR AMISTOSO AGORA ???** ⚽

🏴 **ESTAMOS PROCURANDO JOGO!** 🏴

━━━━━━━━━━━━━━━━━━━━━
        """,
        color=0xFF0000  # VERMELHO
    )
    embed.add_field(name="📋 SITUAÇÃO ATUAL DO TIME", value=">>> ```\n✅ LINE: 100% OK E PRONTA\n🧤 GK: 100% OK E PRONTO\n⏰ HORÁRIO: AGORA MESMO\n📶 PING: VERDE / BOM\n🎙️ CALL: TODO MUNDO ON\n```", inline=False)
    embed.add_field(name="🚨 O QUE PRECISAMOS", value=">>> 🔥 **JOGADORES ATIVOS**\n🔥 **FOCO TOTAL**\n🔥 **VONTADE DE GANHAR**\n🔥 **COMUNICAÇÃO NA CALL**", inline=False)
    embed.add_field(name="👇 FAÇA ISSO AGORA", value="> 1️⃣ **ENTRA NA CALL IMEDIATAMENTE**\n> 2️⃣ **CONFIRMA PRESENÇA NO CHAT**\n> 3️⃣ **AVISA QUE TÁ PRONTO**\n> 4️⃣ **BORA AMASSAR!**", inline=False)
    embed.add_field(name="━━━━━━━━━━━━━━━━━━━━━", value="⚫⚪🔴 **TPS E-SPORTS - O MAIS TEMIDO** 🔴⚪⚫", inline=False)
    embed.set_footer(text="🔴⚫ TPS - AMISTOSO - SEM DESCULPA, SÓ JOGO! ⚫🔴")
    await interaction.followup.send(content="# @everyone @here\n## 🔴⚫⚪ AMISTOSO AGORA ??? ⚪⚫🔴", embed=embed)

# 2 - AMISTOSOHOST - PRETO - COM NICK E LINK
@bot.tree.command(name="amistosohost", description="Host gigante")
async def amistosohost(interaction: discord.Interaction):
    await interaction.response.defer()
    embed = discord.Embed(
        title="⚫🔴 AMISTOSO NA NOSSA CASA - VENHA PERDER! 🔴⚫",
        description="""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🏠🔥 **AMISTOSO NA NOSSA CASA!** 🔥🏠
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🏴 **QUER JOGAR CONTRA O TPS? ENTÃO VEM!** 🏴
👑 **O TIME MAIS BRABO DO ROBLOX!** 👑

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        """,
        color=0x000000  # PRETO
    )
    embed.add_field(name="👤 NICK DO HOST OFICIAL", value="```\n🌟 Creigh_Tps1 🌟\n```", inline=False)
    embed.add_field(name="🔗 LINK DO SERVER OFICIAL", value=">>> **COPIA E COLA ESSE LINK:**\n`https://www.roblox.com/share?code=1e38b417aac9264cb206a7e46b5d657d&type=Server`\n\n[🔴 CLIQUE AQUI PARA ENTRAR DIRETO 🔴](https://www.roblox.com/share?code=1e38b417aac9264cb206a7e46b5d657d&type=Server)", inline=False)
    embed.add_field(name="📋 INFORMAÇÕES COMPLETAS DA PARTIDA", value=">>> ```\n✅ LINE: COMPLETA E PRONTA\n🧤 GK: TITULAR E PRONTO\n🗺️ MAPA: PADRÃO COMPETITIVO\n⚙️ MODO: 11x11 OFICIAL\n🎙️ CALL: OBRIGATÓRIA NA HORA\n🏆 ESTILO: SÉRIO E COMPETITIVO\n```", inline=False)
    embed.add_field(name="⚠️ REGRAS DO NOSSO HOST", value="> 🚫 **SEM TOXICIDADE**\n> 🚫 **SEM XINGAMENTO**\n> ✅ **RESPEITO SEMPRE**\n> ✅ **JOGO LIMPO**\n> 🔥 **VENHA PARA JOGAR SÉRIO!**", inline=False)
    embed.add_field(name="━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", value="🔴⚫⚪ **TPS E-SPORTS - O TIME DA MASSA** ⚪⚫🔴", inline=False)
    embed.set_footer(text="⚫ TPS HOST OFICIAL | Host: Creigh_Tps1 | VERMELHO PRETO BRANCO ⚫")
    await interaction.followup.send(content="# @everyone @here\n## ⚫🏠 AMISTOSO NA NOSSA CASA! ENTRE AGORA! 🏠⚫", embed=embed)

# 3 - PENEIRA - BRANCO
@bot.tree.command(name="peneira", description="Peneira gigante")
async def peneira(interaction: discord.Interaction):
    await interaction.response.defer()
    embed = discord.Embed(
        title="⚪🔴⚫ PENEIRA ABERTA TPS - SUA CHANCE! ⚫🔴⚪",
        description="""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🌟🏆 **PENEIRA OFICIAL TPS E-SPORTS ABERTA!** 🏆🌟
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔥 **JÁ SONHOU EM JOGAR NO TPS?** 🔥
👑 **AGORA É SUA OPORTUNIDADE DE BRILHAR!** 👑
⚽ **ESTAMOS RECRUTANDO OS MELHORES!** ⚽

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        """,
        color=0xFFFFFF  # BRANCO
    )
    embed.add_field(name="👤 NICK DO HOST DA PENEIRA", value="```\n👑 Creigh_Tps1 - DONO DO TPS 👑\n```", inline=False)
    embed.add_field(name="🔗 LINK OFICIAL DA PENEIRA", value=">>> **ENTRA NESSE LINK AGORA:**\n`https://www.roblox.com/share?code=1e38b417aac9264cb206a7e46b5d657d&type=Server`\n\n[⚪ CLIQUE AQUI PARA TENTAR A SORTE ⚪](https://www.roblox.com/share?code=1e38b417aac9264cb206a7e46b5d657d&type=Server)", inline=False)
    embed.add_field(name="📋 REQUISITOS OBRIGATÓRIOS", value=">>> ```\n🗣️ CALL: 100% OBRIGATÓRIA\n🎧 MIC: 100% OBRIGATÓRIO\n⚽ POSIÇÕES: TODAS DISPONÍVEIS\n🏆 NÍVEL: INTERMEDIÁRIO PRA CIMA\n🤝 RESPEITO: ESSENCIAL\n⏰ HORÁRIO: DISPONÍVEL\n```", inline=False)
    embed.add_field(name="🎯 O QUE VAMOS AVALIAR EM VOCÊ", value="> ⚡ **PASSE:** PRECISÃO\n> 🎯 **FINALIZAÇÃO:** QUALIDADE\n> 🧠 **VISÃO DE JOGO:** INTELIGÊNCIA\n> 🗣️ **COMUNICAÇÃO:** FALAR NA CALL\n> 🤝 **TRABALHO EM EQUIPE:** COLETIVO\n> 🔥 **VONTADE:** GARRA!", inline=False)
    embed.add_field(name="━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", value="🔴⚫⚪ **TPS E-SPORTS - VENHA FAZER HISTÓRIA CONOSCO!** ⚪⚫🔴", inline=False)
    embed.set_footer(text="⚪ TPS PENEIRA OFICIAL | NÃO PERCA ESSA CHANCE ÚNICA! ⚪")
    await interaction.followup.send(content="# @everyone @here\n## 🌟⚪ PENEIRA ABERTA - TPS TE ESPERA! ⚪🌟", embed=embed)

# 4 - TREINO - VERMELHO
@bot.tree.command(name="treino", description="Treino gigante")
async def treino(interaction: discord.Interaction):
    await interaction.response.defer()
    embed = discord.Embed(
        title="🔴💪 TREINO OBRIGATÓRIO TPS - COMPAREÇA AGORA! 💪🔴",
        description="""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💪⚽ **ATENÇÃO TOTAL TIME TPS!** ⚽💪
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔥🔥🔥 **TREINO OBRIGATÓRIO AGORA MESMO!** 🔥🔥🔥
🚨 **PRESENÇA DE TODOS É OBRIGATÓRIA!** 🚨
🏆 **RUMO AO TOPO, SEM DESCULPAS!** 🏆

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        """,
        color=0xFF0000  # VERMELHO
    )
    embed.add_field(name="👤 NICK DO TREINO", value="```\n🔴 Creigh_Tps1 - CAPITÃO 🔴\n```", inline=False)
    embed.add_field(name="🔗 LINK DO TREINO", value=">>> **ENTRA AGORA NO TREINO:**\n`https://www.roblox.com/share?code=1e38b417aac9264cb206a7e46b5d657d&type=Server`\n\n[🔴 CLIQUE AQUI PARA ENTRAR NO TREINO 🔴](https://www.roblox.com/share?code=1e38b417aac9264cb206a7e46b5d657d&type=Server)", inline=False)
    embed.add_field(name="📋 INFORMAÇÕES DO TREINO DE HOJE", value=">>> ```\n✅ LINE: TODOS OBRIGATÓRIOS\n🧤 GK: TODOS OBRIGATÓRIOS\n🎙️ CALL: 100% OBRIGATÓRIA\n📝 PRESENÇA: SERÁ COBRADA\n⏰ HORÁRIO: AGORA MESMO\n💪 FOCO: TOTAL E ABSOLUTO\n```", inline=False)
    embed.add_field(name="⚠️ AVISO MUITO IMPORTANTE", value="> 🚨 **QUEM NÃO COMPARECER SEM AVISAR VAI LEVAR PUNIÇÃO!**\n> 🚨 **TREINO É COISA SÉRIA!**\n> ✅ **SE NÃO PUDER IR, AVISE ANTES NO CHAT!**\n> 🔥 **VAMOS COM TUDO TIME!**", inline=False)
    embed.add_field(name="━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", value="🔴⚫⚪ **TPS E-SPORTS - TREINO DE CAMPEÃO!** ⚪⚫🔴", inline=False)
    embed.set_footer(text="🔴 TPS TREINO OFICIAL | FOCO, FORÇA E FÉ! SEMPRE! 🔴")
    await interaction.followup.send(content="# @everyone @here\n## 🔴💪 TREINO OBRIGATÓRIO AGORA! ENTRA AE! 💪🔴", embed=embed)

bot.run(os.getenv("DISCORD_TOKEN"))
