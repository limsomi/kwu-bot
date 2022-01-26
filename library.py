from typing import List
import discord
import json
from discord.ext import commands

def 도서관_정보_가져오기():
    with open('data/library.json', encoding='utf-8') as fp:
        도서관_정보 = json.load(fp)
    return 도서관_정보

@commands.command()
async def 도서관(ctx, menu : str= None):
    """
        menu에는 운영시간, 시설 
    """
    정보 = 도서관_정보_가져오기()
    if menu == None:
        await ctx.send(f"도서관에 대해 알고 싶으면\n!도서관 운영시간, !도서관 시설 라고 보내주세요!")
    
    if menu == "운영시간":
        
        open = 정보["운영시간"]["open"]
        closed = 정보["운영시간"]["closed"]
        await ctx.send(f"도서관은 {open}부터 {closed}까지 운영해요!")
        return
    
    if menu == "시설":
        string = ""
        
        for facil in 정보["시설"]:
            string += facil["이름"]
            string += " : "
            string += facil["설명"]
            string += "\n"

        string += "\n이런 시설들이 있어요!"
        await ctx.send(f"{string}")
