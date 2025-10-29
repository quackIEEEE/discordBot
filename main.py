import discord
import os
import datetime
from dotenv import load_dotenv
from discord.ext import commands
from flask import Flask
from threading import Thread

load_dotenv()

token = os.getenv("DISCORD_BOT_TOKEN")
#要求機器人的權限
intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "/", intents = intents)
TARGET_DATE = datetime.date(2026, 2, 5)

@bot.event
# 當機器人完成啟動
async def on_ready():
    print(f"目前登入身份 --> {bot.user}")

@bot.command()


async def countdown(ctx):
    today = datetime.date.today()
    delta = (TARGET_DATE - today).days
    await ctx.send(f"政大：2/5 \n
                     中興：2/6 \n
                     中央：2/8 \n離考試還剩{delta}天，考試加油:)")


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




