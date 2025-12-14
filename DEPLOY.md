# SpongeBob 思考產生器 - 部署指南

## 📋 快速部署步驟

### 1️⃣ 初始化 Git Repository

```powershell
cd "c:\Users\周\Desktop\AIOT\HW4"
git init
git add .
git commit -m "Initial commit: SpongeBob Streamlit App"
```

### 2️⃣ 推送到 GitHub

```powershell
git remote add origin https://github.com/pcchou102/SpongeBob.git
git branch -M main
git push -u origin main
```

### 3️⃣ 部署到 Streamlit Cloud

1. 前往 https://share.streamlit.io/
2. 登入你的 GitHub 帳號
3. 點擊 **"New app"**
4. 填寫資訊：
   - **Repository**: `pcchou102/SpongeBob`
   - **Branch**: `main`
   - **Main file path**: `app.py`
5. 點擊 **"Advanced settings"**
6. 在 **Secrets** 區塊貼上：
   ```toml
   GROQ_API_KEY = "你的 Groq API 金鑰"
   OPENAI_API_KEY = "你的 OpenAI API 金鑰（可選）"
   ```
7. 點擊 **"Deploy!"**

### 4️⃣ 獲取 API 金鑰

#### Groq API Key（免費，推薦！）
- 網址：https://console.groq.com/
- 註冊後在 "API Keys" 頁面創建金鑰

#### OpenAI API Key（付費）
- 網址：https://platform.openai.com/
- 註冊後在 "API keys" 頁面創建金鑰

## 🧪 本地測試

1. 安裝套件：
   ```powershell
   pip install -r requirements.txt
   ```

2. 設定 Secrets：
   - 複製 `.streamlit/secrets.toml.example` 為 `.streamlit/secrets.toml`
   - 填入你的 API 金鑰

3. 運行應用：
   ```powershell
   streamlit run app.py
   ```

4. 在瀏覽器打開：http://localhost:8501

## 📁 檔案結構

```
HW4/
├── app.py                          # Streamlit 主程式
├── requirements.txt                # Python 套件相依
├── README.md                       # 專案說明文件
├── DEPLOY.md                       # 部署指南（本文件）
├── .gitignore                      # Git 忽略檔案
├── .streamlit/
│   ├── config.toml                 # Streamlit 設定
│   └── secrets.toml.example        # Secrets 範本
└── 【Demo04】用AISuite打造海綿寶寶思考生成器.ipynb  # 原始 Notebook
```

## 🔧 常見問題

### Q: 如果已經有 GitHub repository 了？
直接執行推送指令即可：
```powershell
git remote add origin https://github.com/pcchou102/SpongeBob.git
git push -u origin main
```

### Q: 出現 "API key not found" 錯誤？
檢查 Streamlit Cloud 的 Secrets 設定是否正確，確保變數名稱完全一致。

### Q: 想要更改 UI 顏色？
編輯 `.streamlit/config.toml` 檔案中的顏色設定。

### Q: 可以使用其他 AI 模型嗎？
可以！在 `app.py` 的 `provider_options` 中加入新的模型選項。

## 🎨 自訂設定

### 修改主題顏色
編輯 `.streamlit/config.toml`：
```toml
[theme]
primaryColor = "#FFD700"          # 主要顏色
backgroundColor = "#87CEEB"        # 背景顏色
secondaryBackgroundColor = "#F0F8FF"  # 次要背景
textColor = "#000000"              # 文字顏色
```

### 新增模型
在 `app.py` 中的 `provider_options` 字典新增：
```python
"你的模型名稱": ("provider", "model_name")
```

## 🚀 更新部署

當你修改程式碼後：
```powershell
git add .
git commit -m "更新描述"
git push
```

Streamlit Cloud 會自動偵測變更並重新部署！

---

**祝你部署順利！I'm Ready!!! 🌈**
