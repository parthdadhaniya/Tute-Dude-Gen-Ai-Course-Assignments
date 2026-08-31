import streamlit as st

st.title("Price Calculator")

# Input product price and discount percentage
price = st.number_input("Product Price", min_value=0.0, value=1000.0)
discount = st.slider("Discount (%)", 0, 50, 10)

if st.button("Calculate"):
    final_price = price - (price * discount / 100)
    st.success(f"Final Price: {final_price}")
    
    # Comparison table
    table_data = [
        ["Before", "After"],
        [price, final_price]
    ]
    st.table(table_data)
