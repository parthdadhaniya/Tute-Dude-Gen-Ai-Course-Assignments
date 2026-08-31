import streamlit as st

st.title("Simple Sales Dashboard")
st.write("Monthly sales performance dashboard.")

months = ["January", "February", "March", "April"]

sales = {
    "January": 1200,
    "February": 1500,
    "March": 900,
    "April": 2000
}

selected_month = st.selectbox("Select Month", months)

# Display sales metric for selected month
st.metric(f"Sales for {selected_month}", sales[selected_month])

# Bar chart of sales values
st.bar_chart(list(sales.values()))
