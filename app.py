import streamlit as st

# 页面配置
st.set_page_config(page_title="HTH 专属计算器", page_icon="📈", layout="centered")

# 标题
st.title("💰 HTH 专属金银量化工具")
st.markdown("---")

# 输入框：账户与风险
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        balance = st.number_input("账户总资金 ($)", value=10000, step=100)
    with col2:
        risk_percent = st.slider("风险比例 (%)", 1, 50, 10)

# 输入框：价格
with st.container():
    c1, c2 = st.columns(2)
    with c1:
        entry = st.number_input("📉 进场价格", value=4464.68, format="%.2f")
    with c2:
        sl = st.number_input("🛑 止损价格", value=4435.39, format="%.2f")

# 计算按钮
if st.button("🔥 开始 HTH 量化计算", use_container_width=True):
    sl_range = abs(entry - sl)
    if sl_range == 0:
        st.warning("止损距离不能为0！")
    else:
        # 核心逻辑
        risk_money = balance * (risk_percent / 100)
        lots = risk_money / (sl_range * 100)
        
        # 华丽展示
        st.balloons() # 撒花特效
        st.divider()
        
        # 结果大屏
        res1, res2 = st.columns(2)
        res1.metric(label="🎯 建议手数", value=f"{round(lots, 2)} 手")
        res2.metric(label="💸 计划亏损", value=f"${int(risk_money)}")
        
        direction = "🔴 做多 (BUY)" if entry > sl else "🟢 做空 (SELL)"
        st.info(f"建议方向：{direction}  |  止损空间：{round(sl_range, 2)} 美元")
        st.caption("注：以上基于黄金标准合约（1手=100盎司）计算。")

st.markdown("---")
st.markdown("<center>Powered by HTH Lab | 内部特供</center>", unsafe_allow_html=True)