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
            <table>
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
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)