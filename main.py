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
                <b>
                    人工知能:目的概要
                </b>
                コンピュータの究極の高度利用法と位置づけられるのが人工知能である。<br>
                この分野の諸技術をコンピュータシステムやその発展と関連づけつつ<br>
                他科目では扱っていない話題を中心に順に取り上げる。
            </div><br>

            <div style="padding: 10px; margin-bottom: 10px; border: 1px dotted #333333; border-radius: 5px;">
                <b>
                    セキュリティ:目的概要
                </b>
                情報セキュリティに関する脅威と対策を理解し、暗号技術に関わる知識を習得する。<br>
                【授業形態】講義、遠隔講義(他大学のみ)<br>
                【enPiT科目】enPiT2 BasicSecCap(セキュリティ総論C)科目に対応する。
            </div><br>

            <div style="padding: 10px; margin-bottom: 10px; border: 1px dotted #333333; border-radius: 5px;">
                <b>
                    ネトプロ:目的概要
                </b>
                クライアント、サーバモデル、TCP通信やUDP通信、アプリケーションプログラミングインタフェース(API)の基本および<br>
                ネットワークアプリケーションを効率的に動作させるためのマルチスレッドプログラミングを講義する。<br>
                この基本の後、チャット等の対話型アプリケーション開発の実例、マルチスレッド、WebAPI、Webクライアントを講義し<br>
                開発手法、デプロイ手法を習得する。最終課題として自ら考案したネットワーク利用したシステムを企画し<br>
                チームによりプログラミング実装を行い、発表を行う。
            </div>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.post("/order")
async def take_order(item: str, quantity: int = 1):
    # 在庫チェック（今回は簡易的に3品まで）
    if quantity > 1:
        return {"response": f"申し訳ありません、{item}は一度に3個までしか注文できません。"}
    return {
        "response": f"ご注文ありがとうございます！{item}を{quantity}個承りました。",
        "item": item,
        "quantity": quantity,
        "status": "受付完了"
    }