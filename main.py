import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
import os
from datetime import datetime
import random
import asyncio
from unidecode import unidecode


load_dotenv()
DISCORD_API_KEY = os.getenv("DISCORD_API_KEY")


# Rodando o BOT
class BotDiscord(discord.Client):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(
            command_prefix = "+",
            intents = intents
        )
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

    async def on_ready(self):
        print(f"{self.user} Online! 😁 ")

bot = BotDiscord()


# Interações
@bot.tree.command(name="olá", description="Que Tal Interagir Com o Nosso Bot?")
async def ola(interaction:discord.Interaction):
    await interaction.response.send_message(f"Olá {interaction.user.mention} Eu Sou MatMind, Com Oque Posso Ajudar? 🤔")



@bot.tree.command(name="horario", description="Veja As Horas")
async def hora(interaction:discord.Interaction):
    agora = datetime.now()
    horas = agora.strftime("%H:%M")
    await interaction.response.send_message(f"Aqui Está {interaction.user.mention} : {horas} 🕓")



@bot.tree.command(name="piada", description="Que Tal Alegrar Seu Dia Com Uma Piada?")
async def piada(interaction:discord.Interaction):
    piadas = [
    "O que o zero disse para o oito? \n -Que cinto maneiro! 🎩🤣",
    "Por que o livro de matemática ficou confuso? \n -Porque ele tinha muitos problemas. 📖🤣",
    "Por que o computador foi ao médico? \n -Porque estava com um vírus! 👾🤣",
    "Como o tomate ficou vermelho? \n -Porque viu o molho! 🍅🤣",
    "O que o pato falou para a pata? \n -Vem quác! 🦆🤣",
    "Por que o esqueleto não brigou? \n -Porque ele não tinha estômago para isso! ☠️🤣",
    "Por que a bicicleta não consegue ficar de pé sozinha? \n -Porque ela é duas-rodas! 🚴🤣",
    "O que o feijão falou para o outro? \n -Nos vemos na panela! 🥘🤣",
    "Por que o relógio estava feliz? \n -Porque ele estava no seu momento certo! ⏰🤣",
    "Como o oceanógrafo se despede? \n -Maré vê! 🌊🤣",
    "O que um elevador disse para o outro? \n -Subindo na vida! 🏢🤣",
    "Por que o lápis não pode se casar? \n -Porque ele já está comprometido! ✏️🤣",
    "O que o milho falou para a pipoca? \n -Deixa de ser estourado! 🍿🤣"
]
    piada_aleatoria = random.choice(piadas)
    await interaction.response.send_message(f" Opa {interaction.user.mention} Aqui Está: \n {piada_aleatoria} \n \n Oque Você Achou?")



@bot.tree.command(name="sobre", description="Conheça Um Pouco Sobre Nosso Bot")
async def piada(interaction:discord.Interaction):
    await interaction.response.send_message(f"Eu sou um bot criado para ajudar você {interaction.user.mention} com informações rápidas e divertidas. Se tiver alguma dúvida ou pedido, é só falar!")



@bot.tree.command(name="incentivar", description="Se Anime Com Um Incentivo Motivador")
async def piada(interaction:discord.Interaction):
    motivacoes = [
    "O sucesso é a soma de pequenos esforços repetidos diariamente. 🚀",
    "Acredite em você! Sua única limitação é aquela que você impõe a si mesmo. 💪",
    "Grandes coisas nunca vêm da zona de conforto. Desafie-se! 🔥",
    "Cada dia é uma nova chance para ser melhor do que ontem. 🌟",
    "Não espere por oportunidades. Crie-as! 🎯",
    "O impossível é apenas uma opinião. Vá além! 💫",
    "O segredo do sucesso é a persistência. Continue! 🏆",
    "Seja a mudança que você quer ver no mundo. 🌍",
    "Nenhum obstáculo é grande demais quando sua vontade de vencer é maior. 🏋️",
    "A jornada pode ser difícil, mas a vista no topo vale a pena. ⛰️",
    "A persistência realiza o impossível. 💪🔥",
    "O sucesso começa com a decisão de tentar. 🚀",
    "Não importa a velocidade, siga sempre em frente. 🏃‍♂️"
    ]
    motivacao_aleatoria = random.choice(motivacoes)
    await interaction.response.send_message(f"{interaction.user.mention} Aqui Vai: \n {motivacao_aleatoria} \n \n Se Animou Com Este Incentivo?")



@bot.tree.command(name="batalha", description="Desafie-se com perguntas e respostas, se vencer, o bot vai desafiar ainda mais!")
async def batalha(interaction: discord.Interaction):
    await interaction.response.send_message(f"Como Ousa Declarar Uma Batalha Contra Mim {interaction.user.mention}?! Prepare-se! Vamos lá!\n")

    perguntas = [
        {
            "pergunta": "Qual é a capital da França?",
            "resposta": "Paris",
            "dificuldade": "fácil"
        },
        {
            "pergunta": "Quem pintou a Mona Lisa?",
            "resposta": "Leonardo da Vinci",
            "dificuldade": "média"
        },
        {
            "pergunta": "Qual é o nome do elemento químico com símbolo 'Hg'?",
            "resposta": "Mercúrio",
            "dificuldade": "difícil"
        },
        {
            "pergunta": "Em que ano o homem pisou na lua pela primeira vez?",
            "resposta": "1969",
            "dificuldade": "média"
        },
        {
            "pergunta": "Qual é o maior planeta do nosso sistema solar?",
            "resposta": "Júpiter",
            "dificuldade": "difícil"
        },
        {
            "pergunta": "Quem escreveu 'Dom Quixote'?",
            "resposta": "Miguel de Cervantes",
            "dificuldade": "média"
        },
        {
            "pergunta": "Qual é o maior oceano do planeta?",
            "resposta": "Oceano Pacífico",
            "dificuldade": "fácil"
        },
        {
            "pergunta": "Quantos continentes existem na Terra?",
            "resposta": "7",
            "dificuldade": "fácil"
        },
        {
            "pergunta": "Qual é o nome da maior cadeia de montanhas do mundo?",
            "resposta": "Himalaia",
            "dificuldade": "difícil"
        },
        {
            "pergunta": "Qual é a fórmula química da água?",
            "resposta": "H2O",
            "dificuldade": "fácil"
        }
    ]

    random.shuffle(perguntas)

    for pergunta in perguntas:
        # Bot simulando digitação
        async with interaction.channel.typing():
            await asyncio.sleep(1)  # Tempo que o bot vai "digitar" antes de mandar a resposta

        # Enviar a pergunta
        await interaction.followup.send(f"**Pergunta:** {pergunta['pergunta']}")

        def check(msg):
            return msg.author == interaction.user and isinstance(msg.channel, discord.TextChannel)

        try:
            resposta_usuario = await bot.wait_for('message', check=check, timeout=30.0)

            # Remover acentos e comparar respostas
            resposta_usuario_normalizada = unidecode(resposta_usuario.content.strip().lower())
            resposta_correta_normalizada = unidecode(pergunta['resposta'].lower())

            # Bot simulando digitação após o usuário responder
            async with interaction.channel.typing():
                await asyncio.sleep(1)  # Tempo que o bot "digita" enquanto verifica a resposta

            if resposta_usuario_normalizada == resposta_correta_normalizada:
                await interaction.followup.send("Ok, você me derrotou dessa vez! Mas prometo que da próxima vai ser mais difícil. 😭")
            else:
                await interaction.followup.send(f"Ops, você errou! A resposta correta era: {pergunta['resposta']}. Eu venci! Fim da batalha! 😎")
                break

            # Perguntar se o usuário quer continuar
            await interaction.followup.send("Quer ir mais uma? (Responda 'sim' ou 'não') 🤔")

            def continuar_check(msg):
                return msg.author == interaction.user and isinstance(msg.channel, discord.TextChannel)

            continuar_resposta = await bot.wait_for('message', check=continuar_check, timeout=30.0)

            if continuar_resposta.content.strip().lower() != "sim":
                await interaction.followup.send("Obrigado por jogar! Até a próxima! 😊")
                break

        except asyncio.TimeoutError:
            await interaction.followup.send("Você demorou demais para responder. A batalha terminou! 😒")
            break


# Rodar o Bot
bot.run(DISCORD_API_KEY)