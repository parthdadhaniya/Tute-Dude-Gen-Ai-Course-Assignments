import streamlit as st

st.title("Product Form")

# Sidebar inputs
name = st.sidebar.text_input("Product Name")
category = st.sidebar.selectbox("Category", ["Electronics", "Clothing", "Books", "Groceries"])
price = st.sidebar.number_input("Price", min_value=0.0, value=100.0)

if st.sidebar.button("Add Product"):
    st.success("Product added successfully!")
    st.write("Product Name:", name)
    st.write("Category:", category)
    st.write("Price:", price)
