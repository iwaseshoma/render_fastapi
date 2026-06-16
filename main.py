from typing import Optional

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

import random  # randomライブラリを追加

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉",
        "中吉",
        "小吉",
        "吉",
        "半吉",
        "末吉",
        "末小吉",
        "凶",
        "小凶",
        "大凶"
    ]

    return omikuji_list[random.randrange(10)]


### コードいろいろ... ###

@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
            <table border="1">
            <tr>
            <th>履修授業</th>
            <th>授業日</th>
            </tr>
            
            <tr>
            <td>人工知能</td>
            <td>木曜日:3限</td>
            </tr>

            <tr>
            <td>セキュリティ</td>
             <td>木曜日:4限</td>
            </tr>

            <tr>
            <td>ネトプロ</td>
            <td>金曜:1,2限</td>
            </tr>

            </table>
            <br>
            <div style="padding: 10px; margin-bottom: 10px; border: 1px dotted #333333; border-radius: 5px;">
    
    <div style="border: 15px solid #000; padding: 10px;">
    人工知能:目的概要<br>
    </div>
    コンピュータの究極の高度利用法と位置づけられるのが人工知能である。<br>
    この分野の諸技術をコンピュータシステムやその発展と関連づけつつ<br>
    他科目では扱っていない話題を中心に順に取り上げる。
</div>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

    @app.post("/order")
async def take_order(item: str, quantity: int = 1):
    # 在庫チェック（今回は簡易的に3品まで）
    if quantity > 3:
        return {"response": f"申し訳ありません、{item}は一度に3個までしか注文できません。"}
    return {
        "response": f"ご注文ありがとうございます！{item}を{quantity}個承りました。",
        "item": item,
        "quantity": quantity,
        "status": "受付完了"
    }