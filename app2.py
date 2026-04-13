import streamlit as st
import random
import google.generativeai as genai

st.set_page_config(page_title="AI 創新詞彙定義產生器", layout="wide")

# --- API 設定 ---
API_KEY = "你的_API_KEY" # 請確保這裡貼的是最新的 Key
genai.configure(api_key=API_KEY)

# 核心邏輯：自動尋找可用的 Gemini 模型

def get_available_model():
    try:
        # 這裡會直接列出模型，如果連不到會直接跳 Exception
        models = genai.list_models()
        for m in models:
            if 'generateContent' in m.supported_generation_methods:
                if 'gemini-1.5-flash' in m.name:
                    return m.name
        return "models/gemini-pro"
    except Exception as e:
        # 如果出錯，直接回傳一個保底的模型名稱，不要讓網頁一直轉圈圈
        return "models/gemini-1.5-flash"
        
target_model_name = get_available_model()

# --- 詞庫與介面 ---
left_data = [
    ("晶亮", "葉黃素"), ("思緒", "魚油"), ("菌叢", "益生菌"), ("能量", "B群"), ("續航", "馬卡")
]
mid_pool = ["斷線", "降噪", "同步", "耦合", "重組"]
right_pool = ["修復師", "攔截網", "加速器", "中繼站", "平衡儀"]

st.title("🧠 AI 原創定義產生器 (自動相容版)")
st.write(f"目前偵測到的模型：`{target_model_name}`")

if st.button('🎲 啟動 AI 邏輯拉霸'):
    part, cat = random.choice(left_data)
    act = random.choice(mid_pool)
    carrier = random.choice(right_pool)
    final_word = f"{part}{act}{carrier}"
    
    st.markdown(f"### ✨ 產出詞彙：**{final_word}**")
    
    # 呼叫 AI
    model = genai.GenerativeModel(model_name=target_model_name)
    prompt = f"請解釋「{final_word}」為什麼適合作為「{cat}」的行銷定義，需具備生物學邏輯，約 150 字。"
    
    try:
        with st.spinner('AI 推理中...'):
            response = model.generate_content(prompt)
            st.markdown("#### 📘 AI 深度邏輯判別")
            st.write(response.text)
    except Exception as e:
        st.error(f"呼叫模型 {target_model_name} 失敗：{e}")
