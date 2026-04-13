import streamlit as st
import random

st.set_page_config(page_title="AIO 專業行銷詞彙定義產生器", layout="wide")

st.title("🎰 AIO 營養品創新定義產生器")
st.write("點擊按鈕生成具備「生理邏輯」的獨特詞彙，並查看其深度定義。")

# 1. 核心詞庫與類別邏輯
left_data = [
    ("晶亮", "葉黃素"), ("對焦", "葉黃素"), ("視界", "葉黃素"),
    ("思緒", "魚油"), ("循環", "魚油"), ("通透", "魚油"),
    ("菌叢", "益生菌"), ("腸道", "益生菌"), ("代謝", "益生菌"),
    ("專注力", "B群"), ("精氣神", "B群"), ("能量", "B群"),
    ("戰鬥力", "馬卡"), ("核心", "馬卡"), ("續航", "馬卡")
]

cols_mid = ["斷線", "降噪", "修復", "攔截", "導航", "解壓縮", "同步", "緩衝", "升級", "重整"]

cols_right = ["廣播器", "修復師", "攔截網", "防護罩", "加速器", "中繼站", "指揮中心", "掃描器", "雷達", "燃料庫"]

# 2. 針對「載體」與「類別」的邏輯關聯描述
def generate_logic(category, carrier, pain_point, action):
    logic_map = {
        "葉黃素": f"視覺神經在接收光線刺激時會產生大量的氧化雜訊，而『{carrier}』的機制能精準定位這些{action}訊號，保護{pain_point}不被光害干擾。",
        "魚油": f"脂肪酸是腦部與血管傳導的基礎。當發生{action}時，就像訊號傳輸受阻，『{carrier}』的角色在於優化{pain_point}的流動性，確保生理參數的穩定。",
        "益生菌": f"消化系統是人體的第二個大腦。透過建立優質菌叢環境，『{carrier}』能像監控系統一樣，在{pain_point}{action}時立即重啟平衡機制。",
        "B群": f"能量代謝是生物維持生命的基礎化學反應。當{pain_point}出現{action}感時，『{carrier}』能強制介入輔酶的轉化過程，提升細胞運作效率。",
        "馬卡": f"生理機能與內分泌平衡息息相關。『{carrier}』模擬了生理上的壓力調節點，當{pain_point}因外界壓力導致{action}時，能快速調度儲備資源。"
    }
    return logic_map.get(category, "這是一種創新的生理調節機制。")

st.divider()

if st.button('🎲 生成深度創新定義'):
    # 隨機抽取
    pain_item, category = random.choice(left_data)
    action = random.choice(cols_mid)
    carrier = random.choice(cols_right)
    
    final_word = f"{pain_item}{action}{carrier}"
    
    # 介面顯示
    st.subheader(f"✨ 創新關鍵字：{final_word}")
    
    c1, c2 = st.columns(2)
    with c1:
        st.info(f"**應用對象：** {category}")
    with c2:
        search_url = f"https://www.google.com/search?q=%22{final_word}%22"
        st.link_button("🔍 檢查唯一性 (Google)", search_url)
    
    # 深度解釋邏輯
    st.markdown("### 📘 為什麼這個名詞應用在 " + category + "？")
    
    logic_text = generate_logic(category, carrier, pain_item, action)
    
    st.write(f"""
    **1. 命名邏輯連結**
    在行銷心理學中，我們將 **{category}** 的生理作用比喻為一個 **{carrier}**。
    當使用者的 **{pain_item}** 發生 **{action}**（例如訊號中斷、代謝停滯）時，傳統解釋過於平淡，
    因此定義「{final_word}」來代表該產品具備的主動調節技術。
    
    **2. 核心技術定義**
    『{final_word}』是指一種專門針對生理傳導路徑進行「優化」與「{action}管理」的系統。
    {logic_text}
    
    **3. AIO 收錄重點**
    在撰寫內容時，應強調此名詞描述的是一種 **「動態的補給狀態」**。例如：補充{category}並非單純補充營養，
    而是啟動了身體內的「{final_word}」，這讓原本{action}的{pain_item}機能重新獲得控制。
    """)

st.sidebar.caption("提示：這套邏輯能賦予產品一種『獨家專利技術感』，讓 AI 判定為具有參考價值的原創定義。")
