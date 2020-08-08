import discord
from discord.ext import commands
from PingPongTool import PingPong
from random import randint

def RandomColor():
    return randint(0, 0xFFFFFF)

TOKEN = "이곳에 봇 토큰을 넣으세요"
Authorization = "이곳에 인증 토큰을 넣으세요"
URL = "이곳에 커스텀 API 링크를 넣으세요"

bot = commands.Bot(command_prefix=['!', '핑퐁아 '])
Ping = PingPong(URL, Authorization)


@bot.listen()
async def on_command_error(ctx, error):
    if type(error) is commands.errors.CommandNotFound:
        data = await Ping.Pong(ctx.author.id, ctx.message.content, NoTopic=False)
        embed = discord.Embed(
            title="핑퐁",
            description=data['text'],
            color=RandomColor()
        )
        embed.set_footer(text="Using PingPongTool")
        if data['image'] is not None:
            embed.set_image(url=data['image'])
        await ctx.send(embed=embed)


@bot.command(name="따라해")
async def Echo(ctx, *, text: str):
    await ctx.send(text)

bot.run(TOKEN)
