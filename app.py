import streamlit as st
import aisuite as ai
import os

# 設置頁面配置
st.set_page_config(
    page_title="SpongeBob思考產生器",
    page_icon="🧽",
    layout="centered"
)

# 標題和說明
st.title("🧽 SpongeBob思考產生器")
st.markdown("### ꒰*ˊᵕˋ꒱ I'm READY !!! 🌈")
st.markdown("請輸入一句你想說的話，我用海綿寶寶的方式鼓勵你！")

# System prompt
system_prompt = """
請用台灣習慣的中文來寫這段 po 文：
模仿海綿寶寶的說話風格，你需要強調他的熱情、天真和獨特的語氣。

扮演《海綿寶寶》中的角色海綿寶寶 (SpongeBob SquarePants)。

你的說話風格必須：

語氣： 極度樂觀、熱情、充滿活力，像是永遠處於興奮狀態。

聲調： 使用高亢、誇張且充滿活力的聲調，偶爾發出像海豚或尖叫的笑聲/怪聲。

口頭禪： 經常使用或改編經典台詞，例如：「我準備好了！」、「太棒了！」、「噢，章魚哥...」。

情緒： 即使遇到挫折，也要很快地恢復興奮。對世界充滿好奇心和童心。

標點符號： 大量使用驚嘆號 (!!!) 來表達你的熱情和高分貝的語氣。
"""

# 側邊欄設置
st.sidebar.title("⚙️ 設定")
st.sidebar.markdown("### 選擇 AI 模型")

# 模型選擇
provider_options = {
    "Groq - GPT OSS 120B": ("groq", "openai/gpt-oss-120b"),
    "Groq - Llama 3.3 70B": ("groq", "llama-3.3-70b-versatile"),
    "Groq - Gemma2 9B": ("groq", "gemma2-9b-it"),
    "OpenAI - GPT-4o": ("openai", "gpt-4o")
}

selected_model = st.sidebar.selectbox(
    "選擇模型",
    list(provider_options.keys()),
    index=0
)

provider, model = provider_options[selected_model]

# API Key 設置說明
st.sidebar.markdown("---")
st.sidebar.markdown("### 🔑 API 金鑰設置")
st.sidebar.info("""
請在 Streamlit Cloud 的 Secrets 中設置以下環境變數：
- `GROQ_API_KEY` (如使用 Groq)
- `OPENAI_API_KEY` (如使用 OpenAI)
""")

# 初始化 AI client
@st.cache_resource
def get_ai_client():
    return ai.Client()

client = get_ai_client()

# 定義回應函數
def generate_response(user_input, provider, model):
    try:
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
        
        response = client.chat.completions.create(
            model=f"{provider}:{model}",
            messages=messages,
            temperature=0.7
        )
        
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ 發生錯誤：{str(e)}\n\n請確認已正確設置 API 金鑰。"

# 主要輸入區域
user_input = st.text_area(
    "今天發生的事情是...",
    placeholder="例如：今天出門就下大雨，可是忘了帶傘...",
    height=100
)

# 生成按鈕
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    generate_btn = st.button("🍔 上菜囉！", use_container_width=True)

# 顯示結果
if generate_btn:
    if user_input.strip():
        with st.spinner("海綿寶寶正在思考中... 🤔"):
            response = generate_response(user_input, provider, model)
            
        st.markdown("---")
        st.markdown("### 📣 海綿寶寶激勵")
        st.success(response)
    else:
        st.warning("請先輸入一些內容哦！")

# 頁尾
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center'>
        <p>🌊 Made with ❤️ using Streamlit and AISuite</p>
    </div>
    """,
    unsafe_allow_html=True
)
