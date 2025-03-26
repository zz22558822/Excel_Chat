import sqlite3

# 連接到數據庫（如果不存在，則會創建新的數據庫文件）
conn = sqlite3.connect('database.db')

# 創建一個游標對象
cursor = conn.cursor()

# 創建數據表
cursor.execute('''CREATE TABLE IF NOT EXISTS Chat_Data (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    recordTime DATE,
                    text TEXT
                )''')

# 提交更改並關閉連接
conn.commit()
conn.close()
