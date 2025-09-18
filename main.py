import discord
import os
import datetime
from dotenv import load_dotenv
from discord.ext import commands
from flask import Flask
from threading import Thread

load_dotenv()

token = os.getenv("DISCORD_BOT_TOKEN")
# intents是要求機器人的權限
intents = discord.Intents.all()
# command_prefix是前綴符號，可以自由選擇($, #, &...)
bot = commands.Bot(command_prefix = "/", intents = intents)
TARGET_DATE = datetime.date(2026, 2, 1)

@bot.event
# 當機器人完成啟動
async def on_ready():
    print(f"目前登入身份 --> {bot.user}")

@bot.command()


async def countdown(ctx):
    today = datetime.date.today()
    delta = (TARGET_DATE - today).days
    await ctx.send(f"距離2026年2月1日還有{delta}天，考試加油:)")


app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

def run():
    app.run(host="0.0.0.0", port=10000)

def keep_alive():
    t = Thread(target=run)
    t.start()

if __name__ == "__main__":
    keep_alive()
    bot.run(token)

