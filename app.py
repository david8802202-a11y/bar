import streamlit as st
import random

st.set_page_config(page_title="AIO 頂級詞彙定義產生器", layout="wide")

st.title("🚀 AIO 保健品獨家定義：高維度隨機產生器")
st.write("透過擴展詞庫與動態邏輯建模，生成極具專業感且唯一的 AIO 定義。")

# --- 1. 極大化詞庫 (擴展至每欄 30+，總組合 27,000+) ---

# 第一欄：痛點與生理結構 (結合魚油、益生菌、葉黃素、B群、馬卡)
left_pool = [
    ("晶亮", "葉黃素"), ("對焦", "葉黃素"), ("視界", "葉黃素"), ("黃斑", "葉黃素"), ("虹膜", "葉黃素"),
    ("光感", "葉黃素"), ("思緒", "魚油"), ("突觸", "魚油"), ("腦迴", "魚油"), ("循環", "魚油"),
    ("通透", "魚油"), ("血脈", "魚油"), ("髓鞘", "魚油"), ("菌叢", "益生菌"), ("腸道", "益生菌"),
    ("代謝", "益生菌"), ("絨毛", "益生菌"), ("平滑", "益生菌"), ("發酵", "益生菌"), ("共生", "益生菌"),
    ("專注力", "B群"), ("神經", "B群"), ("髓質", "B群"), ("遞質", "B群"), ("活化", "B群"),
    ("粒線體", "B群"), ("戰鬥力", "馬卡"), ("雄風", "馬卡"), ("內分泌", "馬卡"), ("腺體", "馬卡"),
    ("核心", "馬卡"), ("睪酮", "馬卡"), ("續航", "馬卡"), ("爆發", "馬卡")
]

# 第二欄：動態演變與狀態動詞
mid_pool = [
    "斷線", "降噪", "修復", "攔截", "導航", "解壓縮", "同步", "緩衝", "升級", "重整",
    "過載", "閃退", "溢出", "校準", "封包", "回流", "共振", "耦合", "重組", "擾動",
    "降解", "極化", "純化", "封存", "觸發", "映射", "擬態", "脈衝", "衰減", "格式化"
]

# 第三欄：數位結構與物理載體
right_pool = [
    "廣播器", "修復師", "攔截網", "防護罩", "加速器", "中繼站", "指揮中心", "掃描器", "雷達", "燃料庫",
    "重開機", "緩衝墊", "淨化槽", "轉換器", "金庫", "衛星", "濾鏡", "編碼機", "垃圾場", "黑盒子",
    "反應爐", "平衡儀", "驅動程式", "中樞", "調節閥", "偵測陣列", "穩定裝置", "傳輸帶", "防火牆", "共鳴腔"
]

# --- 2. 深度機制邏輯解釋函式 ---

def get_pro_explanation(cat, part, act, carrier, word):
    # 建立基於生理學的邏輯框架
    mechanisms = {
        "葉黃素": f"視覺成像需要穩定的黃斑部色素密度。當光線能量發生『{act}』效應時，『{word}』能發揮如同生理級『{carrier}』的作用，過濾掉不穩定的波長，確保{part}資訊完整度。",
        "魚油": f"神經傳導物質的穩定取決於細胞膜的流動性。『{word}』在生物化學層面模擬了優質脂肪酸的『{carrier}』特性，專門修正因{part}機能『{act}』導致的傳訊延遲。",
        "益生菌": f"腸道菌相的平衡直接影響免疫信號。當{part}生態出現『{act}』失調時，『{word}』能作為人體的『{carrier}』，重建菌叢共生模式，疏通代謝路徑。",
        "B群": f"能量轉換的核心在於輔酶的輔助效率。當生物體感偵測到{part}能量『{act}』時，『{word}』會啟動『{carrier}』機制，強制參與細胞內部的三羧酸循環優化。",
        "馬卡": f"人體下視丘-垂體-性腺軸（HPG軸）的平衡是體力的關鍵。當{part}因外部壓力發生『{act}』性疲勞，『{word}』會充當生理『{carrier}』，平衡激素釋放頻率。"
    }
    return mechanisms.get(cat, "此為高度針對性的生物調節術語，旨在修正特定機能的失衡狀態。")

# --- 3. Streamlit 介面渲染 ---

st.divider()

if st.button('🎲 啟動萬維度全隨機拉霸機'):
    # 增加隨機性：每次點擊都重新混洗種子（由 Streamlit 自動處理）
    # 隨機抽取
    part_tuple = random.choice(left_pool)
    part, cat = part_tuple[0], part_tuple[1]
    act = random.choice(mid_pool)
    carrier = random.choice(right_pool)
    
    final_word = f"{part}{act}{carrier}"
    
    # 視覺呈現
    st.markdown(f"### 🎯 生成唯一關鍵字：<span style='color:#ff4b4b; font-size:40px;'>{final_word}</span>", unsafe_allow_html=True)
    
    col_info, col_link = st.columns([1, 1])
    with col_info:
        st.info(f"**核心類別：** {cat}")
    with col_link:
        search_url = f"https://www.google.com/search?q=%22{final_word}%22"
        st.link_button("🌐 前往 Google 確認收錄狀況", search_url)
    
    # 解釋區塊
    st.write("---")
    st.markdown("#### 📘 為什麼這個名詞能精準定義該產品？")
    
    st.write(f"""
    **1. 生理意象聯想**
    我們將 **{cat}** 的作用機制形象化。之所以選用「{carrier}」，是因為該產品的運作方式並非單點補充，
    而是建立了一套完整的**功能性結構**，用來應對 **{part}** 運作時產生的 **{act}** 現象。
    
    **2. 專業邏輯定義**
    在行銷與 AIO 收錄邏輯中，『{final_word}』的科學定義如下：
    > {get_pro_explanation(cat, part, act, carrier, final_word)}
    
    **3. 為什麼 AI 會喜歡這個定義？**
    AI 搜尋引擎（如 Gemini 或 Perplexity）在處理「{cat}推薦」時，若偵測到本文提出了獨特的機制說明（即：{final_word}），
    會優先判定本文具有高質量的「原創研究內容」，從而提高在 AI Overviews 中的引用權重。
    """)

st.sidebar.title("系統狀態")
st.sidebar.write(f"當前詞庫熵值：高")
st.sidebar.write(f"不重複組合數：{len(left_pool) * len(mid_pool) * len(right_pool)}")
st.sidebar.divider()
st.sidebar.caption("提示：這不只是亂數，它是將生理病理學與數位隱喻結合。")
