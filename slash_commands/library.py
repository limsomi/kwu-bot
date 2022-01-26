import discord
import json
from discord.ext import commands
from discord.commands.context import ApplicationContext
from discord.commands import Option
from discord.file import File
import os

# 데이터 베이스 참조하기
def 도서관_정보_가져오기():
    with open('data/library.json', encoding='utf-8') as fp:
        도서관_정보 = json.load(fp)
    return 도서관_정보


# 도서관 사진 가져오기
def get_image_paths():
    file_paths = []
    
    for fn in os.listdir('./img/library'):
        file_paths.append(os.path.join(os.getcwd(), 'img', 'library', fn))
        
    return file_paths

async def images(ctx : ApplicationContext):
    imgs = get_image_paths()
    
    
    files = [File(path) for i, path in enumerate(imgs)]

    await ctx.respond(files=files)


async def facilities(ctx  : ApplicationContext):
    정보 = 도서관_정보_가져오기()
    string = ""    
    for facil in 정보["시설"]:
        string += facil["이름"]
        string += " : "
        string += facil["설명"]
        string += "\n"

    string += "\n이런 시설들이 있어요!"
    await ctx.respond(f"{string}")
    return

async def operating_hours(ctx : ApplicationContext):
    정보 = 도서관_정보_가져오기()
    open = 정보["운영시간"]["open"]
    closed = 정보["운영시간"]["closed"]
    await ctx.respond(f"도서관은 {open}부터 {closed}까지 운영해요!")
    return


@commands.slash_command(
    name = "도서관",
    description= "도서관에 대한 정보를 알려줍니다!",
    guild_ids = [935129838556180500],
)
async def library_command(
    ctx : ApplicationContext,
    선택: Option(str,
                    "Choose what you want", 
                    choices=["시설", "운영시간", "사진"], 
                    required=True)
):
    print(f"{ctx=}")
    print(f"{선택=}")
    
    if 선택 == "시설":
        await facilities(ctx)
        
    if 선택 =="운영시간":
        await operating_hours(ctx)
        
    if 선택 == "사진":
        await images(ctx)
    
    return
    # await ctx.respond("")