import streamlit as st
import math

# 網頁外觀設定
st.set_page_config(page_title="專屬 QQQ 計算器", page_icon="💰")

# 噴氣球驚喜
st.balloons()

st.title("💖 專屬你的財富增長計算器")
st.write("只要堅持投資 QQQ，15 年後的你一定會感謝現在的自己！")

# 輸入區
st.divider()
amount = st.number_input("預計投入總金額 (USD)", min_value=100, value=1000, step=100)
price = st.number_input("買入時 QQQ 的實質股價 (USD)", min_value=1.0, value=445.0)

# 計算邏輯
years = 15
rate = 0.12 # 假設年回報 12%
shares = amount / price
future_value = amount * math.pow((1 + rate), years)

# 結果顯示
st.subheader("📊 15 年後的預測結果")
st.metric("預計總價值", f"${future_value:,.2f}")
st.write(f"當初買入股數：**{shares:.2f}** 股")
st.success(f"這筆錢在 15 年後翻了約 **{future_value/amount:.1f}** 倍！")

st.divider()
st.info("💡 投資小秘訣：市場波動是正常的，最重要是保持耐心。")
