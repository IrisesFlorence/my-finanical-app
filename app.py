import streamlit as st
import pandas as pd
import math

st.set_page_config(page_title="QQQ 定期定額計算機", page_icon="💰")
st.balloons()

st.title("📈 QQQ 長期投資增長預測")
st.write("設定你的定期定額計劃，看看 15 年後的成果！")

st.divider()

# 輸入區
col1, col2 = st.columns(2)
with col1:
initial_investment = st.number_input("初始啟動資金 (USD)", min_value=0, value=1000)
periodic_amount = st.number_input("每次定額投入金額 (USD)", min_value=0, value=650)

with col2:
price_now = st.number_input("現時 QQQ 股價 (USD)", min_value=1.0, value=650.0)
frequency = st.selectbox("投資頻率", ["每個月", "每三個月", "每半年", "每年"])

# 轉換頻率為數值
freq_map = {"每個月": 12, "每三個月": 4, "每半年": 2, "每年": 1}
periods_per_year = freq_map[frequency]
total_periods = 15 * periods_per_year
annual_rate = 0.12 # 假設年回報 12%
periodic_rate = annual_rate / periods_per_year

# 計算複利 (定期定額公式)
# 初始資金增值 + 定期定額增值
fv_initial = initial_investment * math.pow((1 + annual_rate), 15)
fv_periodic = periodic_amount * ((math.pow(1 + periodic_rate, total_periods) - 1) / periodic_rate) * (1 + periodic_rate)

total_fv = fv_initial + fv_periodic
total_invested = initial_investment + (periodic_amount * total_periods)

# 顯示結果
st.subheader(f"📊 15 年後 ({frequency}供款) 的結果")
st.metric("預計總資產", f"${total_fv:,.2f}")

col3, col4 = st.columns(2)
col3.write(f"總投入本金：${total_invested:,.2f}")
col4.write(f"淨賺利息：${total_fv - total_invested:,.2f}")

st.divider()
st.success(f"💡 透過「{frequency}」定額投資，你的財富增長了約 {total_fv/total_invested:.1f} 倍！")
st.caption("註：此模型假設年化回報率為 12%，市場有波動，數據僅供參考。")
