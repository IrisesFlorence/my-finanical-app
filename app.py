import streamlit as st
import math

st.set_page_config(page_title="QQQ 定期定額計算機", page_icon="💰")

st.title("📈 QQQ 長期投資增長預測")
st.write("設定你的定期定額計劃，看看 15 年後的成果！")

# 1. 輸入參數
initial_investment = st.number_input("初始啟動資金 (USD)", min_value=0, value=1000)
periodic_amount = st.number_input("每次定額投入金額 (USD)", min_value=0, value=650)
price_now = st.number_input("現時 QQQ 股價 (USD)", min_value=1.0, value=650.1)
frequency = st.selectbox("投資頻率", ["每個月", "每三個月", "每半年", "每年"])

# 2. 設定計算邏輯
freq_map = {"每個月": 12, "每三個月": 4, "每半年": 2, "每年": 1}
periods_per_year = freq_map[frequency]
total_years = 15
total_periods = total_years * periods_per_year
annual_rate = 0.12 # 假設平均年回報 12%
periodic_rate = annual_rate / periods_per_year

# 3. 計算複利
# (A) 初始資金如果「一直唔理」15年後嘅價值
fv_only_initial = initial_investment * math.pow((1 + annual_rate), total_years)

# (B) 定期定額增值嘅部分
fv_periodic = periodic_amount * ((math.pow(1 + periodic_rate, total_periods) - 1) / periodic_rate) * (1 + periodic_rate)

# (C) 總資產 (初始 + 定期)
total_fv = fv_initial_value = (initial_investment * math.pow((1 + annual_rate), total_years)) + fv_periodic
total_invested = initial_investment + (periodic_amount * total_periods)

# 4. 顯示結果
st.divider()
st.subheader(f"📊 {total_years} 年後的預期結果")
st.write(f"### 預計總資產：**${total_fv:,.2f}**")

# 新加嘅對比行
st.info(f"💡 若初始資金 ${initial_investment:,.2f} 一直唔理，15 年後僅變為：${fv_only_initial:,.2f}")

st.write(f"總投入本金（初始+供款）：${total_invested:,.2f}")
st.write(f"淨賺利息：${total_fv - total_invested:,.2f}")

st.divider()
st.success(f"💡 透過持續「{frequency}」定額投資，你的財富增長了約 {total_fv/total_invested:.1f} 倍！")
st.caption("註：假設年化回報 12%，市場有波動，數據僅供參考。")

