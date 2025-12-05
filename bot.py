import os
import asyncio
import discord
from discord.ext import commands
import telegram

DISCORD_TOKEN = os.getenv("MTQ0NjI1MzM3Mzc0MDQyMTIyMA.GO3Wxp.2mrW_IGJTyi69NQb63y8bJ366lEikDDDaSszvM")
TELEGRAM_TOKEN = os.getenv("8287650101:AAFv6cl1fABMAgBkZp5Iedj5at0bwyV0M14")
TELEGRAM_CHAT_ID = os.getenv("-1003382011732")
DISCORD_CHANNEL_ID = int(os.getenv("1443355104018301080"))

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
telegram_bot = telegram.Bot(token=TELEGRAM_TOKEN)

@bot.event
async def on_ready():
    print(f"Discord bot logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.channel.id == DISCORD_CHANNEL_ID and not message.author.bot:
        try:
            asyncio.create_task(
                telegram_bot.send_message(
                    chat_id=TELEGRAM_CHAT_ID,
                    text=f"📢 *Новое сообщение в Discord:*\n\n{message.content}",
                    parse_mode="Markdown"
                )
            )
        except Exception as e:
            print("Ошибка при отправке:", e)

    await bot.process_commands(message)

bot.run(DISCORD_TOKEN)
