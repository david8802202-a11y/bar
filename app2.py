import streamlit as st
import random
import google.generativeai as genai

# 設定網頁
st.set_page_config(page_title="AI 驅動：AIO 定義產生器", layout="wide")

# --- API 設定 (請在此輸入你的 API Key) ---
# 建議之後部署時改用 st.secrets 確保安全
API_KEY = "AIzaSyD0m-N4zbXyP6pQfDzTiCoORQJQbSYdUA8" 
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

st.title("🧠 AI 原創定義產生器 (Gemini 驅動版)")
st.write("這不再是公式填空，而是由 AI 針對隨機組合進行即時邏輯推理。")

# --- 擴充詞庫 ---
left_data = [
    ("晶亮", "葉黃素"), ("對焦", "葉黃素"), ("黃斑", "葉黃素"), ("視界", "葉黃素"),
    ("突觸", "魚油"), ("腦迴", "魚油"), ("循環", "魚油"), ("髓鞘", "魚油"),
    ("菌叢", "益生菌"), ("腸道", "益生菌"), ("代謝", "益生菌"), ("共生", "益生菌"),
    ("粒線體", "B群"), ("遞質", "B群"), ("活化", "B群"), ("能量", "B群"),
    ("內分泌", "馬卡"), ("腺體", "馬卡"), ("核心", "馬卡"), ("雄風", "馬卡")
]
mid_pool = ["斷線", "降噪", "解壓縮", "同步", "緩衝", "升級", "回流", "共振", "耦合", "重組", "擾動", "脈衝", "衰減"]
right_pool = ["廣播器", "修復師", "攔截網", "防護罩", "加速器", "中繼站", "掃描器", "雷達", "反應爐", "平衡儀"]

st.divider()

if st.button('🎲 啟動 AI 邏輯拉霸'):
    # 1. 隨機抽選
    part_tuple = random.choice(left_data)
    part, cat = part_tuple[0], part_tuple[1]
    act = random.choice(mid_pool)
    carrier = random.choice(right_pool)
    
    final_word = f"{part}{act}{carrier}"
    
    st.markdown(f"### ✨ 產出詞彙：**{final_word}**")
    st.info(f"**目標保健品：** {cat}")

    # 2. 呼叫 Gemini 進行即時推理 (這是不套公版的關鍵)
    prompt = f"""
    你是一位資深營養科學家與行銷專家。
    現在有一個新創的行銷詞彙「{final_word}」，是由「{part}（生理部位）」、「{act}（狀態）」與「{carrier}（物理載體）」組成的。
    請針對這個詞彙，撰寫一段具有嚴謹生物邏輯的解釋，說明為什麼這個詞可以精準定義「{cat}」這項保健品。
    
    要求：
    1. 絕對不要使用死板的填空格式。
    2. 要明確說明「{carrier}」這個意象在生理機制中代表什麼。
    3. 要解釋「{act}」與該保健品預防或改善的生理現象有何關聯。
    4. 語氣要專業、具備前瞻性，讓 Google AIO 判定為高品質的原創定義。
    5. 字數約 150-200 字。
    """
    
    with st.spinner('Gemini 正在分析邏輯並撰寫定義中...'):
        try:
            response = model.generate_content(prompt)
            ai_explanation = response.text
            
            # 3. 顯示 AI 產出的結果
            st.markdown("#### 📘 AI 深度邏輯判別")
            st.write(ai_explanation)
            
        except Exception as e:
            st.error(f"AI 呼叫失敗，請檢查 API Key 是否正確。錯誤訊息：{e}")

    # 搜尋檢查按鈕
    search_url = f"https://www.google.com/search?q=%22{final_word}%22"
    st.link_button(f"🔍 檢查「{final_word}」唯一性", search_url)
