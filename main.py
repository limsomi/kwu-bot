# 이 예시는 Discord Development Portals에서 'members' 권한 인텐트를 클릭해야 사용할 수 있습니다!
import random

import discord
import asyncio
from discord.message import Message
from discord.ext import commands
from discord.ui import Button, View
from typing import List

from discord.webhook import async_
from my_secrets import TOKEN

# 코드가 너무 길어지면 스크립트를 따로 만들어서 import 할 수 있습니다.
from library import 도서관
from restaurant import *

from slash_commands.library import library_command
from slash_commands.restaurant import 식당추천,식당찾기,식당랜덤추천

description = """Discord Bot 샘플 봇입니다"""

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", description=description, intents=intents)

bot.add_command(도서관)
bot.add_command(식당)
bot.add_command(찾기)
bot.add_command(추천)

bot.add_application_command(library_command)
bot.add_application_command(식당추천)
bot.add_application_command(식당찾기)
bot.add_application_command(식당랜덤추천)

@bot.event
async def on_ready():
    print(f"로그인 성공! 닉네임: {bot.user} 아이디(ID): {bot.user.id}")
    print("------")    


@bot.event
async def on_message(message : Message):
    # 이 봇이 작성한 메세지는 무시
    if message.author.id == bot.user.id:
        return
    
    # 다른 봇이 보낸 메시지의 경우 무시
    if message.author.bot:
        return
    
    # 여러분이 만든 서버(길드)만 메세지를 받고 싶다면 이 조건문을 이용하세요
    # 봇을 초대한 서버(길드)이름을 알고 싶다면 print(message.guild.name)를 통해서 확인!
    # if not message.guild.name == "Bot Test":
    #     return
    
    # 사용자가 보낸 메세지 객체 - 길드 이름, 유저 이름, 아이디, ... 많은 정보를 가지고 있습니다.
    print(message)
    # 보낸 메세지
    print(message.content)
    
    # 위에 명시한 command_prefix(명령어 접두어)가 포함된 메세지의 경우
    # 명령을 수행하기 위해 이 코드는 on_message 함수 맨 아래에 작성합니다!
    await bot.process_commands(message)


@bot.command(description="안녕!")
async def hello(ctx):
    button = Button(label="Click me!", style=discord.ButtonStyle.green, emoji="😂")
    view = View()
    view.add_item(button)
    await ctx.send("Hi!", view=view)


@bot.command(description="랜덤으로 골라주기 사용법: !랜덤 하나 둘 셋")
async def 랜덤(ctx, *choices: List[str]):
    """
        choices : List[str]
            사용자가 보낸 명령어를 제외한 메세지
            (위 예시의 경우 ["하나", "둘", "셋"])
            으로 받습니다.
    """
    await ctx.send(random.choice(choices))

@bot.command(description="주어진 초 이후에 알람을 보내드립니다!")
async def 알람(ctx, seconds : str = None):
    """
        seconds : int
            주어진 자연수 만큼 대기 이후 @mention을 통해 알림을 보냅니다.
    """
    if seconds is None:
        await ctx.send(f"몇 초 뒤에 알람을 드릴지 알려주세요!\n사용 예시: !알림 5")
    
    try:
        # 사용자가 입력한 메세지는 str(문자열) 타입으로 들어오기 때문에
        # int(정수형)으로 변환 후 작업을 수행한다.
        seconds = int(seconds)

        await asyncio.sleep(seconds)
        await ctx.send(f"{ctx.author.mention}님 {seconds}초가 지났어요!")
    except Exception as e:
        print(e)
        await ctx.send(f"이건 자연수가 아니자나! {seconds} ")

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f"{member.name} joined in {member.joined_at}")



bot.run(TOKEN)


