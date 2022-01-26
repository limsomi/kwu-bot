import discord
import json
from discord.ext import commands
from discord.commands.context import ApplicationContext
from discord.commands import Option
from discord.file import File
import os

from restaurant import 추천,찾기
from random import *

# 데이터 베이스 참조하기
def 식당_정보_가져오기():
    with open('data/restaurant.json', encoding='utf-8') as fp:
        식당_정보 = json.load(fp)
    return 식당_정보

식당정보=식당_정보_가져오기()

async def 랜덤추천(ctx : ApplicationContext):
        value=choice(choice(list(식당정보.values())))
        await ctx.send("이 식당을 추천드립니다\n\n")
        for i in value:
            await ctx.send(f"{i}:{value[i]}")
        return


@commands.slash_command(
    name = "식당추천",
    description= "식당에 대한 정보를 알려줍니다!",
    guild_ids = [935129838556180500]
)
async def 식당추천(
    ctx ,
    선택: Option(str,
                    "Choose what you want", 
                    choices=["분식", "일식", "중식","한식"], 
                    required=True)
):
    print(f"{ctx=}")
    print(f"{선택=}")
    
    if 선택 == "분식":
        string = ""       
        for rt in 식당정보["분식"]:
            string+="이름 : "
            string += rt["이름"]
            string += "\n"
            string+="운영시간 : "
            string += rt["운영시간"]
            string += "\n"
            string+="추천메뉴 : "
            string += rt["추천메뉴"]
            string += "\n"
            string += "\n"

        string += "\n이런 식당들이 있어요!"
        await ctx.send(f"{string}")
    

    elif 선택 =="일식":
        string = ""
        for rt in 식당정보["일식"]:
            string+="이름 : "
            string += rt["이름"]
            string += "\n"
            string+="운영시간 : "
            string += rt["운영시간"]
            string += "\n"
            string+="추천메뉴 : "
            string += rt["추천메뉴"]
            string += "\n"
            string += "\n"

        string += "\n이런 식당들이 있어요!"
        await ctx.send(f"{string}")


    elif 선택 == "중식":
        string = ""
        for rt in 식당정보["중식"]:
            string+="이름 : "
            string += rt["이름"]
            string += "\n"
            string+="운영시간 : "
            string += rt["운영시간"]
            string += "\n"
            string+="추천메뉴 : "
            string += rt["추천메뉴"]
            string += "\n"
            string += "\n" 
        string += "\n이런 식당들이 있어요!"
        await ctx.send(f"{string}")       

    elif 선택=="한식":
        string = ""
        for rt in 식당정보["한식"]:
            string+="이름 : "
            string += rt["이름"]
            string += "\n"
            string+="운영시간 : "
            string += rt["운영시간"]
            string += "\n"
            string+="추천메뉴 : "
            string += rt["추천메뉴"]
            string += "\n"
            string += "\n"

        string += "\n이런 식당들이 있어요!"
        await ctx.send(f"{string}")


    # await ctx.respond("")

@commands.slash_command(
    name="식당찾기",
    description="식당찾기",
    guild_ids = [935129838556180500]
)
async def 식당찾기(
    ctx,
    선택:Option(str,
                    "찾으실 식당의 이름을 입력해주세요",
                    required=True)
    ):
        print(f"{ctx=}")
        print(f"{선택=}")

        await ctx.send("찾으시는 식당의 정보입니다\n\n")
        count=0
        for type in 식당정보:
            if count!=1:
                for rt in 식당정보[type]:
                    if 선택==rt["이름"]:
                        count+=1
                        for value in rt:
                            await ctx.send(f"{value}:{rt[value]}")
                        break
            else:
                break
        if count==0:
            await ctx.send("!찾으시는 식당의 정보가 없습니다")
        return

@commands.slash_command(
    name = "식당랜덤추천",
    description= "식당을 랜덤으로 추천해줄게요!",
    guild_ids = [935129838556180500]
)
async def 식당랜덤추천(
    ctx : ApplicationContext
):
    await 랜덤추천(ctx)


