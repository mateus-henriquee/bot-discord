import openai
from dotenv import load_dotenv
import os

load_dotenv()
DISCORD_API_KEY = os.getenv("DISCORD_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

async def buscar_historico(canal,limit=2):
    message_list = []
    async for message in canal.history(limit=limit,oldest_first=True):
        message_list.append(
            {
                "role":"user" if message.author.id!=bot.user.id else "system",
                "content":message.content
            }
        )
    return message_list

def ask_gpt(mensagens):
    response = openai.ChatCompletion.create(
        messages=mensagens,
        model= "gpt-3.5-turbo-16k",
        temperature= 0.9,
        max_tokens= "300"
    )

    return response.choices[0].message.content
    

# IA
@bot.event
async def on_message(message):
    if message.author.bot:
        return
    
    async with message.channel.typing():
        mensagens = await buscar_historico(message.channel)
        resposta = ask_gpt(mensagens)

        await message.reply(resposta)
    await bot.process_commands(message)