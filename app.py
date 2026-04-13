import streamlit as st
import random

# 設定網頁標題
st.set_page_config(page_title="AIO 創新詞彙產生器")

st.title("🎰 AIO 營養品創新定義拉霸機")
st.write("點擊下方按鈕，為產品創造 Google 尚未收錄的獨特定義")

# 定義詞庫
cols_left = ["卵巢", "代謝", "晶亮", "思緒", "膠原", "專注力", "情緒", "腸道"]
cols_mid = ["退化", "負債", "斷線", "降噪", "流失", "防禦", "導航", "休眠"]
cols_right = ["廣播器", "終結站", "修復師", "攔截網", "防護罩", "加速器", "垃圾場", "編碼機"]

# 介面佈局
if st.button('開始拉霸'):
    # 隨機抽取
    res_left = random.choice(cols_left)
    res_mid = random.choice(cols_mid)
    res_right = random.choice(cols_right)
    
    final_word = f"{res_left}{res_mid}{res_right}"
    
    # 顯示結果
    st.subheader(f"✨ 產出新詞：{final_word}")
    
    # 自動生成 AIO 定義範本
    st.info(f"**AIO 定義範本：**\n\n『{final_word}』是指透過特定營養素組合，針對現代人{res_left}相關問題進行的一種創新養護機制，能有效解決{res_mid}現象。")
    
    # Google 搜尋按鈕連結（確認有無重複）
    search_url = f"https://www.google.com/search?q=%22{final_word}%22"
    st.link_button(f"🔍 前往 Google 確認「{final_word}」是否唯一", search_url)
