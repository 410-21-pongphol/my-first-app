import streamlit as st
st.title("🛒แอปพลิเคชั่นคำนวณราคาสินค้าพร้อมส่วนลด 10%")
price = st.number_input("กรอกราคาสินค้า (บาท):", value=0.0)
discount = price * 0.10
net_price = price - discount
st.header(f"• ภาษีมูลค่าเพิ่ม (VAT 10%): **{discount:.2f}** บาท")
st.header(f"• ราคาสุทธิ: {net_price:.2f} บาท")
st.divider()
