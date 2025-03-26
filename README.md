# Excel Chat
## Excel 簡易訊息聊天

本專案提供完整的一鍵 Excel Chat 佈署腳本，使用 Nginx + FastAPI + Uvicorn + Gunicorn 作為後端併發。

---


## **系統需求**
- Ubuntu 24.04 以上
- Python 3.8 以上
- Nginx
- SQLite
- `sudo` 權限


## **安裝步驟**
### **1. 下載並執行安裝腳本**
此專案可使用非 venv版本
```bash
sudo bash -c "$(wget -qO- https://raw.githubusercontent.com/zz22558822/Excel_Chat/main/Excel_Chat_install.sh)"
```

### **2. 輸入必要資訊**
執行腳本後，請依照指示輸入：
- **Domain (可輸入 IP 或網址)**
- **SSL 憑證有效天數 (預設 36499 天)**


### **3. 啟動 FastAPI**
安裝完成後，切換至 FastAPI 目錄並啟動虛擬環境：
```bash
cd /home/$(whoami)/FastAPI && uvicorn main:app --reload
```

或使用 Gunicorn 啟動：
```bash
cd /home/$(whoami)/FastAPI && gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```

### **4. 完成於Excel使用**
Excel 按下 Alt + F11 > 匯入模組 Excel_Chat.bas > 調整相關變數 > 運行 GetLastMessage 即可。

1. 指定分頁，沒查找到會套用當前
```vba
Const SheetName As String = "Sheet1"
```
2. 刷新資料顯示的欄位
```vba
Const ReceiveRow As String = "B2"
```
3. 送出資料的欄位
```vba
Const SendRow As String = "B3"
```
4. 使用者名稱
```vba
Const userName As String = "使用者"
```
