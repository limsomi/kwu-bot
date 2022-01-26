from optparse import Option
from typing import List
import discord
import json
from discord.ext import commands
from random import *

def 식당_정보_가져오기():
    with open('data/restaurant.json', encoding='utf-8') as fp:
        식당_정보 = json.load(fp)
    return 식당_정보

식당정보=식당_정보_가져오기()

@commands.command()
async def 찾기(ctx, user : str=None):#식당 정보 찾을 때 사용


    if user==None:
        await ctx.send("찾고 싶은 식당의 이름을 보내주세요 \n예: !찾기 윤스쿡")
        return

    else:
        #restaurant.json에서 음식 종류가 중복되는 식당이 있기 때문에 적어둠, 예:지지고
        count=0
        for type in 식당정보:
            if count!=1:
                for rt in 식당정보[type]:
                    if user==rt["이름"]:
                        await ctx.send("찾으시는 식당의 정보입니다\n\n")
                        count+=1
                        for value in rt:
                            await ctx.send(f"{value}:{rt[value]}")
                        break
        if count==0:
            await ctx.send("찾으시는 식당의 정보가 없습니다")


@commands.command()
async def 추천(ctx,value : str=None):#식당 추천할 때 사용
    if value==None:
        await ctx.send('''
1. !추천 분식
2. !추천 일식
3. !추천 중식
4. !추천 한식


4가지 중 하나를 보내주세요''')

    elif value=="분식":
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
        return
    
    elif value == "일식":
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
        return

    elif value == "중식":
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
        return
    elif value == "한식":
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
        return
    else:
        await ctx.send("입력하신 음식은 찾을 수 없습니다. 다시 보내주세요")


@commands.command()
async def 식당(ctx, menu : str= None):

    if menu == None:
        await ctx.send(f'''
식당에 대한 정보를 얻고 싶으시군요

1. !식당 추천-식당 종류에 따라 식당 추천받기
2. !식당 랜덤_추천-랜덤으로 식당 추천
3. !식당 찾기-찾는 식당 정보 보기


3가지 중 하나를 보내주세요 예: !식당 추천''')


    elif menu=="추천":
        await 추천(ctx)
        return
      
    elif menu=="랜덤_추천":
        value=choice(choice(list(식당정보.values())))
        await ctx.send("이 식당을 추천드립니다\n\n")
        for i in value:
            await ctx.send(f"{i}:{value[i]}")
        return
        
    elif menu=="찾기":
        await 찾기(ctx)
        return

    else:
        await ctx.send("입력하신 정보는 찾을 수 없습니다. 다시 보내주세요")
        return
