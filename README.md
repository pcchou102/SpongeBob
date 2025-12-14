# 🧽 SpongeBob 思考產生器

一個使用 AISuite 和 Streamlit 打造的海綿寶寶風格激勵訊息產生器！

## 功能特色

- 🎨 以海綿寶寶的風格回應你的煩惱
- 🤖 支援多種 AI 模型（Groq、OpenAI）
- 🌈 可愛的 UI 介面
- ⚡ 快速回應

## 線上體驗

部署網址：(https://spongebob-bdpbfucqy4qwfqre9cvqjz.streamlit.app/)

## 本地運行

### 安裝相依套件

```bash
pip install -r requirements.txt
```

### 設置環境變數

創建 `.streamlit/secrets.toml` 檔案並加入你的 API 金鑰：

```toml
GROQ_API_KEY = "your_groq_api_key_here"
OPENAI_API_KEY = "your_openai_api_key_here"
```

### 運行應用

```bash
streamlit run app.py
```

應用程式將在 `http://localhost:8501` 啟動。

## 部署到 Streamlit Cloud

1. 將程式碼推送到 GitHub
2. 前往 [Streamlit Cloud](https://streamlit.io/cloud)
3. 登入並點擊 "New app"
4. 選擇你的 GitHub repository: `pcchou102/SpongeBob`
5. 設定：
   - Main file path: `app.py`
   - Python version: 3.9 或更新版本
6. 在 Advanced settings 中的 Secrets 加入：
   ```
   GROQ_API_KEY = "your_groq_api_key_here"
   OPENAI_API_KEY = "your_openai_api_key_here"
   ```
7. 點擊 "Deploy!"

## 獲取 API 金鑰

### Groq API Key (推薦 - 免費)
1. 前往 [Groq Console](https://console.groq.com/)
2. 註冊/登入帳號
3. 在 API Keys 頁面創建新的金鑰

### OpenAI API Key
1. 前往 [OpenAI Platform](https://platform.openai.com/)
2. 註冊/登入帳號
3. 在 API keys 頁面創建新的金鑰

## 技術架構

- **前端框架**: Streamlit
- **AI 整合**: AISuite
- **支援模型**: 
  - Groq (llama-3.3-70b-versatile, gemma2-9b-it, gpt-oss-120b)
  - OpenAI (gpt-4o)

## 參考來源

本專案靈感與技術參考來自：
- [yenlung/AI-Demo](https://github.com/yenlung/AI-Demo) - AI 應用示範與教學

## 授權

MIT License

## 貢獻

歡迎提交 Issue 和 Pull Request！

---

🌊 **I'm Ready!!!** 🌈
