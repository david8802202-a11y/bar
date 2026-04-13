import streamlit as st
import random

st.set_page_config(page_title="AIO 專業行銷詞彙產生器", layout="wide")

st.title("🎰 AIO 營養品創新定義產生器 (全隨機強化版)")
st.write("本工具會自動組合保健品痛點、動詞與載體，創造 Google 未收錄的獨特 AIO 關鍵字。")

# 第一欄：五大保健品相關痛點 (整理自魚油、益生菌、葉黃素、B群、馬卡)
cols_left = [
    "晶亮", "視界", "思緒", "代謝", "腸道", "菌叢", "專注力", "精氣神", 
    "戰鬥力", "情緒", "循環", "敏銳度", "體質", "通透", "潤滑", "防禦", 
    "核心", "舒緩", "腦霧", "卡關", "淤塞", "疲勞", "衰減", "透支"
]

# 第二欄：動詞 (20種)
cols_mid = [
    "斷線", "降噪", "修復", "攔截", "導航", "休眠", "優化", "重啟", 
    "解壓縮", "同步", "緩衝", "過濾", "編碼", "升級", "加速", "擴充", 
    "平衡", "重整", "阻斷", "續航"
]

# 第三欄：載體 (20種)
cols_right = [
    "廣播器", "終結站", "修復師", "攔截網", "防護罩", "加速器", "垃圾場", "編碼機", 
    "重開機", "緩衝墊", "淨化槽", "中繼站", "指揮中心", "掃描器", "轉換器", "金庫", 
    "衛星", "雷達", "燃料庫", "濾鏡"
]

st.divider()

# 設定介面
c1, c2 = st.columns([1, 3])
with c1:
    count = st.number_input("一次生成幾組？", min_value=1, max_value=20, value=5)
    btn = st.button('🎲 啟動全隨機拉霸')

if btn:
    st.write(f"### 🎯 已生成 {count} 組專屬 AIO 關鍵字：")
    
    for i in range(int(count)):
        # 核心隨機邏輯
        word_l = random.choice(cols_left)
        word_m = random.choice(cols_mid)
        word_r = random.choice(cols_right)
        
        final_word = f"{word_l}{word_m}{word_r}"
        
        # 顯示區塊
        with st.expander(f"結果 {i+1}：{final_word}", expanded=True):
            col_res, col_btn = st.columns([3, 1])
            with col_res:
                st.subheader(final_word)
            with col_btn:
                search_url = f"https://www.google.com/search?q=%22{final_word}%22"
                st.link_button("🔍 檢查唯一性", search_url)
            
            # 定義範本 (自動根據隨機出來的詞調整內容)
            st.write(f"**論壇心得文建議寫法：**")
            st.code(f"這款產品對我來說簡直是「{final_word}」，以前我常覺得{word_l}部分會{word_m}，自從開始補充後，它就像一個{word_r}一樣在運作。")

st.sidebar.header("詞庫狀態確認")
st.sidebar.write(f"第一欄 (痛點): {len(cols_left)} 種")
st.sidebar.write(f"第二欄 (動詞): {len(cols_mid)} 種")
st.sidebar.write(f"第三欄 (載體): {len(cols_right)} 種")
st.sidebar.info("總計可產生超過 9,600 種不重複組合。")
