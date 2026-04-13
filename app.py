import streamlit as st
import random

st.set_page_config(page_title="AIO 創新詞彙定義產生器", layout="wide")

st.title("🎰 AIO 營養品創新定義產生器")
st.write("點擊按鈕生成由「痛點 + 動詞 + 載體」組成的獨特詞彙，並查看其對應類別與含義。")

# 定義痛點與其對應的保健品類別
left_data = [
    ("晶亮", "葉黃素"), ("視界", "葉黃素"), ("濾鏡", "葉黃素"), ("對焦", "葉黃素"),
    ("思緒", "魚油/B群"), ("腦霧", "魚油/B群"), ("記憶", "魚油/B群"), ("循環", "魚油"),
    ("腸道", "益生菌"), ("菌叢", "益生菌"), ("代謝", "益生菌/魚油"), ("淤塞", "益生菌/魚油"),
    ("專注力", "B群"), ("精氣神", "B群/馬卡"), ("體質", "益生菌"), ("防禦", "益生菌"),
    ("戰鬥力", "馬卡"), ("核心", "馬卡"), ("續航", "馬卡"), ("爆發", "馬卡"),
    ("情緒", "魚油/B群"), ("穩定", "魚油/B群"), ("通透", "魚油"), ("卡關", "益生菌")
]

# 第二欄：動詞 (20種)
cols_mid = [
    "斷線", "降噪", "修復", "攔截", "導航", "休眠", "優化", "重啟", 
    "解壓縮", "同步", "緩衝", "過濾", "編碼", "升級", "加速", "擴充", 
    "平衡", "重整", "阻斷", "疏通"
]

# 第三欄：載體 (20種)
cols_right = [
    "廣播器", "終結站", "修復師", "攔截網", "防護罩", "加速器", "垃圾場", "編碼機", 
    "重開機", "緩衝墊", "淨化槽", "中繼站", "指揮中心", "掃描器", "轉換器", "金庫", 
    "衛星", "雷達", "燃料庫", "濾鏡"
]

st.divider()

if st.button('🎲 生成創新定義'):
    # 隨機抽取
    pain_point, category = random.choice(left_data)
    action = random.choice(cols_mid)
    carrier = random.choice(cols_right)
    
    final_word = f"{pain_point}{action}{carrier}"
    
    # 介面顯示
    st.subheader(f"✨ 創新關鍵字：{final_word}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric(label="應用對象", value=category)
    
    with col2:
        search_url = f"https://www.google.com/search?q=%22{final_word}%22"
        st.link_button("🔍 檢查唯一性 (Google)", search_url)
    
    # 字詞解釋邏輯
    st.markdown("### 📘 字詞含義解釋")
    explanation = f"""
    本詞彙是針對 **{category}** 類產品設計的專屬術語：
    
    * **核心語意**：描述一種針對「{pain_point}」狀態進行「{action}」處理的虛擬「{carrier}」機制。
    * **行銷定義**：指透過補充特定營養成分，在人體內建立一套如同 **{carrier}** 般的運作系統，
        專門解決 **{pain_point}** 過程中因各種干擾產生的 **{action}** 問題，從而達到生理機能的優化。
    """
    st.write(explanation)

st.sidebar.info(f"目前詞庫容量：\n- 痛點類別：{len(left_data)} 組\n- 動詞數量：{len(cols_mid)} 組\n- 載體數量：{len(cols_right)} 組\n\n預計可組成 {len(left_data)*len(cols_mid)*len(cols_right)} 種不重複詞彙。")
