# 딱히 secrets.json 이나 main.py 파일의 위치를 바꾸지 않는 이상 건들일 필요는 없습니다.
import json

TOKEN : str = None

with open("secret.json", mode="r", encoding="utf-8") as fp:
    data = json.load(fp)
    TOKEN = data["token"]
    
__all__  = [ TOKEN ]