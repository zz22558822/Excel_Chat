from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import sqlite3
import datetime
from dateutil.relativedelta import relativedelta

# 初始化 FastAPI 應用
app = FastAPI()

# 設定 CORS 允許跨域請求
origins = [
    "http://你的Domain",
    "https://你的Domain",
    "http://localhost",
    "http://127.0.0.1",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # 允許所有 HTTP 方法
    allow_headers=["*"],  # 允許所有標頭
)

# 定義資料結構
class Hardware(BaseModel):
    name: str
    text: str

# 連接 SQLite 資料庫
def get_db_connection():
    conn = sqlite3.connect('database.db')  # 使用指定的資料庫文件
    conn.row_factory = sqlite3.Row  # 使得返回的是字典型態資料
    return conn

# 建立資料表
def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Chat_Data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            recordTime DATE,
            text TEXT
        )
    ''')
    conn.commit()
    conn.close()

# 呼叫資料庫創建表格
create_table()


# API :新增訊息
@app.post("/api/add_Text")
async def add_Text(hardware: Hardware):
    # 檢查必須的欄位是否提供
    if not hardware.name or not hardware.text:
        raise HTTPException(status_code=400, detail="需少必要資料")

    # 插入資料到資料庫
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        # 取得當下時間（格式：YYYY-MM-DD HH:MM:SS）
        record_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute('''
            INSERT INTO Chat_Data (name, recordTime, text)
            VALUES (?, ?, ?)
        ''', (hardware.name, record_time, hardware.text))
        conn.commit()
    except sqlite3.IntegrityError:
        # 返回錯誤
        conn.close()
        raise HTTPException(status_code=400, detail="資料重複寫入")

    conn.close()
    return {"message": "資料成功寫入。"}

# API :查詢訊息
@app.get("/api/get_last_text")
async def get_last_text():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT text FROM Chat_Data ORDER BY id DESC LIMIT 1")
    row = cursor.fetchone()
    
    conn.close()

    if row:
        return {"text": row[0]}
    else:
        return {"text": "無訊息"}
